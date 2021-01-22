import requests
import re

# request.get()的基础使用方法、params参数配置以及json()方法使用
data = {
    'name': 'germey',
    'age': 22
}
r = requests.get('http://httpbin.org/get', params=data)     # 使用get发送请求，并配置params参数
print(r.text)
print(r.json())                                             # 解析返回结果将json格式转化为字典格式

# 抓取网页（这里提前用到正则表达式知识抓取分析知乎问题内容），添加headers头信息
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebkit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
}
r = requests.get('https://www.zhihu.com/explore', headers=headers)              # 这里添加headers头信息和urlopen是相似的
pattern = re.compile('explore-feed.*?question_link.*?>(.*?)</a>', re.S)
titles = re.findall(pattern, r.text)
print(titles)

# 抓取二进制数据
r = requests.get('https://github.com/favicon.ico')
print(r.text)                                               # 获取返回结果的text属性
print(r.content)                                            # 获取返回结果的content属性
with open('favicon.ico', 'wb') as f:
    f.write(r.content)                                      # 利用open（）方法保存图片
