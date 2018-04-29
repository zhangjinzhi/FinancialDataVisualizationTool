# coding=utf-8
import sys
import tushare as ts
import numpy as np
import MySQLdb
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.svm import SVR
from sklearn.preprocessing import StandardScaler
from numpy import *

from changeTime2UTC import changeTime
##########################################################
reload(sys)
sys.setdefaultencoding('utf8')

import traceback


def throw_error():
    raise Exception("数据库中取出的list长度和传入的list长度不一致")
    # print "数据库中取出的list长度和传入的list长度不一致"

def onetotwo(one_list, table_name, cursor):
    two_list = []
    millseconds_list = []
    for price in one_list:
        temp_list = []

        sql = 'select date from ' + table_name + ' where close=' + str(price)
        # print sql
        try:
            cursor.execute(sql)
            row = cursor.fetchone()

        except MySQLdb.Error, e:
            print "Mysql Error %d: %s" % (e.args[0], e.args[1])
        date = "".join(row)

        millseconds = changeTime(date)
        millseconds_list.append(millseconds)

        temp_list.append(millseconds)
        temp_list.append(float(("%.2f" % price)))
        print price
        print temp_list
        two_list.append(temp_list)

    return two_list,millseconds_list


def get_predicted_data(table_name):
    # 打开数据库连接
    db = MySQLdb.connect(host='127.0.0.1', user='root', passwd='zjz4818774', db='tusharedata', port=3306,
                         charset='utf8')

    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    sql1 = 'select date,open,high,close,low,volume,ma5,ma10,ma20,price_change from '+table_name+' order by date asc'

    try:
        cursor.execute(sql1)
        rows = cursor.fetchall()

    except MySQLdb.Error, e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])

    # # 关闭数据库连接
    # db.close()

    price_data = []
    tag = []

    line_num = 0
    for row in rows:
        line_num += 1

        if line_num < 401:

            col = []
            for i in range(1, 9):
                col.append(row[i])

            price_data.append(col)

            # if row[9] > 0 :
            #    tag.append(1)
            # else:
            #    tag.append(0)
            tag.append(row[3])

    price_data = price_data[:-1]
    # print price_data
    tag = tag[1:]
    # print tag

    X = np.array(price_data)
    Y = np.array(tag)
    # print X
    # print Y
    ###########################################

    x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.4)
    # f(x) = (x - means) / standard deviation
    scaler = StandardScaler()
    scaler.fit(x_train)
    # standardization
    x_train = scaler.transform(x_train)
    x_test = scaler.transform(x_test)

    # construct SVR model
    #########################
    clf_linear = SVR(kernel='linear')
    clf_poly = SVR(kernel='poly', degree=3)
    clf_sigmoid = SVR(kernel='sigmoid')
    svr = clf_linear
    #########################
    # svr = SVR(kernel = 'rbf')

    svr.fit(x_train, y_train)
    y_predict = svr.predict(x_test)
    # print y_test
    # print y_predict
    result = hstack((y_test.reshape(-1, 1), y_predict.reshape(-1, 1)))
    # print result
    ##################################
    score = svr.score(x_test, y_test)
    # print score
    print y_test
    y_test_two_list,millseconds_list=onetotwo(y_test,table_name,cursor)
    print y_test_two_list
    y_predict_two_list = []
    if len(y_predict)==len(millseconds_list):
        # print len(y_predict)

        for i in range(len(y_predict)):
            temp_two_list = []
            temp_two_list.append(millseconds_list[i])
            temp_two_list.append(float(("%.2f" % y_predict[i])))
            y_predict_two_list.append(temp_two_list)

    else:
        throw_error()

    # 关闭数据库连接
    db.close()

    return y_predict_two_list,y_test_two_list,score
    # import matplotlib.pyplot as plt
    #
    # plt.autoscale(True, 'both', None)
    # # 绘制方格
    # plt.rc('axes', grid=True)
    # plt.rc('grid', color='0.75', linestyle='-', linewidth=0.5)
    # plt.plot(y_test, label='original close price')
    # plt.plot(y_predict, label='predicted close price')
    # plt.legend(loc='best')
    # # 设置坐标标签
    #
    # plt.xlabel('Time Interval')
    # # plt.ylabel('Close')
    # # 将x坐标日期进行倾斜
    # plt.setp(plt.gca().get_xticklabels(), rotation=20, horizontalalignment='right')
    # plt.show()


if __name__ == "__main__":

    stock_table = "PLICC_data"
    predict_data, origin_data, score = get_predicted_data(stock_table)
    print predict_data
    print origin_data
    print score