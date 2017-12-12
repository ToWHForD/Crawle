# coding = utf-8
#这个Downloader.py的作用是提供下载作用



import requests
from urllib.parse import quote
import pymysql
import re
import os
import threading

#DIR代表默认路径，MAX代表下载的最大数量，SET_IMG_LIST代表已经下载的图片网址集合
DIR = "D:\\TEMP\\Crawle"
MAX = 200
SET_IMG_LIST = set()

#解码表
str_table = {
    '_z2C$q': ':','_z&e3B': '.','AzdH3F': '/'
}

char_table = {
    'w': 'a',
    'k': 'b',
    'v': 'c',
    '1': 'd',
    'j': 'e',
    'u': 'f',
    '2': 'g',
    'i': 'h',
    't': 'i',
    '3': 'j',
    'h': 'k',
    's': 'l',
    '4': 'm',
    'g': 'n',
    '5': 'o',
    'r': 'p',
    'q': 'q',
    '6': 'r',
    'f': 's',
    'p': 't',
    '7': 'u',
    'e': 'v',
    'o': 'w',
    '8': '1',
    'd': '2',
    'n': '3',
    '9': '4',
    'c': '5',
    'm': '6',
    '0': '7',
    'b': '8',
    'l': '9',
    'a': '0'
}


#解码函数
def decode(url):
    # 先替换字符串
    for key, value in str_table.items():
        url = url.replace(key, value)
    # 再替换剩下的字符
    table = str.maketrans(char_table)
    return url.translate(table)


#获取下载图片列表的函数，返回一个列表值,参数是一个搜索关键词和每次的步数，为30的倍数。
def getObjUrl(word,x):
    word = quote(word)
    #url是需要访问的网址，通过此网址，获取需要的list。
    url = r"http://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&fp=result&queryWord\
    ={word}&cl=2&lm=-1&ie=utf-8&oe=utf-8&st=-1&ic=0&word={word}&face=0&istype=2nc=1&pn={pn}&rn=60"
    urls = url.format(word = word,pn = x)
    temp = requests.get(urls).text
    re_url = re.compile(r'"objURL":"(.*?)"')
    listUrl = re.findall(re_url,temp)
    imgUrl = [decode(url) for url in listUrl]
    return imgUrl


#判断下载的存放列表是否存在的函数，提供一个path路径，若存在，则返回true，若不存在，则创建
#创建成功返回true，失败则返回false，若为true，则代表路径有效。
def mkdir(dir):
    try:
        isExists = os.path.exists(dir)
        if not isExists:
            os.makedirs(dir)
            print(dir+"成功创建。")
            return True
        else:
            return isExists

    except Exception as e:
        print("失败了，原因：",e)
        return False



#下载方法




class StartDown(threading.Thread):
    def __init__(self,url,name):
        super(StartDown,self).__init__()
        self.url = url
        self.name = name
        mkdir(DIR)
    
    def initalize(url,name): 
        req = StartDown.download(url)
        path = DIR+"\\"+name+"."+url.split(".")[-1]
        if req != None:
            try:
                with open(path,"wb") as f:
                    f.write(req)
                    f.close()
            except:
                print("失败")


    def download(url):
        try:
            return requests.get(url,timeout=15).content
        except:
            return None      

    def run(self):
            StartDown.initalize(self.url,self.name)


def do(keyword):
    #获得要下载的列表            
    x = 60
    while x < MAX:
        imglist = getObjUrl(keyword,x)
        for imgUrl in imglist:
            SET_IMG_LIST.add(imgUrl)
        x += 60
    print(len(SET_IMG_LIST))
    index = 0

    for url in SET_IMG_LIST:
        temp = StartDown(url,str(index))
        temp.start()
        index += 1
