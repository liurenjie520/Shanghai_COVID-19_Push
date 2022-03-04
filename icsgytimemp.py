# -*- coding:utf-8 -*-
import datetime


import gytimetick
import shuijishu

def sd(ddd):

    ddd = ddd
    now_time = datetime.datetime.now() + datetime.timedelta(hours=8)
    bd = now_time.strftime('%Y%m%d')
    y = datetime.datetime.now().year
    y = str(y)
    # tomorrow = (datetime.date.today() + datetime.timedelta(days=1)).strftime("%Y%m%d")
    with open(file="icsgytimemp.ics", encoding="utf8", mode="w") as file_object:
        start_string = "BEGIN:VCALENDAR\nVERSION:2.0\nCALSCALE:GREGORIAN\nMETHOD:PUBLISH\nX-WR-CALNAME:" \
                       + "公演前5分钟切票提醒" + "\nX-WR-TIMEZONE:Asia/Shanghai\n" \
                       + "X-WR-CALDESC:"+bd+"微博发布了公演\n"
        file_object.write(start_string)
        body = gytimetick.timejx(ddd)
        body_string = ("BEGIN:VEVENT\nDTSTAMP:20220222T184136Z\nUID:",
                       "END:VEVENT\n")


        if body==None:
            print('今天没有发布公演。')
        else:
            for item in body:
                body0 = body_string[0]

                qiepiao0 = datetime.datetime.strptime(y + item[0], '%Y%m月%d日')
                qiepiao0 = qiepiao0.strftime('%Y%m%d')

                qiepiao1 = datetime.datetime.strptime(item[1], '%H：%M')
                h = qiepiao1.strftime('%H')
                h = int(h)
                h = h - 8
                txshi = "{0:02d}".format(h)
                txshi = str(txshi)
                # ms = t.strftime('%M%S')
                min = qiepiao1.strftime('%M')
                min = int(min)
                min = min - 5
                txmin = "{0:02d}".format(min)
                txmin = str(txmin)
                s = qiepiao1.strftime('%S')
                s = str(s)
                qiepiao1hms = txshi + txmin + s


                qiepiao2 =  item[2]



                qiepiao3 = datetime.datetime.strptime(item[3], '%H：%M')
                qiepiao3 = qiepiao3.strftime('%H')
                qiepiao3=qiepiao3+'点'

                body1 = qiepiao0 + 'almanac_in_' + shuijishu.suiji() + "\n"
                body2 = "DTSTART;VALUE=DATE:" + qiepiao0 + "\nDTEND;VALUE=DATE:" + qiepiao0 + "\n"
                beizhu = "DESCRIPTION:" +"今天切"+qiepiao2+qiepiao3+"的票！"+"\n"
                body3 = "SUMMARY:" + "5分钟后开始切"+qiepiao2+qiepiao3+"的票！" + "\n"
                tixing0 = "BEGIN:VALARM" + "\n" + "TRIGGER;VALUE=DATE-TIME:" + qiepiao0 + "T"+qiepiao1hms+"Z" + "\n"
                tixing1 = "ACTION:DISPLAY" + "\n" + "END:VALARM" + "\n"
                body4 = body_string[1]
                full_body = body0 + body1 + body2 + beizhu + body3 + tixing0 + tixing1 + body4
                file_object.write(full_body)
            end_string = "END:VCALENDAR"
            file_object.write(end_string)
    return '函数icsgytimemp.py执行ok'
