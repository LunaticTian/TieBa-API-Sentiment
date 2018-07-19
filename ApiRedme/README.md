# Tieba API Util 

:smiley: :smiley: :smiley: :smiley:


## TieBa API


### 相关依赖
	pip install requests
	
	pip install BeautifulSoup

### 使用方法

	import TiebaApiUtil

内置两个方法，分别是GetPage/GetTiebaOne。


### GetPage

调用方法

	TiebaApiUtil.GetPage(Key,Start,End)

参数说明：


* key：贴吧关键词
	
需要访问的贴吧关键词，譬如：'国际米兰'。

* Start：开始页数

默认为1，不能为负。

* End：结束页数

默认为3，不能为负。

该函数返回Json，返回形式为：

* key:贴吧名称
* Page：
	* X：贴吧当前页数
		* Id：帖子ID
		* Title：帖子标题
		* Reply：帖子回复数
		* Author：帖子作者
		* Time：最后回复时间


<br>

	TiebaApiUtil.GetPage(key='国际米兰',Start=1,End=3)
如下：
<br>	

	

	{
		
		"key":"国际米兰",
		"Page"::[
				{
				"1":[
					{
						"Id":"5793707221",
						"Title":"官方:埃德尔转会江苏苏宁",
						"Reply":"102",
						"Author":"树欲动而风又止",
						"Time":"23:34"
					},
					{
						"Id":"5793703055",
						"Title":"国际米兰新闻晚报，7月13日",
						"Reply":"254",
						"Author":"wyp861025",
						"Time":"23:44"
					}
					]
				}
				{
				"2":[
					{
						"Id":"5793707221",
						"Title":"官方:埃德尔转会江苏苏宁",
						"Reply":"102",
						"Author":"树欲动而风又止",
						"Time":"23:34"
					},
					{
						"Id":"5793703055",
						"Title":"国际米兰新闻晚报，7月13日",
						"Reply":"254",
						"Author":"wyp861025",
						"Time":"23:44"
					}
					]
				}
				]

	}


### GetTiebaOne

使用方法:

	TiebaApiUtil.GetTiebaOne(ID)
参数说明：

* Id:帖子唯一ID

该函数返回Json，返回形式为：

* Text：内容
* Author：用户
* Time：时间
* FloorInFloor：楼中楼
	* Text：内容
	* Author：用户
	* Time：时间

<br>


	TiebaApiUtil.GetTiebaOne(5789990094)

<br>


	{
		"Text":"<img src=\"http://tb2.bdstatic.com/tb/editor/images/client/image_emoticon25.png\"/>这么容易就爆照的，不是抠脚就是快餐<br/>",
		"Author":"一涵呦",
		"Time":"7-10 20:56",
		"FloorInFloor":[
				{
				"Text":"快餐是啥",
				"Author":"可爱的Hjkjbb",
				"Time":"14:25"
				},
				{
				"Text":"回复 <a href=\"i?un=言清欢🍒🔯🔯\">言清欢🍒🔯🔯</a> :快餐就是我们平常点的外卖。",
				"Author":"李坤铭12",
				"Time":"15:16"
				},
				{
				"Text":"回复 言清欢🍒🔯🔯 ：打一次就走的，不过夜的<img src=\"http://tb2.bdstatic.com/tb/editor/images/client/image_emoticon68.png\"/><img src=\"http://tb2.bdstatic.com/tb/editor/images/client/image_emoticon68.png\"/>",
				"Author":"啦啦队长15",
				"Time":"15:24"
				},
				{
				"Text":"回复 <a href=\"i?un=米破是张小恒\">米破是张小恒</a> :你小弟弟就这么粗。",
				"Author":"让我鸡儿放会假",
				"Time":"16:47"
				},
				{
				"Text":"卖茶叶的",
				"Author":"天生的she手",
				"Time":"20:12"
				}
			]
	}




