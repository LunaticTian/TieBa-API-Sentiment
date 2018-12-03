# Tieba API Sentiment

贴吧API以及关键词提醒，舆情监控,微信陪聊机器人。

:smiley::smiley::smiley::smiley::smiley:

## Time update

- 2018/7/3 立项
- 2018/7/12 完成设计
- 2018/7/14 完成API部分
- 2018/7/19 修复API部分，完成关键词监控部分
- 2018/7/20 关键词监控部分上线，微信监控部分测试...
- 2018/7/20 修复初始化问题
- 2018/7/23 更新Sentiment人性化设置，加入全新微信机器人监控(myitchat.py)
- 2018/7/25 更新myitchat以及Sentiment API，添加配置修改内容
- 2018/7/25 Beta V0.1 上线 
- 2018/7/27 修复若干问题,正式版V1.0上线
- 2018/7/28 修复因访问速度过快引起的连接重置的bug
- 2018/10/15 增加时间过滤，修复若干BUG。


## 相关依赖
	python 3+
	pip install requests
	pip install BeautifulSoup
	pip install itchat


## 使用方法

### Windows：

点击目录下的：
***TiebaStrat.bat***

![](http://pbnsc9qwg.bkt.clouddn.com/win.jpg)


### Windows/Linux：

CMD/powershell：***python myitchat.py***

![](http://pbnsc9qwg.bkt.clouddn.com/linux.jpg)


扫码完成后即可开启贴吧微信助手。



### 微信机器人

![](http://pbnsc9qwg.bkt.clouddn.com/robet.PNG)


### 关键词舆情监控

编辑TiebaSetting.conf：

	[Setting]
	# 休眠周期/秒
	sleep = 300
	# 监控贴吧
	tb = 林俊杰,周杰伦,王力宏
	# 开始监控页数
	start = 1
	# 结束监控页数
	end = 3
	# 时间控制
	Time = 2018-10-14-0
	# 0/1  0:过滤Time之前 1:过滤Time之后 
	
	[Customize]
	# 关键词
	essential = 演唱会,华语乐坛





1. 启动微信扫码登陆
2. 输入“开启监控”,即可记录该用户ID并且在之后的监控数据以及配置修改都只有该用户可执行。
![](http://pbnsc9qwg.bkt.clouddn.com/wx1.png)
3. 输入“修改配置”，复制模板修改并且发送即可修改。
![](http://pbnsc9qwg.bkt.clouddn.com/wx5.png)
4. 享受结果。

![](http://pbnsc9qwg.bkt.clouddn.com/wx6.PNG)

----------
## 详细思路

访问我的博客：

[贴吧监控助手](http://lunatic.wang/posts/d1eb00bb/)

----------
## 自定义第三方拓展

- 第三方贴吧请以 *TieBa API Util*  拓展
- 舆情功能拓展以及其他功能拓展 *Sentiment API*
- 微信机器人拓展 *myitchat*

以上为建议拓展文件衍生。

----------
## TieBa API Util 

- 获取官方贴吧信息
- 高度自由化的信息收集
- 可制作第三方客户端
- 回复以及楼中楼形式

[<font size=4>Tieba API 相关说明</font>](/ApiRedme)

## Sentiment API 

- 自定义贴吧监控
- 自定义关键词监控
- 自定义更新周期
- 可定制化的信息收集
- 可作为其他项目工具


[<font size=4>Sentiment API 相关说明</font>](/Sentiment)

## myitchat

- 图灵机器人
- 智能对话
- 微信监控舆情
- 智能化控制

[<font size=4>myitchat 相关说明</font>](/myitchat)



## 其他说明

请勿用于商业用途
