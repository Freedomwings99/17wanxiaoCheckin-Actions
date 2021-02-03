"""
Server酱推送服务
https://sc.ftqq.com/3.version
"""
import requests


def server_push(sckey, title, desp):
    """
    :param sckey: 官网获取 sckey，用来发送消息，测试版请修改接口 url 地址
    :param title: 发送消息的标题
    :param desp: 发送文本
    :return:
    """
    send_url = f"https://sc.ftqq.com/{sckey}.send"
    params = {"text": title, "desp": desp}
    try:
        res = requests.post(send_url, data=params).json()
        """
        {"errno":1024,"errmsg":"bad pushtoken"}
        {"errno":0,"errmsg":"success","dataset":"done"}
        {"errno":1024,"errmsg":"不要发送重复的内容"}
        """
        if not res["errno"]:
            return {"status": 1, "msg": "Server酱推送服务成功"}
        else:
            return {"status": 0, "errmsg": f"Server酱推送服务失败，{res['errmsg']}"}
    except Exception as e:
        return {"status": 0, "errmsg": f"Server酱推送服务失败，{e}"}


if __name__ == '__main__':
    sckey = "SCU90543Ta7d070aba5fa5f6976b8f05dd98b32085e7615bc0f542"
    title = "完美校园健康打卡推送"
    desp = """
------
#### 现在时间：
```
2021-02-02 20:00:34 PM
```
#### 冯剑平healthy打卡信息：
```
{
    "businessType": "epmpics",
    "jsonData": {
        "areaStr": "{\"streetNumber\":\"\",\"street\":\"\",\"district\":\"湘潭县\",\"city\":\"湘潭市\",\"province\":\"湖南省\",\"town\":\"\",\"pois\":\"曲尺塘\",\"lng\":112.71891100000371,\"lat\":27.818064989315328,\"address\":\"湘潭县曲尺塘\",\"text\":\"湖南省-湘潭市\",\"code\":\"\"}",
        "customerid": "1999",
        "deptStr": {
            "deptid": 141659,
            "text": "土木工程学院-测绘工程-2017测绘工程2班"
        },
        "deptid": 141659,
        "gpsType": 1,
        "phonenum": "17377820279",
        "reportdate": 1612267229638,
        "source": "app",
        "stuNo": "20172987",
        "templateid": "pneumonia",
        "token": "e39c768d-17ef-4d81-aade-3a1fd4e4128d",
        "updatainfo": [
            {
                "propertyname": "bodyzk",
                "value": "正常温度(小于37.3)"
            },
            {
                "propertyname": "istouchcb",
                "value": "自己家中"
            },
            {
                "propertyname": "sfwz2",
                "value": "内地学生"
            },
            {
                "propertyname": "symptom",
                "value": "无"
            },
            {
                "propertyname": "homehealth",
                "value": "无"
            },
            {
                "propertyname": "isConfirmed",
                "value": "无"
            },
            {
                "propertyname": "ownbodyzk",
                "value": "良好"
            },
            {
                "propertyname": "ishborwh",
                "value": "无"
            },
            {
                "propertyname": "outdoor",
                "value": "绿色"
            },
            {
                "propertyname": "ownPhone",
                "value": "17377820279"
            },
            {
                "propertyname": "emergencyContact",
                "value": "郑怀玲"
            },
            {
                "propertyname": "mergencyPeoplePhone",
                "value": "18674490817"
            }
        ],
        "userid": "6274894",
        "username": "冯剑平"
    },
    "method": "submitUpInfo"
}
```
------
| Text                           | Message |
| :----------------------------------- | :--- |
| 今日体温 | 正常温度(小于37.3) |
| 自己当日所在位置 | 自己家中 |
| 身份类别 | 内地学生 |
| 是否出现可疑症状 | 无 |
| 是否存在以下高危行为 | 无 |
| 医学诊断情况及被要求采取医学措施的情况 | 无 |
| 同居住家庭成员身体健康状况 | 良好 |
| 所在小区是否有疫情 | 无 |
| 居民健康码颜色 | 绿色 |
| 本人电话 | 17377820279 |
| 紧急联系人姓名 | 郑怀玲 |
| 紧急联系人电话 | 18674490817 |
------
```
{'msg': '成功', 'code': '10000', 'data': 1}
```
------
#### 1858，获取user_info失败，打卡失败
------


>
> [17wanxiaoCheckin-Actions](https://github.com/ReaJason/17wanxiaoCheckin-Actions)
>
>期待你给项目的star✨

[INFO]; {'status': 0, 'errmsg': "Server酱推送服务失败，'dict' object has no attribute 'text'"}
[INFO]; {'status': 1, 'msg': 'QQ邮箱推送成功'}
[INFO]; {'status': 1, 'msg': 'Qmsg酱推送服务成功'}
"""
    print(server_push(sckey, title, desp))
