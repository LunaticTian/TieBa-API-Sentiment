# -*- coding: utf-8 -*-

import time
import configparser
import TiebaApiUtil
import copy


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
        print(test1)
        for i in test1['Page']:
            for x in i.values():
                for j in x:
                    IdList.append(j['Id'])
    # print(IdList.__len__())
    return IdList

# 获取TEXT 以及对比
def GetText(list):

    for id in list:
        Text = TiebaApiUtil.GetTiebaOne(id)

        test1 = eval(Text)
        # print('请开始你的表演')
        # print(TiebaApiUtil.GetTiebaOne(id))
        print(test1)
        for i in test1:
        # 检测回复是否有关键词

            try:
                if OneToOne(i['Text']):
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
                            if str(id) in Save:
                                # print('旧楼中楼ID')
                                Save[str(id)] += 1
                            else:
                                # print('新楼中楼ID')
                                Save[str(id)] = 1
            except TypeError:
                pass


def OneToOne(Text):
    for i in EssentialList:
        if  i in Text:
            # print(Text+ '    '+ i)
            # print ('OK')
            return True


'''

# 信息存取列表
Save = {}

# 读取文件或前一个爬取列表

NewSave = {}

'''
def ComparisonDict():
    T = 1
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

def FileOpen():
    with open('list.tieba','r',encoding='utf-8') as file:
        save = file.read()
        OldSave.update(eval(save))

def FileSave():
    with open('list.tieba','w',encoding='utf-8') as file:
        file.write(str(OldSave))




def ini():
    # 初始化
    print('初始化')
    GetText(GetId())
    OldSave.update(copy.deepcopy(Save))
    Save.clear()
    FileSave()

def Main():

    # 爬取sleep 修正时间
    # return '123123123123123'
    time.sleep(X)
    print('开始运行')
    # 清空对比函数
    NewList.clear()

    # 获取Save
    GetText(GetId())
    # 对比Save to OldSave
    ComparisonDict()
    # 保存以防错误
    FileSave()

    return NewList




def setting():
    print(keyList)
    print(EssentialList)
    print(X)
    print('监控贴吧列表: '+ str(keyList) + '\n' + '监控关键词: '+ str(EssentialList) + '\n'+ '监控周期: ' + str(X) + '\n'+'开始-终止/页数: '+ str(Start)+'-'+str(End))
    return '监控贴吧列表: '+ str(keyList) + '\n' + '监控关键词: '+ str(EssentialList) + '\n'+ '监控周期: ' + str(X) + '\n'+'开始-终止/页数: '+ str(Start)+'-'+str(End)

