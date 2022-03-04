# -*- coding:utf-8 -*-
import datetime


import gytime
import shuijishu

def sd(ddd):

    ddd = ddd
    now_time = datetime.datetime.now() + datetime.timedelta(hours=8)
    bd = now_time.strftime('%Y%m%d')
    # tomorrow = (datetime.date.today() + datetime.timedelta(days=1)).strftime("%Y%m%d")
    with open(file="icsgytime.ics", encoding="utf8", mode="w") as file_object:
        start_string = "BEGIN:VCALENDAR\nVERSION:2.0\nCALSCALE:GREGORIAN\nMETHOD:PUBLISH\nX-WR-CALNAME:" \
                       + "公演开始时间提醒" + "\nX-WR-TIMEZONE:Asia/Shanghai\n" \
                       + "X-WR-CALDESC:"+bd+"微博发布了公演\n"
        file_object.write(start_string)
        body = gytime.sdf(ddd)
        body_string = ("BEGIN:VEVENT\nDTSTAMP:20220912T184136Z\nUID:",
                       "END:VEVENT\n")


        if body==None:
            print('今天没有发布公演。')
        else:
            for item in body:
                body0 = body_string[0]
                body1 = item[0] + 'almanac_in_' + shuijishu.suiji() + "\n"
                body2 = "DTSTART;VALUE=DATE:" + item[0] + "\nDTEND;VALUE=DATE:" + item[0] + "\n"
                beizhu = "DESCRIPTION:" +"\n"
                body3 = "SUMMARY:" + "现在公演开始了！" + "\n"
                tixing0 = "BEGIN:VALARM" + "\n" + "TRIGGER;VALUE=DATE-TIME:" + item[0] + "T"+item[1]+"Z" + "\n"
                tixing1 = "ACTION:DISPLAY" + "\n" + "END:VALARM" + "\n"
                body4 = body_string[1]
                full_body = body0 + body1 + body2 + beizhu + body3 + tixing0 + tixing1 + body4
                file_object.write(full_body)
            end_string = "END:VCALENDAR"
            file_object.write(end_string)
    return '函数icsgytime.py执行ok'
