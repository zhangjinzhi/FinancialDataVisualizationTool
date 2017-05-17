#coding=utf-8
import sys
import MySQLdb
from changeTime2UTC import changeTime
reload(sys)
sys.setdefaultencoding('utf8')

# # 打开数据库连接
# db =MySQLdb.connect(host='127.0.0.1',user='root',passwd='zjz4818774',db='tusharedata',port=3306,charset='utf8')
#
# # 使用cursor()方法获取操作游标
# cursor = db.cursor()
#
#
# # SQL 查询语句
# # sql = "SELECT * FROM EMPLOYEE WHERE INCOME > '%d'" % (1000)
# # sql = 'select * from PLICC_data'
# sql1 = 'select date,open,high,close,low,price_change from PLICC_data  order by date asc'
# sql2 = 'select date,open,high,close,low from PingAnInsurance  order by date asc'
#
# try:
#     cursor.execute(sql1)
#
#     rows = cursor.fetchall()
#     #获取连接对象的描述信息
#     # desc = cursor.description
#     # print 'cursor.description:',desc
#
#     # #打印表头，就是字段名字
#     # print "%s %3s" % (desc[0][0], desc[1][0])
#
#     # for row in rows:
#     #     print row
#
# except MySQLdb.Error,e:
#      print "Mysql Error %d: %s" % (e.args[0], e.args[1])
#
# # 关闭数据库连接
# db.close()
#
#
# for row in rows:
#     date_list = str(row[0]).split('-')
#     year =date_list[0]
#     # print year
#     temp_month = date_list[1]
#     month = re.sub(r"\b0*([1-9][0-9]*|0)", r"\1", temp_month)
#     # print month
#     temp_day = date_list[2]
#     day = re.sub(r"\b0*([1-9][0-9]*|0)", r"\1", temp_day)
#     # print day
#     t = (int(year), int(month), int(day), 0, 0, 0, 0, 0, 0)
#     secs = time.mktime( t )
#     # print "time.mktime(t) : %f" %  secs
#     # print "asctime(localtime(secs)): %s" % time.asctime(time.localtime(secs))
#     millisecond = secs*1000
#     print millisecond


def get_data_list(table_name,*tupleArg):
    db = MySQLdb.connect(host='127.0.0.1', user='root', passwd='zjz4818774', db='tusharedata', port=3306,charset='utf8')
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    # SQL 查询语句
    # sql = "SELECT * FROM EMPLOYEE WHERE INCOME > '%d'" % (1000)
    # sql = 'select * from PLICC_data'
    sql1 = 'select date'
    for i, element in enumerate(tupleArg):
        print "tupleArg %d-->%s" % (i, str(element))
        sql1 += ',' + str(element)

    sql1 = sql1 +' from ' + table_name + ' order by date asc'
    print sql1
    sql2 = 'select date,open,high,close,low from PingAnInsurance  order by date asc'
    try:
        cursor.execute(sql1)

        rows = cursor.fetchall()
        # 获取连接对象的描述信息
        # desc = cursor.description
        # print 'cursor.description:',desc

        # #打印表头，就是字段名字
        # print "%s %3s" % (desc[0][0], desc[1][0])

        # for row in rows:
        #     print row

    except MySQLdb.Error, e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])


    result_list = []

    for row in rows:
        # time = changeTime(row[0])
        # print time
        # print row[0]
        temp_list = []

        for item in row:
            temp_list.append(item)

        print temp_list[0]
        temp_list[0] = changeTime(temp_list[0])
        # print temp_list
        result_list.append(temp_list)

    # 关闭数据库连接
    db.close()
    return result_list


if __name__ == "__main__":
    # tupleArg = ["open","high","low","close"]
    # table = 'PLICC_data'
    # get_data_list(table, *tupleArg)

    compared_data_tupleArg = ["close"]
    compared_table = 'PingAnInsurance'
    compared_data = get_data_list(compared_table, *compared_data_tupleArg)
    # print compared_data
