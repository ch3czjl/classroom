#coding:utf-8
import requests
import json
import gzip
from city import city
while True:
    cityname = raw_input('你想查哪个城市的天气？\n')
    # print cityname,type(cityname)
    citycode = city.get(cityname)
    # print citycode,type(citycode),bool(citycode)
    if citycode:
        try:
            r = requests.get(url=('http://www.weather.com.cn/data/cityinfo/%s.html' % citycode))    # 最基本的GET请求
            # print(r.status_code)    # 获取返回状态
            # r = requests.get(url='http://dict.baidu.com/s', params={'wd':'python'})   #带参数的GET请求
            # print(r.url)
            # print r.encoding,type(r.encoding)
            # print r.content.encode(encoding)
            if r.encoding != 'ISO-8859-1':
                r = gzip.open(r)
            # r1 = gzip.open(r)

            r.encoding = 'utf-8'
            # print r.text,type(r.text)  #打印解码后的返回数据
            # print r.text
            data = r.text
            result = json.loads(data)
            # print type(result)
            result_1 = result['weatherinfo']
            str_temp = ('%s\n%s~%s')%(
                result_1['weather'],
                result_1['temp1'],
                result_1['temp2']
            )
            print str_temp
        except:
            print '查询失败'
    else:
        print '没有找到该城市'