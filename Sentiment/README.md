# Sentiment API

---

:tokyo_tower: :tokyo_tower: :tokyo_tower: 


## Sentiment


### 相关依赖

	import TiebaApiUtil

### 使用方法

	import tieba

内置方法：

- GetId
- GetText
- OneToOne
- ComparisonDict()
- ini()
- Main()
- setting()

内置文件:

- TiebaSetting.conf

配置文件相关参数:

	[Setting]
	
	Sleep = 18000
	# 贴吧名 贴吧用英文逗号(,)分隔符分割

	tb = 国际米兰,AC米兰,皇家马德里
	
	# 贴吧页数指定爬取 默认起始页Start=1 End = 3
	
	Start = 1
	
	End = 10
	
	[Customize]
	
	# 关键词
	
	Essential = C罗,尤文,梅西,卡卡,透

	

---
### GetId


#### 调用方法


	tieba.GetId()

#### 方法说明

该方法获取配置文件信息，获取贴吧列表调用TiebaApiUtil.GetPage()方法。


#### 返回形式：

![](http://pbnsc9qwg.bkt.clouddn.com/tieba6)





---

### GetText

#### 使用方法:

	tieba.GetText(list)

#### 参数说明：

list:获取贴吧页数标题列表，以及比较相关关键词信息

#### 方法说明

通过调用OneToOne()比较关键词,将相关数据存入Save中。

#### 返回形式


该方法没有返回值。


---
### OneToOne

#### 使用方法:

	tieba.OneToOne(Text)

#### 参数说明：

Text:用户回复内容

#### 方法说明：

将内容与关键词进行比较

#### 返回形式

该方法返回布尔值。

- True
	- 比对成功
- False
	- 比对失败 


---

### ComparisonDict

#### 使用方法：
不推荐单独使用

#### 参数说明：
无

#### 方法说明：
该方法用以Save与OldSave进行对比从而达到监控目的

#### 返回形式

重新生成新list —> NewList

#### NewList

对比差异及结果

---
### ini

#### 使用方法：
tieba.ini()

#### 参数说明：
无

#### 方法说明：
该方法用以程序第一次启动用以初始化，在程序未启动或者未生成数据文件时先行调用该方法。

#### 返回形式
无

---
### Main

#### 使用方法：

tieba.ini()

#### 参数说明
无

#### 方法说明：

该方法为监控主程序,当程序完成初始化后进行监控

#### 返回形式：

NewList ——> 该list存放监控数据变化




---

### setting()

#### 使用方法：

tieba.setting()

#### 参数说明
无

#### 方法说明：

该方法查看TiebaSetting.conf配置内容

#### 返回形式：

String 字符串形式：

![](http://pbnsc9qwg.bkt.clouddn.com/tieba7.jpg)



