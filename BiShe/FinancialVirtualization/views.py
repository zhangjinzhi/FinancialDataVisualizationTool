#coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse
import json
import operator

from check_DB import check_data_isin_DB
from store_data2DB import get_hist_data
from get_data_fromDB import get_data_list
from get_name_by_code import get_stock_name
from predict_result import get_predicted_data

import sys
reload(sys)
sys.setdefaultencoding('utf8')

def home(request):

    return render(request, 'introduction/index.html')
# http://www.cnblogs.com/starof/p/4724381.html
# http://www.cnblogs.com/fnng/p/3750596.html   可以借鉴登录注册的后台逻辑
def login(request):

    return render(request, 'introduction/login.html')
def register(request):

    return render(request, 'introduction/register.html')

def contact(request):

    return render(request, 'introduction/contact.html')

def baidumap(request):

    return render(request, 'introduction/baidumap.html')

def default_highstocks(request):
    stock_name = '中国人寿'

    candlestick_volume_data_tupleArg = ["open", "high", "low", "close","volume"]
    candlestick_data_tupleArg = ["open", "high", "low", "close"]
    basicline_data_tupleArg = ["close"]

    # tupleArg = ["open","high","low","close","volume"]
    table = 'PLICC_data'

    candlestick_volume_data = get_data_list(table, *candlestick_volume_data_tupleArg)
    candlestick_data = get_data_list(table, *candlestick_data_tupleArg)
    basicline_data = get_data_list(table, *basicline_data_tupleArg)
    # print basicline_data
    print "################################"

    predict_data, origin_data, score = get_predicted_data(table)

    predict_data.sort(key=operator.itemgetter(0))
    origin_data.sort(key=operator.itemgetter(0))
    # print origin_data

    return render(request, 'function/query_stock.html', {'stock_name': json.dumps(stock_name),'candlestick_data': json.dumps(candlestick_data),'basicline_data': json.dumps(basicline_data),'candlestick_volume_data': json.dumps(candlestick_volume_data),'origin_data': json.dumps(origin_data),'predict_data': json.dumps(predict_data)})

def search_stock(request):
    Raw_StockID = request.GET['StockID']
    # stock_code = "code601766"
    StockID = "code"+str(Raw_StockID)
    #存储数据到数据库中
    if check_data_isin_DB(StockID) == "nothas":
       print "nothas"
       if get_hist_data(Raw_StockID) == "wrong":
           print "wrong"
           return render(request, '404.html')

    candlestick_volume_data_tupleArg = ["open", "high", "low", "close","volume"]
    candlestick_data_tupleArg = ["open", "high", "low", "close"]
    basicline_data_tupleArg = ["close"]

    # tupleArg = ["open","high","low","close","volume"]
    stock_name = get_stock_name(str(Raw_StockID))
    table = StockID

    candlestick_volume_data = get_data_list(table, *candlestick_volume_data_tupleArg)
    candlestick_data = get_data_list(table, *candlestick_data_tupleArg)
    basicline_data = get_data_list(table, *basicline_data_tupleArg)
    # print basicline_data

    predict_data, origin_data, score = get_predicted_data(table)

    predict_data.sort(key=operator.itemgetter(0))
    origin_data.sort(key=operator.itemgetter(0))
    # print origin_data

    return render(request, 'function/query_stock.html', {'stock_name': json.dumps(stock_name),'score':score,'candlestick_data': json.dumps(candlestick_data),'basicline_data': json.dumps(basicline_data),'candlestick_volume_data': json.dumps(candlestick_volume_data),'origin_data': json.dumps(origin_data),'predict_data': json.dumps(predict_data)})


def wrong(request):

   return render(request, '404.html')


