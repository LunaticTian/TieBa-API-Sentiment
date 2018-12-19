import itchat
import requests
import tieba
import threading
import json
import platform

KEY = 'xxxxxxx'

T = 0

def get_response(msg, UserId):
    # 这里我们就像在“3. 实现最简单的与图灵机器人的交互”中做的一样
    # 构造了要发送给服务器的数据
    apiUrl = 'http://openapi.tuling123.com/openapi/api/v2'


    data = {
    "reqType": 0,
    "perception": {
        "inputText": {
            "text": msg
        },
        "inputImage": {
            "url": ""
        },
        "selfInfo": {
            "location": {
                "city": "",
                "province": "",
                "street": ""
            }
        }
    },
    "userInfo": {
        "apiKey": "42afd1a6112f4a93bbaa83022d980132",
        "userId": str(UserId)[1:33]
    }
}

    print(data)
    try:
        r = requests.post(apiUrl, data=json.dumps(data)).json()
        # 字典的get方法在字典没有'text'值的时候会返回None而不会抛出异常

        r = r['results']
        r = r[0]
        r = r['values']
        return r['text']
    # 为了防止服务器没有正常响应导致程序异常退出，这里用try-except捕获了异常
    # 如果服务器没能正常交互（返回非json或无法连接），那么就会进入下面的return
    except:
        # 将会返回一个None
        return


id = ''


@itchat.msg_register(itchat.content.TEXT)
def print_content(msg):
    # print(msg)
    global id
    print('id = |'+ id)
    print(msg['Text'] == '修改配置')
    print(id == msg['FromUserName'])
    if msg['Text'] == '开启监控' and (id == '' or id ==None ):

        # 引用全局变量
        id = msg['FromUserName']
        itchat.send_msg('已经开启监控~', toUserName=id)
        itchat.send_msg(tieba.setting(), toUserName=id)
        return

    if msg['Text'] == '修改配置' and id == msg['FromUserName']:
        Setting = tieba.GetSetting()
        a = {
            '监控贴吧列表':Setting[0],
            '监控关键词':Setting[1],
            '监控周期(S)':Setting[2],
            '开始页数':Setting[3],
            '结束页数': Setting[4]
        }
        itchat.send_msg('修改以下列信息，并且将修改后的信息复制发送', toUserName=id)

        itchat.send_msg(str(a), toUserName=id)
        return

    if  '监控贴吧列表' in msg['Text']:
        global T
        T = 1

        son = tieba.SetSetting(eval(msg['Text']))
        return son





    # 这次对接收信息做一次判断
    sentence = msg['Text']

    # 如果用户发送的是YYF则执行刷任务
    print(msg['FromUserName'])



    return get_response(msg['Text'],msg['FromUserName'])

def Main():
    global T
    i = 1
    while 1:

        C = tieba.Main()
        print('This is myitchat: '+ str(C) )
        print(T)

        if C == None or C == [] or C == ' ' or len(C) > 3452:
            continue
        if T == 1:
            T = 0
            print('改变了T: '+ str(T))

        if  T ==0 and i != 0 :
            itchat.send_msg('监控到更新的数据  \n \n'+str(C),toUserName=id)
        i += 1





# 识别系统
sysstr = platform.system()

if(sysstr =="Windows"):
    itchat.auto_login(hotReload=True)
elif sysstr == "Linux":
    itchat.auto_login(enableCmdQR=2)


# blockThread=False 启用解除block
itchat.run(blockThread=False)
tieba.ini()
tie = threading.Thread(target=Main())
tie.start()





