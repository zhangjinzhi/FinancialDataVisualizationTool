# -*- coding: UTF-8 -*-
import time # 引入time模块
import re
# t = (1970, 1, 1, 8, 0, 0, 0, 0, 0)
# secs = time.mktime( t )
# print "time.mktime(t) : %f" %  secs
# print "asctime(localtime(secs)): %s" % time.asctime(time.localtime(secs))

def changeTime(date):
    date_list = date.encode("utf-8").split('-')
    # date_list = str(date).split('-')
    year = date_list[0]
    # print year
    temp_month = date_list[1]
    month = re.sub(r"\b0*([1-9][0-9]*|0)", r"\1", temp_month)
    # print month
    temp_day = date_list[2]
    day = re.sub(r"\b0*([1-9][0-9]*|0)", r"\1", temp_day)
    # print day
    t = (int(year), int(month), int(day), 0, 0, 0, 0, 0, 0)
    secs = time.mktime(t)
    # print "time.mktime(t) : %f" %  secs
    # print "asctime(localtime(secs)): %s" % time.asctime(time.localtime(secs))
    millisecond = secs * 1000
    return int(millisecond)


if __name__ == "__main__":
    date = "2016-02-06"
    changeTime(date)