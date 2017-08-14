#coding :utf-8
import requests
import json


baseUrl='http://d1.weather.com.cn/calendar_new/2017/101160101_2017%s.html?_=1502716678373'
user_agent='Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36'
head={
    'Accept':'*/*',
    'Accept-Encoding' : 'gzip,deflate',
    'Accept-Language':'zh-CN,zh;q=0.8',
    'Connection':'keep-alive',
    'Cookie':'vjuids=-724f10927.15de0c54f84.0.19dc2abd122e9; UM_distinctid=15de0c550171ed-05a9c0f9e75fb2-59462f1d-100200-15de0c5501978e; BIGipServerd1src_pool=1874396221.20480.0000; f_city=%E5%8C%97%E4%BA%AC%7C101010100%7C; Hm_lvt_080dabacb001ad3dc8b9b9049b36d43b=1502714613,1502715843,1502716201,1502716208; Hm_lpvt_080dabacb001ad3dc8b9b9049b36d43b=1502716666; vjlast=1502714614.1502714614.30',
    'Host':'d1.weather.com.cn',
    'Referer':'http://www.weather.com.cn/weather40d/101160101.shtml',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36'
}


for month in range(1,13):
    # print(month)
    if month<10:page=str(0)+str(month)
    else:page=str(month)
    url=baseUrl%page
    r = requests.get(url, headers=head)
    r.encoding = 'utf-8'
    weather = r.text
    weaList = weather.lstrip('var fc40 = [').split('},')
    for i in weaList:
        if i.endswith(']'):
            i=i.rstrip(']')
        elif not i.endswith('}'):
            i=i+'}'
        #通过以上步骤将字符串变为{key1:val1,key2:val2...}
        x=json.loads(i)     #变为字典类型
        if int(x['date'])>20171231:
            break
        print(x['date'],'高温：',x['hmax'],'低温：',x['hmin'])




#json  str  re