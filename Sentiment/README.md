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
- GetSetting() 
- SetSetting() 
- dict_string()

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

---

### GetSetting() 

#### 使用方法：

tieba.GetSetting()

#### 参数说明
无

#### 方法说明：

该方法查看TiebaSetting.conf配置内容,以list形式返回

#### 返回形式：

![](http://pbnsc9qwg.bkt.clouddn.com/tieba8.jpg)

---
### SetSetting(dict) 

#### 使用方法：

tieba.GetSetting()

#### 参数说明
dict : 传入修改的配置文件信息

#### 方法说明：

该方法动态修改配置文件信息，用户在程序运行中改变关键词等配置信

#### 返回形式：


![](http://pbnsc9qwg.bkt.clouddn.com/tieba7.jpg)

---
### dict_string(dict) 

#### 使用方法：

tieba.dict_string(dict)

#### 参数说明
dict :适配关键词的Text等相关dict信息

#### 方法说明：

该方法用于去除适配的Text内容中去除HTML信息的图片标签以及其他影响阅读的标签

#### 返回形式：

> 监控到更新的数据  
>  
> 帖子地址: https://tieba.baidu.com/p/5660167836

> 
> 
> 帖子地址: https://tieba.baidu.com/p/5806639338
> 二硕影迷(7-23 19:24):回复 啦啦啦哈哈撒</a :嗯，今年刚录取的
> 
> 卿卿且苧(11:23):回复 二硕影迷</a :每天自己拿桶存水啊，或者买个和垃圾桶大的桶存一宿舍的水
> 
> 
> 帖子地址: https://tieba.baidu.com/p/5805131589
> 萝卜森兔耳德(7-22 07:42):现在马上要录取了，突然想到一个很害怕的情况！我是第二批次，十个学校知道必须专业服从调剂于是我先把那十个勾给打上了然后再写的学校和代码，问一下提交的时候我服从的调剂勾会不会没有啊感觉好吓人啊！  
> 
> 
> 帖子地址: https://tieba.baidu.com/p/5803120565
> GGXHTML(7-20 16:37):山东影制的录取 出来啦吗   </a  
> 
> a37203050(7-22 05:45):回复 GGXHTML</a :出录取了嘛
> 
> 神奇的兔酱(7-22 08:33):回复 a37203050 ：没有出，10个计划山东，最低录取到411分。 应该会追加计划
> 
> GGXHTML(7-22 09:43):这个学习的录取线大概什么时候出啊？
> 
> 
> 帖子地址: https://tieba.baidu.com/p/5808492570
> 熏熏暖风(22:40):本来江夏区算半个郊区，现在还没有地铁只有3种公交可以出去，不过地铁通了就方便了，地铁口离东湖还是有一些距离的，宿舍环境装修了，被称为酒店级宿舍，图书馆还是不错的，市区的话，江夏区的市区大概半个多小时，不过没什么玩的买买一些东西是可以的，洪山区那边公交就50分钟到街道口那边，之后去哪里有地铁就各种方便了，就是放假的时候公交人很多 
> 
> 
> 帖子地址: https://tieba.baidu.com/p/5807674831
> zzhxiannv(23:04):不知道什么预录变成录取 
> 
> 
> 帖子地址: https://tieba.baidu.com/p/5806260556
> 哈欠女神(7-23 10:49):最低528！！（2017年这所学校在海南录取最低分）
> 
> shine包仔(7-23 14:07):回复 泌夫人</a :我觉得还可以，环境不错，宿舍统一四人间，独卫，有热水有空调


