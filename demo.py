import datetime
import json
import os
import requests

def yujin():
    SCKEY = "2927f55550ef46b8a867ba1c3141786a"
    URL = 'https://devapi.qweather.com/v7/warning/now'

    params = {
        'key': SCKEY,
        'location': '101161007'
    }

    response_ = requests.get(URL, params=params)

    # print(response_.json())

    response = response_.json()
    now_time = datetime.datetime.now()
    bd = datetime.datetime.now().strftime('%Y%m%d')
    if response['code'] == '200':
        if response['warning']:
            id = response['warning'][0]['id']
            sender = response['warning'][0]['sender'] if 'sender' in response['warning'][0] else '未知'
            pubTime = response['warning'][0]['pubTime']
            title = response['warning'][0]['title']
            startTime = response['warning'][0]['startTime'] if 'startTime' in response['warning'][0] else '未知'
            endTime = response['warning'][0]['endTime'] if 'endTime' in response['warning'][0] else '未知'
            status = response['warning'][0]['status'] if 'status' in response['warning'][0] else '未知'
            level = response['warning'][0]['level']
            typeName = response['warning'][0]['typeName']
            text = response['warning'][0]['text']

            body = f"『{text}』    来源：{sender}  发布时间：{pubTime}   开始时间：{startTime}   结束时间：{endTime}   状态：{status}   等级：{level}   灾害类型：{typeName}"
            # body = f"{text}\n\n发送者：{sender}\n发布时间：{pubTime}\n开始时间：{startTime}\n结束时间：{endTime}\n状态：{status}\n等级：{level}\n灾害类型：{typeName}\n"
            # body=eval(body)
            dd = f"[('{bd}','{body}')]"
            dd = eval(dd)
            return dd




if __name__ == '__main__':
    print(yujin())
    print('1')
    htmldata = lasthtml(urlid)
    huanghang = "<br />"
    tu = htmljiexi.getpiclast(urlid)
    content = htmldata + huanghang + tu
    content = content.replace('"', '&quot;')
    url = 'http://wxpusher.zjiecode.com/api/send/message'
    HEADERS = {'Content-Type': 'application/json'}
    # dt = datetime.now()
    # time = dt.strftime('%Y-%m-%d')
    # 'application/x-www-form-urlencoded'
    # 'application/json;charset=utf-8'
    FormData = {
        "appToken": "AT_iaPxpUE0FLNUECu1zFnKhFR7R9NU5K8e",
        "content": content,
        "summary": f"有上海市新冠肺炎疫情防控新闻发布会！",
        "contentType": 1,

        "topicIds": [

        ],
        "uids": [
            "UID_noWsar4x3r0zd4WqjCaoD5CIX9Xi"
        ],
        "url": ""
    }

    res = requests.post(url=url, json=FormData, headers=HEADERS)
    # content = requests.post(url=url, data=FormData).text

    print(res.text)