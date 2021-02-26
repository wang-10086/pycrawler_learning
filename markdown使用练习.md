# markdown使用练习



## 一、**正文及引用**

markdown是一种好用的语言

> 这是一段引用（需要多打一个回车才能结束引用）

***

## 二、网址和图片

戳这里[百度](http://www.baidu.com)

![桌面图](https://ss0.bdstatic.com/70cFvHSh_Q1YnxGkpoWK1HF6hhy/it/u=2873789948,317726200&fm=26&gp=0.jpg)

***

## 三、粗斜体

**这里是粗体**

*这里是斜体*

***这里是粗斜体***

***

## 四、表格

| 推送人 |  推送时间  | 推送内容 |
| :----: | :--------: | :------: |
|   王   | 2020.09.09 |   待定   |
|   冯   | 2020.07.23 |   待定   |

***

## 五、代码

``这是一个代码框``

```
from lxml import etree

text = '''
<div>
<ul>
<li class="item-0"><a href="link1.html">first item</a></li>
<li class="item-1"><a href="link2.html">second item</a></li>
<li class="item-inactive"><a href="link3.html">third item</a></li>
<li class="item-1"><a href="link4.html">fourth item</a></li>
<li class="item-0"><a href="link5.html">fifth item</a></li>
</ul>
</div>
'''
html = etree.HTML(text)                 # 利用HTML类对text进行初始化，构造一个XPath解析对象
result = etree.tostring(html)           # 利用tosring()方法输出修正后的HTML代码，结果为bytes类型
print(result.decode('utf-8'))           # 利用decode()方法将bytes类型转化为str类型并输出

html = etree.parse('./test.html', etree.HTMLParser())       # 直接读取文本文件进行解析
result = etree.tostring(html)
print(result.decode('utf-8'))
```



***

