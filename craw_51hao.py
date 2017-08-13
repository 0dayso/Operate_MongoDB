# coding:utf-8
import requests
from bs4 import BeautifulSoup
from requests.exceptions import RequestException
import re
from multiprocessing.dummy import Pool as ThreadPool
from pymongo import MongoClient


home_pageUrl='http://www.51hao.cc/'
user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
headers = {'User-Agent': user_agent}
all_cityUrl="http://www.51hao.cc/all.html"
cityList=[]
phoneNumber={}

def download(url):
    try:
        r = requests.get(url,headers=headers)
        r.encoding = 'gb2312'   #设置编码，不设置中文会乱码
        return r
    except RequestException as e:
        print("The problem is {}!".format(e))

def getCity(url):
    r = download(url)
    Soup = BeautifulSoup(r.text,'lxml')

    for province in Soup.find_all('a',href=re.compile(r'city/\w+$')):
        print(province.text)
        for city in Soup.find_all('a',href=re.compile(province['href']+r'/\w+.php')):
            print(city.text,city['href'])

            cityList.append(home_pageUrl+city['href'])

    p.map(getNumber,cityList)

def getNumber(url):
    r=download(url)
    Soup=BeautifulSoup(r.text,'lxml')
    title =Soup.select('div[class~=title] > span')[0].text
    ProvincePattern=re.compile(u"[\u4e00-\u9fa5]+")     #用来匹配省份
    Province_City=title[:-10]
    Province=re.search(ProvincePattern,Province_City).group().strip()
    City=Province_City[4:].strip()
    for cuc in Soup.find_all('div',class_='ab_menu cuc'):
        cucList=cuc.find_next('ul')
        for num in cucList.find_all('a',href=re.compile(r'../../mobile/')):
            db.liantong.insert_one({'号码':num.text,'省/直辖市':Province,'市':City,'运营商':'中国联通'})
    for ctc in Soup.find_all('div',class_='ab_menu ctc'):
        ctcList=ctc.find_next('ul')
        for num in ctcList.find_all('a',href=re.compile(r'../../mobile/')):
            db.dianxin.insert_one({'号码': num.text, '省/直辖市': Province, '市': City, '运营商': '中国电信'})
    for cm in Soup.find_all('div',class_='ab_menu cm'):

        cmList=cm.find_next('ul')
        for num in cmList.find_all('a',href=re.compile(r'../../mobile/')):
            db.yidong.insert_one({'号码': num.text, '省/直辖市': Province, '市': City, '运营商': '中国移动'})


client=MongoClient()
db=client.PhoneNumber
p=ThreadPool(4)
getCity(all_cityUrl)
p.close()
p.join()
# print(cityList)
