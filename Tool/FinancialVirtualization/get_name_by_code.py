#coding=utf-8
import sys
import MySQLdb
reload(sys)
sys.setdefaultencoding('utf8')


def get_stock_name(stock_code):
    db = MySQLdb.connect(host='127.0.0.1', user='root', passwd='zjz4818774', db='tusharedata', port=3306,charset='utf8')
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    sql1 = 'select name from all_stock where code='+str(stock_code)
    try:
        cursor.execute(sql1)

        row = cursor.fetchone()

        name = row[0]

    except MySQLdb.Error, e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])
        return "code"+str(stock_code)

    # 关闭数据库连接
    db.close()
    return str(name)


if __name__ == "__main__":

    code = "600540"
    name = get_stock_name(code)
    print str(name)
