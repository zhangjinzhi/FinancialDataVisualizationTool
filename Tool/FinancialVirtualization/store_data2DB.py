#coding=utf-8
import tushare as ts
import sys
from sqlalchemy import create_engine
from sqlalchemy.types import VARCHAR
def get_hist_data(stock_code):
    stock = ts.get_hist_data(code=str(stock_code),start='2014-01-01',end='2017-01-01')

    # print type(stock)
    engine = create_engine('mysql+pymysql://root:zjz4818774@127.0.0.1/tusharedata?charset=utf8')

    try:
        stock.to_sql('code'+str(stock_code), engine, if_exists='replace',dtype={'date': VARCHAR(stock.index.get_level_values('date').str.len().max())})

    except Exception, e:
        print Exception, ":", e
        return "wrong"

    return "ok"

if __name__ == '__main__':
    # stock_code = "601766"
    stock_code = "603996"
    result = get_hist_data(stock_code)
    print result
