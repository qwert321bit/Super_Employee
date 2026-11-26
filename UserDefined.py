# --------------------感谢您使用Super Employees自动投递程序---------------------
# 应用版本V1.0
# 应用作者: JasonYANG17
# 仓库地址: https://github.com/JasonYANG170/Super_Employee
# Wiki教程: https://github.com/JasonYANG170/Super_Employee/wiki
# -------------用户配置选项-----------------------
poststate = 1  # 不投递0;投递1;
UseResultPush = 0  # 是否启用推送
PushToken = ''  # 在pushpush网站中可以找到
# 自定义请求的设备名称
deviceName='Lin'


# --------------平台选择--------------------
# 开启的平台请务必下滑找到该平台的配置项并填入对应配置
# 是否启用实习僧
shixiseng_state = 1
yizhanchi_state = 0
bosszhipin_state = 0
zhilianzhaopin_state = 0
maimai_state = 0
wubatongcheng_state = 0
# --------------实习僧配置项--------------------
# 是否投递(不投递:0,投递优先在线简历:1,投递优先离线简历:2)
shixiseng_postnumber=100#想要推送的数量
shixiseng_poststate = 1#是否开启推送。0:否，1:是
# Cookie(参考wiki说明获取)
shixiseng_Cookie = 'utm_source_first=PC; position=pc_default; utm_source=PC; utm_campaign=PC; SXS_XSESSION_ID=2|1:0|10:1795694221|15:SXS_XSESSION_ID|88:ZWQ3Y2E2M2E2NzNjYjIzNmMyNGJkMjI3NWIyNmRjZjQwMDBjYTc3Mzc2MjM3YzM2MWFiN2E4YWVlYjc2MjI3Zg==|a5884624e323371eb4e445d343e2fbf8f338809cc1eb29117d82daac6ef45854; SXS_XSESSION_ID_EXP=2|1:0|10:1795694221|19:SXS_XSESSION_ID_EXP|16:MTc5ODI4NjIyMQ==|6e0f644ea6c13882ea90f90637d201ba5a8f44dd747241546aa80f364db909da; affefdgx=usr_siwjj62k2wsq; sxs_usr=2|1:0|10:1795694221|7:sxs_usr|24:dXNyX3Npd2pqNjJrMndzcQ==|d28b9f4912fcb51d6e5543d4a84ace87b8a6f12e579de2779c2f8aa9093c2d51; xyz_usr=2|1:0|10:1795694221|7:xyz_usr|24:dXNyX3Npd2pqNjJrMndzcQ==|e577bbdd877c6ec26dc4e9cb8c5c2556e4e81ada8cb21cc24667f4038ce59afd; userflag=user'
# 筛选条件(带‘*’号的为必填项)
shixiseng_Search = {
    'p': "1",
    't': "0",  # 智能排序:0，最近发布优先:1      *
    'city': "北京|上海|广州|深圳|杭州",  # 地区(全国或其他省市)      *
    'nature': "",  # 类型：股份制企业|合伙企业
    'scale': "",  # 规模：50-150人|500-2000人
    'ipo': "",  # 融资：B轮|A轮
    'k': "AI应用开发",  # 岗位                     *
    'degree': "大专|本科",  # 学历：大专|本科
    'emp_chance': "",  # 空间：提供转正|面议
    'intention': "实习",  # 需求：校招|实习
    'internship_duration': "",  # 在岗时间：1个月|3个月以上
    'days_per_week': "",  # 工作时间：4天|1天
    'payment_per_day': ""  # 日薪：200-300|100以下
}
# --------------易展翅配置项--------------------
yizhanchi_postnumber=0#想要推送的数量
yizhanchi_poststate = 0#是否开启推送。0:否，1:是
yizhanchi_city="北京|上海|广州|深圳|杭州"#城市
yizhanchi_Cookie =""
yizhanchi_Search = {
    'page_size': "1000",#查询范围  *
    'page': "1",#当前页面        *
    'positiontype': "",
    'minsalary': "",#最低工资
    'maxsalary': "",#最高工资
    'show_third_position': "",
    'keyword': "",#岗位     *
    'region_id': "",
    'intern_time_id': "",
    'intern_cycle_id': "",
    'correct_id': "",
    'parttime_duration': "",
    'jianzhitype': "",
    'classid': "",
    'financid': "",
    'natureid': "",
    'scaleid': "",
    'areaid': "",
    'location': "",
    'port': "",
    'region_type': "",
    'sort': ""
}
# --------------Boss直聘配置项--------------------
bosszhipin_poststate = 1#是否开启推送。0:否，1:是
bosszhipin_postnumber=100#想要推送的数量
bosszhipin_city=""#城市
bosszhipin_Cookie =""
bosszhipin_Search = {
    'scene': "1",
    'query': "",#岗位
    'city': "",
    'experience': "",
    'payType': "",
    'partTime': "",
    'degree': "",
    'industry': "",
    'scale': "",
    'stage': "",
    'position': "",
    'jobType': "",
    'salary': "",
    'multiBusinessDistrict': "",
    'multiSubway': "",
    'page': "1",
    'pageSize': "5000"
}
# --------------智联招聘--------------------
zhilianzhaopin_poststate = 0#是否开启推送。0:否，1:是
zhilianzhaopin_postnumber=0#想要推送的数量
zhilianzhaopin_Chatstate = 0#是否开启聊天打招呼。0:否，1:是
# Cookie(参考wiki说明获取)
zhilianzhaopin_Cookie = ''
zhilianzhaopin_cvNumber=''
zhilianzhaopin_Search ={
    "pageIndex": "1",
    "S_SOU_WORK_CITY": "",#城市ID（教程获取）
    "eventScenario": "",
    "filterMinSalary": "1",
    "S_SOU_EXPAND": "SOU_COMPANY_ID",
    "pageSize": "30",
    "keywordChange": "1",
    "S_SOU_FULL_INDEX": "",#岗位
    "cvNumber": zhilianzhaopin_cvNumber,#你的ID
    "x-zp-utm-client-version": "u",
    "rt": "",
    "d": "",
    "os_version": "14",
    "channel": "tengxun",
    "version": "8.11.26",
    "platform": "4",
    "at": "",
    "identity": "1",
    "businessLine": "com.zhaopin.social",
    "anonymous": "0",
    "userRole": "0",
    "oaid": ""
}
# --------------脉脉--------------------
maimai_poststate = 0#是否开启推送。0:否，1:是
maimai_postnumber=0#想要推送的数量
# Cookie(参考wiki说明获取)
maimai_Token = ''#你的token,在Cookie
maimai_Cookie = ''
maimai_Search  = {
    'city': "",#城市
    'company_scales': "全部",
    'count': "10",
    'degree': "全部",
    'finances': "全部",
    'fr': "search_job_list_search_job_list",
    'major': "",
    'mj': "",
    'page': "0",
    'pf': "",
    'profession': "",
    'province': "",#省份
    'query': "",#岗位
    'rn': "1",
    'salary': "全部",
    'sid': "",
    'sortby': "default",
    'use_native_net': "1",
    'work_times': "全部",
    'version': "6.6.10",
    'ver_code': "",
    'channel': "MyAPP",
    'vc': "Android 14/34",
    'push_permit': "1",
    'net': "wifi",
    'open': "icon",
    'appid': "3",
    'device': "",
    'udid': "",
    'is_push_open': "1",
    'isEmulator': "0",
    'rn_version': "0.69.0",
    'launched_by_user': "1",
    'android_id': "",
    'oaid': "NA",
    'hms_oaid': "",
    'sm_dl': "0",
    'sm_did': "",
    'u': "",
    'access_token': maimai_Token,#你的token
    'webviewUserAgent': "Mozilla/5.0 (Linux; Android 14; 21051182C Build/UQ1A.240105.004.A1; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/128.0.6613.40 Safari/537.36",
    'density': "1.875",
    'screen_width': "",
    'screen_height': "",
    'launch_uuid': "",
    'session_uuid': "",
    'last_launch_time': ""
}
# --------------58同城--------------------
wubatongcheng_poststate = 0#是否开启推送。0:否，1:是
wubatongcheng_postnumber=0#想要推送的数量
wubatongcheng_Chatstate=0#是否开启聊天打招呼。0:否，1:是
# Cookie(参考wiki说明获取)
wubatongcheng_clientid = ''
wubatongcheng_cityid=''#城市ID（教程获取）
wubatongcheng_Search  = {
    'os': "android",
    'v': "1",
    'curVer': "13.10.2",
    'appId': "1",
    'format': "json",
    'searchType': "newSouList",
    'key': "",#岗位
    'action': "getListInfo,getFilterInfo,getRecTagInfo",
    'pagetype': "filterList",
    'filterParams': "{\"filterLocalId\":\"-1\",\"filterLocal\":\"\"}",
    'localname': "",
    'isNeedAd': "1",
    'page': "1",
    'extendParams': "{\"intentionArray\":[]}"
}
