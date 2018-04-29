#coding=utf-8
import sys
import MySQLdb
reload(sys)
sys.setdefaultencoding('utf8')

def check_data_isin_DB(stock_code):
    db = MySQLdb.connect(host='127.0.0.1', user='root', passwd='zjz4818774', db='tusharedata', port=3306,
                         charset='utf8')
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    # SQL 查询语句
    # sql = "SELECT * FROM EMPLOYEE WHERE INCOME > '%d'" % (1000)
    # sql = 'select * from PLICC_data'

    sql1 = "select date,open,high,close,low from "+stock_code
    try:
        cursor.execute(sql1)

        row = cursor.fetchone()

        if row != "":
            return "has"
        # else:
        #     return "not has"

    except MySQLdb.Error, e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])

    # 关闭数据库连接
    db.close()
    return "nothas"


if __name__ == '__main__':
    stock_code = "code601766"
    check_result = check_data_isin_DB(stock_code)
    print check_result
