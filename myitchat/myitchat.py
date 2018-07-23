import itchat
import requests
import tieba
import threading
import json


# 图灵key

KEY = 'xxxxxxxxx'


def get_response(msg, UserId):
    # 这里我们就像在“3. 实现最简单的与图灵机器人的交互”中做的一样
    # 构造了要发送给服务器的数据
    apiUrl = 'http://openapi.tuling123.com/openapi/api/v2'
    # data = {
    #     'key'    : KEY,
    #     'info'   : msg,
    #     'userid' : 'wechat-robot',
    # }

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
        "apiKey": KEY,
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
    if msg['Text'] == '开启监控'and (id == '' or id ==None ):

        # 引用全局变量
        id = msg['FromUserName']
        itchat.send_msg('已经开启监控~', toUserName=id)
        itchat.send_msg(tieba.setting(), toUserName=id)



        return
    # 这次对接收信息做一次判断
    sentence = msg['Text']

    # 如果用户发送的是YYF则执行刷任务
    print(msg['FromUserName'])



    return get_response(msg['Text'],msg['FromUserName'])

def Main():

    while 1:

        C = tieba.Main()
        print('This is myitchat: '+ str(C) )
        if C == None or C == []:
            continue
        itchat.send_msg(str(C),toUserName=id)







# itchat.auto_login(enableCmdQR=2)
itchat.auto_login(hotReload=True)
# blockThread=False 启用解除block
itchat.run(blockThread=False)
tieba.ini()
tie = threading.Thread(target=Main(), )
tie.start()





