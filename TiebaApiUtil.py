# -*- coding: utf-8 -*-
import json
import requests
from bs4 import BeautifulSoup
import re
import copy
import time

# 自制贴吧api
"""
该api依赖百度贴吧web版

贴吧api作为工具类，可制作第三方客户端，极速/个性/无广告
"""


"""
模拟三星手机访问
虽然不加headers也可正常访问，但是我们还是要严谨
"""

headers = {
    'Host': 'tieba.baidu.com',
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Mobile Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9'
}

# 获取某个贴吧页面帖子

"""
url = http://tieba.baidu.com/mo/q---9CC3CD881B0FE2BA30F4559A6AF8A941%3AFG%3D1-sz%40320_240%2C-1-3-0--2--wapp_1531379582221_177/m?kw=%E6%9E%97%E4%BF%8A%E6%9D%B0&lp=5011&lm=&pn=0
kw:贴吧关键词
pn=页数(0,20,40,60...)页数
        (1,2,3,4)
"""

"""
 pnf=1 起始页 默认为第一页 Start
 pne=3 结束页 默认为第三页 End
"""
def GetPage(key,Start=1,End=3):
    url1 = 'http://tieba.baidu.com/mo/q---9CC3CD881B0FE2BA30F4559A6AF8A941%3AFG%3D1-sz%40320_240%2C-1-3-0--2--wapp_1531379582221_177/m?kw='
    url2 = '&lp=5011&lm=&pn='

    Start = Start*20-20
    # 防止出现输入0的情况
    if Start == -20:
        Start = 0

    End = End*20


    ReturnJson = {
        'key' : key
    }
    SuperList = []
    for i in range(Start,End,20):

        url = url1 + key + url2 + str(i)

        # print(url)
        time.sleep(0.01)
        GetPageID = requests.get(url = url,headers=headers)
        if '欢迎创建本吧，与今后来到这里的朋友交流讨论' in GetPageID.text:
            Error = {
                'Error':'改吧尚未建立'
            }
            return json.dumps(Error,ensure_ascii=False)
        Soup = BeautifulSoup(GetPageID.text,'lxml')
        find = Soup.select('div.i')

        # 计数 调整标题
        c = 1

        '''
        这里需要添加一个list,这样一页就在一个list中
        
        '''
        SouList = []

        for x in find:

            # print(x)
            pattern = re.compile('kz=(.*?)&.*?">(.*?)</a>.*?回([0-9]\d*)\s(.*?)\s(.*?)</p>',re.S)
            items = re.findall(pattern, str(x))
            # print(items)
            # 这里对标题进行一次修正，防止出现 '1.\xa0' 情况
            if c < 10:
                Title = items[0][1][3:]
            else:
                Title = items[0][1][4:]

            c += 1
            # 创建一个Dict

            Son = {
                'Id':items[0][0],
                'Title':Title,
                'Reply':items[0][2],
                'Author':items[0][3],
                'Time':items[0][4]
            }
            SouList.append(Son)

        Page = {
            str(int((i + 20) / 20)): SouList
        }


        # 这里需要清空list
        """
        引入copy 
        在python 赋值是引入A=B，当清空或者销毁前者B被赋值的变量时，出现复制后的变量A为空，所以这里我们采用copy包中的deepcopy方法而不是copy方法。
        
        参考：https://www.cnblogs.com/koliverpool/p/6791579.html
        """

        SuperList.append(copy.deepcopy(Page))
        SouList.clear()
        if not '下一页' in GetPageID.text:
            break
    ReturnJson['Page'] = SuperList



    # 添加 ensure_ascii=False 防止中文乱码
    Result = json.dumps(ReturnJson,ensure_ascii=False)

    return Result

"""
获取单个页数，该函数只于贴子ID有关

http://tieba.baidu.com/mo/q---9CC3CD881B0FE2BA30F4559A6AF8A941%3AFG%3D1-sz%40320_240%2C-1-3-0--2--wapp_1531379582221_177/m?kz=4552337163&new_word=&pinf=1_2_0&pn=60&lp=6021
关键词是
KZ：帖子ID
pn：(0,30,60,90)
(1,2,3,4)

"""
def GetTiebaOne(ID):
    """
        json 格式
        {
            'Text':'balabalabala'
            'Author':'123'
            'FloorInFloor':{
                    {
                "Text": "balabalabala ",
                "Author": "123",
                "Time": "<a href=\"i?un=uacpayhs\">uacpayhs</a> <span class=\"b\">09:34"
                },{
                "Text": "回复 ",
                "Author": "极限rabbit",
                "Time": "<a href=\"i?un=uacpayhs\">uacpayhs</a> <span class=\"b\">09:34"
            },
                }

        }
    """
    # 先获取帖子第一页以及帖子回复数

    page = 0
    url1 = 'http://tieba.baidu.com/mo/q---9CC3CD881B0FE2BA30F4559A6AF8A941%3AFG%3D1-sz%40320_240%2C-1-3-0--2--wapp_1531379582221_177/m?kz='
    url2 = '&new_word=&pinf=1_2_0&pn='+ str(page)
    url3 = '&lp=6021'
    url = url1+str(ID)+url2+url3
    # print(url)
    # 于前处理
    time.sleep(0.01)
    GetContent = requests.get(url=url,headers=headers)
    # Soup = BeautifulSoup(GetContent.text,'lxml')

    #   获取页数
    # SumPage = Soup.select_one('div.h > input[type="text"]').attrs['value']

    # --------------------------------------------
    # print(str(page))
    Soup = BeautifulSoup(GetContent.text, 'lxml')
    findall = Soup.select('div.i')
    FatherList = []
    SonDict = {}

    # 异常以及不存在的帖子说明：

    if '您要浏览的贴子不存在' in GetContent.text:
        ReturnJ = {
            'Error' : 'Error'
        }
        return json.dumps(ReturnJ)
    # 页数增加
    for page in range(0,16122330,30):
        # 这里要对页数循环
        url1 = 'http://tieba.baidu.com/mo/q---9CC3CD881B0FE2BA30F4559A6AF8A941%3AFG%3D1-sz%40320_240%2C-1-3-0--2--wapp_1531379582221_177/m?kz='
        url2 = '&new_word=&pinf=1_2_0&pn=' + str(page)
        url3 = '&lp=6021'
        url = url1 + str(ID) + url2 + url3
        # print(url)
        time.sleep(0.01)
        GetContent = requests.get(url=url,headers=headers)

        Soup = BeautifulSoup(GetContent.text, 'lxml')
        findall = Soup.select('div.i')

        for OneContent,count in zip(findall,range(1,999)):


            if count == 1 and page == 0:

                pattern = re.compile('class="i">1楼.\s(.*?)<table>.*?<span class="g"><a href=".*?">(.*?)</a>.*?class="b">(.*?)</s', re.S)
                items = re.findall(pattern, str(OneContent))
                Text = items[0][0]
                Author = items[0][1]
                Time = items[0][2]
                SonDict['Text'] = Text
                SonDict['Author'] = Author
                SonDict['Time'] = Time
                SonDict['FloorInFloor'] = ''
                FatherList.append(copy.deepcopy(SonDict))
            else:

                pattern = re.compile('class="i">\d*楼.\s(.*?)<table>.*?<span class="g"><a href=".*?">(.*?)</a>.*?class="b">(.*?)</span>.*?href="(.*?)">回复(.*?)</a>', re.S)
                items = re.findall(pattern, str(OneContent))

                if items == [] or items == None or items == '':
                    continue
                Text = items[0][0]
                Author = items[0][1]
                Time = items[0][2]


                Floor = items[0][4][1:-1]
                # print(items)
                FloorInFloor = []
                if not (Floor == '' or Floor == None):
                    # print(items[0][2])
                    FloorInFloor = GetFloorInFloor(url=items[0][3])
                SonDict['Text'] = Text
                SonDict['Author'] = items[0][1]
                SonDict['Time'] = Time
                SonDict['FloorInFloor'] = FloorInFloor
                FatherList.append(copy.deepcopy(SonDict))
                FloorInFloor.clear()
                SonDict.clear()

            # 这里不能直接判断下一页

        if not '下一页' in GetContent.text:
            break

    FatherListJson = json.dumps(FatherList,ensure_ascii=False)
    return FatherListJson
#获取楼中楼

def GetFloorInFloor(url):
    url1 = 'http://tieba.baidu.com/mo/q---9CC3CD881B0FE2BA30F4559A6AF8A941%3AFG%3D1-sz%40320_240%2C-1-3-0--2--wapp_1531379582221_177/'

    # 这里要做一次替换，因为html的&是&amp;,做一次替换

    # 参数内置默认99
    url2 = url1 + url.replace('&amp;','&') +'&fpn='



    # 读取楼中楼信息

    ReturnList = []

    for pn in range(1,100):
        time.sleep(0.01)
        web = requests.get(url=url2+str(pn),headers=headers)
        Soup = BeautifulSoup(web.text,'lxml')
        findall = Soup.select('div.i')
        for i in findall:

            pattern = re.compile(
                '<div class="i">(.*?)<br/><a hre.*?>(.*?)</a>.*?<span class="b">(.*?)</span>',
                re.S)
            items = re.findall(pattern, str(i))
            Son = {
                'Text':items[0][0],
                'Author':items[0][1],
                'Time':items[0][2]
            }
            ReturnList.append(Son)

    # 获取楼中楼页数
        if not '下一页' in web.text:
            break
    return ReturnList






