
from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any
from urllib.parse import parse_qsl, urlencode, urlsplit, urlunsplit


class JobCollectorBase:
    """岗位收集系统的基础类：标准化、筛选和去重。"""

    def __init__(self, config_path: str | Path = "config/job_filters.json"):
        self.config_path = Path(config_path)

        with self.config_path.open("r", encoding="utf-8") as f:
            self.filters = json.load(f)

    @staticmethod
    def _clean(value: Any) -> str:
        """统一处理字符串，去除多余空格。"""
        if value is None:
            return ""
        return re.sub(r"\s+", " ", str(value)).strip()

    def normalize_job(self, job: dict[str, Any]) -> dict[str, Any]:
        """将不同平台的岗位数据转换为统一格式。"""
        fields = [
            "platform",
            "title",
            "company",
            "city",
            "salary",
            "education",
            "job_type",
            "url",
            "description",
        ]

        normalized = {
            field: self._clean(job.get(field))
            for field in fields
        }

        return normalized

    def match_keyword(self, job: dict[str, Any]) -> bool:
        """判断岗位标题或描述是否包含目标关键词。"""
        keywords = self.filters.get("keywords", [])

        if not keywords:
            return True

        content = (
            job["title"] + " " + job["description"]
        ).casefold()

        return any(
            keyword.casefold() in content
            for keyword in keywords
            if keyword.strip()
        )

    def match_city(self, job: dict[str, Any]) -> bool:
        """判断岗位城市是否符合要求。"""
        locations = self.filters.get("locations", [])

        if not locations:
            return True

        city = job["city"]

        return any(
            location.casefold() in city.casefold()
            for location in locations
        )

    def match_education(self, job: dict[str, Any]) -> bool:
        """判断岗位学历是否达到最低要求。"""
        education = job["education"]

        if not education:
            return False

        # 本科及以上也接受硕士、博士等更高学历
        levels = {
            "高中": 1,
            "中专": 1,
            "大专": 2,
            "本科": 3,
            "硕士": 4,
            "博士": 5,
        }

        required = self.filters.get("education", [])

        if not required:
            return True

        required_level = max(
            (levels.get(item, 0) for item in required),
            default=0,
        )

        if required_level == 0:
            return education in required

        if "不限" in education:
            return False

        if "以下" in education:
            return False

        actual_level = max(
            (
                level
                for degree, level in levels.items()
                if degree in education
            ),
            default=0,
        )

        return actual_level >= required_level

    def match_job_type(self, job: dict[str, Any]) -> bool:
        """判断岗位类型是否符合要求。"""
        job_type = job["job_type"]
        required = self.filters.get("job_type", [])

        if not required:
            return True

        if not job_type:
            return False

        return any(
            item.casefold() in job_type.casefold()
            for item in required
        )

    def match_salary(self, job: dict[str, Any]) -> bool:
        """判断薪资是否符合配置。"""
        salary_config = self.filters.get("salary", {})

        if salary_config.get("unlimited", False):
            return True

        salary = job["salary"]

        if not salary:
            return False

        if (
            salary_config.get("accept_negotiable", False)
            and "面议" in salary
        ):
            return True

        return True

    def matches_filters(self, job: dict[str, Any]) -> bool:
        """综合判断岗位是否符合全部筛选条件。"""
        return all([
            self.match_keyword(job),
            self.match_city(job),
            self.match_education(job),
            self.match_job_type(job),
            self.match_salary(job),
        ])

    @staticmethod
    def _make_job_key(job: dict[str, Any]) -> str:
        """生成岗位唯一标识，优先使用岗位链接。"""
        url = job["url"]

        if url:
            parts = urlsplit(url)

            # 去除常见追踪参数，保留其他查询参数
            query = [
                (key, value)
                for key, value in parse_qsl(parts.query)
                if not (
                    key.lower().startswith("utm_")
                    or key.lower() in {
                        "from", "source", "ref"
                    }
                )
            ]

            canonical_url = urlunsplit((
                parts.scheme.lower(),
                parts.netloc.lower(),
                parts.path.rstrip("/"),
                urlencode(query),
                "",
            ))

            return canonical_url.casefold()

        # 没有链接时使用公司、岗位和城市组合
        return "|".join([
            job["company"].casefold(),
            job["title"].casefold(),
            job["city"].casefold(),
        ])

    def deduplicate(
        self,
        jobs: list[dict[str, Any]],
    ) -> list[dict[str, Any]]:
        """去除重复岗位，保留首次出现的记录。"""
        seen = set()
        unique_jobs = []

        for job in jobs:
            key = self._make_job_key(job)

            if not key.strip("|"):
                continue

            if key not in seen:
                seen.add(key)
                unique_jobs.append(job)

        return unique_jobs

    def filter_jobs(
        self,
        jobs: list[dict[str, Any]],
    ) -> list[dict[str, Any]]:
        """执行标准化、筛选和去重。"""
        normalized_jobs = [
            self.normalize_job(job)
            for job in jobs
        ]

        matched_jobs = [
            job
            for job in normalized_jobs
            if self.matches_filters(job)
        ]

        return self.deduplicate(matched_jobs)
