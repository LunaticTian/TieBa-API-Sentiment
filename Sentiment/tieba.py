# -*- coding: utf-8 -*-

import time
import configparser
import TiebaApiUtil
import copy
import re

"""
此处用".conf"进行配置
Python 读取写入配置文件 —— ConfigParser
https://www.cnblogs.com/feeland/p/4514771.html

    config = configparser.ConfigParser()
    config.read('test.conf')
    db_host = config.get("db", "db_port")
    
"""


# 参数配置说明
"""
[Setting]
爬取贴吧
tb:{'国际米兰','linjj','dota','dota2'}

爬取默认页数
Start：1
End：4

[Customize]
关键词
Essential:{'昨天','今天','明天','后天'}

"""


config = configparser.ConfigParser()
# 编码要设置成utf-8-sig而并不是utf-8
config.read('TiebaSetting.conf', encoding='utf-8-sig')
key = config.get("Setting", "tb")
keyList = key.split(',')
Essential = config.get("Customize", "Essential")
EssentialList = Essential.split(',')

# 休息周期
X = config.getint("Setting", "Sleep")

# 开始页数
Start = config.getint("Setting", "Start")
# 结束页数
End = config.getint("Setting", "End")

# 信息存取列表
Save = {}

# 读取文件或前一个爬取列表

OldSave = {}

# 新出现的帖子

NewList = []


# 获取ID
def GetId():
    IdList = []
    for name in keyList:
        test = TiebaApiUtil.GetPage(key=name,Start=Start,End=End)
        test1 = eval(test)
        # print(test1)
        for i in test1['Page']:
            for x in i.values():
                for j in x:
                    IdList.append(j['Id'])
    # print(IdList.__len__())
    return IdList


# 存取相关关键词详细信息

OldKeyText = {}
KeyText = {}

'''
{
123123123 : [
{
}
]


}

'''



# 获取TEXT 以及对比
def GetText(list):

    for id in list:

        # 标志  为0则代表无关键词，为1则有关键词
        T = 0

        # 存放 某个ID的所有关键回复楼
        KeyList = []

        Text = TiebaApiUtil.GetTiebaOne(id)

        test1 = eval(Text)
        # print(str(test1))

        for i in test1:
        # 检测回复是否有关键词
            try:
                if OneToOne(i['Text']):
                    # 存放关键词检索
                    T = 1
                    key = {
                        'Author': i['Author'],
                        'Text':i['Text'],
                        'Time':i['Time']
                    }

                    KeyList.append(key)

                    # ID 在Save中

                    if str(id) in Save:
                        # print('旧ID')
                        Save[str(id)] += 1
                    # ID 不在Save中
                    else:
                        # print('出现新ID')
                        Save[str(id)] = 1
                # 检测楼中楼是否存在
                if  not (i['FloorInFloor']  == '' or i['FloorInFloor']  == None or i['FloorInFloor']  == []):

                    # 存在楼中楼则遍历
                    for f in i['FloorInFloor']:

                        if OneToOne(f['Text']):

                            # 存放关键词检索
                            T = 1
                            key = {
                                'Author': f['Author'],
                                'Text': f['Text'],
                                'Time': f['Time']
                            }

                            KeyList.append(key)

                            if str(id) in Save:
                                # print('旧楼中楼ID')
                                Save[str(id)] += 1
                            else:
                                # print('新楼中楼ID')
                                Save[str(id)] = 1
            except TypeError:
                pass
        if T == 1:
            T = 0
            KeyText[str(id)] = copy.deepcopy(KeyList)
            KeyList.clear()




def OneToOne(Text):
    for i in EssentialList:
        if  i in Text:
            return True


'''

# 信息存取列表
Save = {}

# 读取文件或前一个爬取列表

NewSave = {}

'''
def ComparisonDict():
    # print('This is OldSave: '+ str(OldSave))
    # print('This is Save: '+ str(Save))

    for x in Save:
        for i,y in zip(OldSave,range(1,len(OldSave)+1)):
            # print(str(len(OldSave)) + '    y '+ str(y))
            if x == i:
                # 值相同
                # print('KEY相同')
                # print(str(x))
                if not Save[x] == OldSave[i]:
                    # print('值不相同')
                    NewList.append(str(i))
                break
            # if y == len(OldSave):
            #     # print('y == len(OldSave)')
            #     # print(x +"     "+i)
            if y == len(OldSave) and  x != i:
                # print('test2222')
                NewList.append(str(x))

    OldSave.clear()
    OldSave.update(copy.deepcopy(Save))
    Save.clear()
 # 5800836228     3244759899

# 程序每次完成循环都要存取一次

# 判断NewList 是否为空

NewKey = {}
dict = {}

def ComparisonDictKey():
    # print('This is OldKeyText: ' + str(OldKeyText))
    # print('This is KeyText: ' + str(KeyText))



    for New in KeyText:
        list = []


        # 判断新的KeyText的ID是不是在OldKeyText中，如果在则对比是否有不同
        if New in OldKeyText.keys():
            T = 0
            for K in KeyText[New]:

                for O,C in zip(OldKeyText[New],range(1,len(OldKeyText[New])+1)):
                    if K['Text'] == O['Text'] and K['Author'] == O['Author'] and K['Time'] == O['Time']:
                        break
                    if C == len(OldKeyText[New]) and (K['Text'] != O['Text'] or K['Author'] != O['Author'] or K['Time'] != O['Time']):
                        print(K)
                        list.append(K)
                        T = 1
            if T == 1:
                dict[New] = copy.deepcopy(list)
                list.clear()
                T = 0
        else:
            dict[New] = copy.deepcopy(KeyText[New])

    print('This is Update '+str(dict))

    OldKeyText.clear()
    OldKeyText.update(copy.deepcopy(KeyText))
    KeyText.clear()















def FileOpen():
    with open('list.tieba','r',encoding='utf-8') as file:
        save = file.read()
        OldSave.update(eval(save))

    with open('key.tieba','r',encoding='utf-8') as file:
        oldkeytext = file.read()
        OldKeyText.update(eval(oldkeytext))

def FileSave():
    with open('list.tieba','w',encoding='utf-8') as file:
        file.write(str(OldSave))

    with open('key.tieba','w',encoding='utf-8') as file:
        file.write(str(OldKeyText))




def ini():
    # 初始化
    try:
        F = open('list.tieba','r',encoding='utf-8')
        F.close()
    except OSError :
        print('初始化')
        GetText(GetId())
        OldSave.update(copy.deepcopy(Save))
        Save.clear()
        FileSave()

    return



def Main():


    time.sleep(X)
    print('开始运行')
    # 清空对比函数
    NewList.clear()
    dict.clear()
    # 获取Save
    GetText(GetId())
    # 对比Save to OldSave
    ComparisonDict()
    ComparisonDictKey()
    # 保存以防错误
    FileSave()
    print('This is NewList : ' + str(NewList))
    print(dict)
    c = dict_string(dict)



    return c




def setting():
    # print(keyList)
    # print(EssentialList)
    # print(X)
   #  print('监控贴吧列表: '+ str(keyList) + '\n' + '监控关键词: '+ str(EssentialList) + '\n'+ '监控周期: ' + str(X) + '\n'+'开始-终止/页数: '+ str(Start)+'-'+str(End))
    return '监控贴吧列表: '+ str(keyList) + '\n' + '监控关键词: '+ str(EssentialList) + '\n'+ '监控周期: ' + str(X) + '\n'+'开始-终止/页数: '+ str(Start)+'-'+str(End)

def GetSetting():
    return keyList,EssentialList,X,Start,End
'''
帖子地址：https://tieba.baidu.com/p/5806299422
遥远彼方(12:24):

'''

def dict_string(dict):
    res = ''
    url = 'https://tieba.baidu.com/p/'
    for one in dict:
        IDurl = url + one

        str1 = ''
        for i in dict[one]:

            a = re.compile('< img .*?"/>', re.I)
            b = re.compile('<a h.*?">', re.I)
            c = re.compile('<br/>', re.I)
            f = re.compile('<img .*?"/>', re.I)
            d = a.sub('', str(i['Text']))
            d = b.sub('', str(d))
            d = c.sub(' ', str(d))
            d = f.sub(' ', str(d))

            str1 = str1 + i['Author'] + '('+i['Time']+')'+':'+d + '\n\n'

        res = res + '帖子地址: '+IDurl + '\n' + str1 + '\n'
        print(res)
    return res




# 更改配置

def SetSetting(dict):
    global keyList,EssentialList,X,Start,End

    keyList = dict['监控贴吧列表']
    EssentialList = dict['监控关键词']
    X = dict['监控周期(S)']
    Start = dict['开始页数']
    End = dict['结束页数']

    # 写入文件
    config = configparser.ConfigParser()
    # 编码要设置成utf-8-sig而并不是utf-8
    config.read('TiebaSetting.conf', encoding='utf-8-sig')

    config.set('Setting','Sleep',str(X))
    config.set('Setting', 'Start', str(Start))
    config.set('Setting', 'End', str(End))
    config.set('Setting', 'tb', ','.join(keyList))
    config.set('Customize', 'Essential', ','.join(EssentialList))

    with open("TiebaSetting.conf", "w+",encoding='utf-8') as f:
        config.write(f)

    return '监控贴吧列表: ' + str(keyList) + '\n' + '监控关键词: ' + str(EssentialList) + '\n' + '监控周期: ' + str(
        X) + '\n' + '开始-终止/页数: ' + str(Start) + '-' + str(End)


