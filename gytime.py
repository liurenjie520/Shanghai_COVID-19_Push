# -*- coding:utf-8 -*-
#场时间：\d+月\d\d日+\d{2,}
#xianqudiao \d+月\d\d日+\d{2,}点59分
#\d+月\d\d日+\d{2,}：+\d\d goumsishijisn
from datetime import datetime
#gytime \d+月\d\d日+\d{2,}点

#soumai \d+月\d\d日+\d{2,}点场于(.+?)售卖

import re

#\d+月\d\d日+\d{2,}点场于(.+?)售卖
def timejx(ddd):
    ddd=ddd
    strr=ddd
    # strr = "#恋爱禁止条例#公演将于2月26日（周六）19：00，本场公演为@沈莹-AKB48TeamSH生日公演；#缩略图#研修生公演将于2月26日（周六）/2月27日（周日）14：00举办；2月27日（周日）19:00举办《春日缩略图特别公演》。#缩略图#研修生公演门票将采取官方商城售卖的方式。#恋爱禁止条例#公演和《春日缩略图特别公演》门票将采取VIP门票申请实名制抽选，普通门票和站票在官方商城售卖的方式。恋爱禁止条例公演：公演场地：万代南梦宫梦想剧场时间：2月26日19点VIP门票申请🔗：网页链接VIP门票申请时间：截至2月18日20点59分普通门票&amp;站票售卖时间：2月21日18：48开始售卖春日缩略图特别公演：公演场地：万代南梦宫梦想剧场时间：2月27日19点VIP门票申请🔗：网页链接VIP门票申请时间：截至2月18日20点59分普通门票&amp;站票售卖时间：2月22日18：48开始售卖缩略图研修生公演：公演场地：万代南梦宫梦想剧场时间：2月26日14点和2月27日14点门票购买时间：2月26日14点场于2月21日17：48开始售卖2月27日14点场于2月22日17：48开始售卖"
    # qudiaostr=str.replace("\d+月\d\d日+\d{2,}点59分", "qudiao");
    qudiaostr = re.sub(r'\d{1,2}月\d{1,2}日+\d{1,2}点59分', '', strr)
    qudiaostr2 = re.sub(r'(0?[1-9]|[1][012])月(0?[1-9]|[12][0-9]|3[01])日([0-1]?[0-9]|2[0-3])点场(.+?)售卖', '', qudiaostr)
    y = datetime.now().year
    y = str(y)
    print(qudiaostr2)

    result1 = re.findall(r"\d{1,2}月\d{1,2}日+\d{1,2}点", qudiaostr2)

    # qudiaostrbt=re.findall(r"#(.+?)#", str)
    # qudiaostrbt=list(set(qudiaostrbt))
    print(type(result1))
    print((result1))

    # print(qudiaostrbt)
    qudiaostr3= re.findall(r'(0?[1-9]|[1][012])月(0?[1-9]|[12][0-9]|3[01])日([0-1]?[0-9]|2[0-3])点场(.+?)售卖', qudiaostr)

    qudiaostr3=str(qudiaostr3)
    t1=qudiaostr3.replace('[(\'', '')
    t2=t1.replace('\')]', '')
    t3=t2.replace('\'), (\'', '')
    t4 = t3.replace('\', \'', '')



    result2 = re.findall(r"\d{1,2}月\d{1,2}日\d{1,2}：\d{1,2}", t4)
    # print(result2)

    gg=[]
    opt = ''
    for i in result1:
        t = datetime.strptime(y + i, "%Y%m月%d日%H点")
        h=t.strftime('%H')
        h=int(h)
        h=h-8
        txshi = "{0:02d}".format(h)
        txshi = str(txshi)
        ms = t.strftime('%M%S')
        hms=txshi+ms
        ymd = t.strftime('%Y%m%d')





        st = (f'{ymd}', f'{hms}')
        st = str(st) + ','
        opt = opt + st
        lsat = '[' + opt + ']'
        lsat = lsat.replace('),]', ')]')


    return lsat



def sdf(ddd):
    ddd=ddd
    s=timejx(ddd)
    dicee = eval(s)
    return dicee
    # print(dicee)

# 
# if __name__ == '__main__':
#     ddd="AKB48TeamSH #缩略图#研修生公演将于3月5日（周六）/3月6日（周日）14：00举办，3月5日场是@张嘉哲-AKB48TeamSH 生日公演；#恋爱禁止条例#公演将于3月5日（周六）/3月6日（周日）19：00举办，3月6日场是@桂楚楚-AKB48TeamSH 生日公演+百场公演。#缩略图#研修生公演门票将采取官方商城售卖的方式。#恋爱禁止条例#公演门票将采取VIP门票申请实名制抽选，普通门票和站票在官方商城售卖的方式。缩略图研修生公演：公演场地：万代南梦宫梦想剧场时间：3月5日14点和3月6日14点门票购买时间：3月5日14点场于2月28日17：48开始售卖3月6日14点场于3月1日17：48开始售卖恋爱禁止条例公演：公演场地：万代南梦宫梦想剧场时间：3月5日19点和3月6日19点VIP门票申请🔗：网页链接VIP门票申请时间：截至2月25日20点59分普通门票&amp;站票售卖时间：3月5日19点场于2月28日18：48开始售卖3月6日19点场于3月1日18：48开始售卖购买了通票的用户请携带登记的身份证前往剧场领票，本月云公演也是免费哦，欢迎大家收看~金仓鼠周榜统计时间为2月26日(周六)至3月4日(周五)，每周金仓鼠总榜第一名可根据自己参加的公演选择一首歌曲进行直拍，快来为自己喜欢的成员应援吧！"
#     pp=sdf(ddd)
#     print(pp)
