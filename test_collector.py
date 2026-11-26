
from collector.base import JobCollectorBase


collector = JobCollectorBase()

test_jobs = [
    {
        "platform": "实习僧",
        "title": "Python开发实习生",
        "company": "星云科技",
        "city": "北京",
        "salary": "面议",
        "education": "本科及以上",
        "job_type": "实习",
        "url": "https://example.com/job/001",
        "description": "负责Python后端开发",
    },
    {
        "platform": "智联招聘",
        "title": "大模型应用开发实习生",
        "company": "AI科技公司",
        "city": "上海",
        "salary": "5k-8k",
        "education": "硕士及以上",
        "job_type": "实习",
        "url": "https://example.com/job/002",
        "description": "参与大模型应用开发",
    },
    {
        "platform": "Boss直聘",
        "title": "Java开发工程师",
        "company": "测试公司",
        "city": "北京",
        "salary": "8k-12k",
        "education": "本科",
        "job_type": "全职",
        "url": "https://example.com/job/003",
        "description": "负责Java开发",
    },
]

result = collector.filter_jobs(test_jobs)

print(f"原始岗位数：{len(test_jobs)}")
print(f"筛选后岗位数：{len(result)}")

for job in result:
    print(
        job["title"],
        job["company"],
        job["city"],
    )
