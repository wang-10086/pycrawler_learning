import re
import requests

# match()方法
content = 'Hello 123 4567 World_This is a Regex Demo'
result = re.match('^Hello\s\d\d\d\s\d{4}\s\w{10}', content)
print(result)
print(result.group())
print(result.span())

# 匹配目标
result = re.match('^Hello\s(\d{3})\s(\d{4})\sWorld', content)
print(result)
print(result.group(1), result.group(2))

# 通用匹配
result = re.match('^Hello.*Demo$', content)
print(result)
print(result.group())

# 贪婪与非贪婪
result = re.match('^He.*(\d+).*Demo$', content)             # 单纯的.*表示贪婪匹配
print('贪婪匹配:', result.group(1))
result = re.match('^He.*?(\d+).*Demo$', content)            # 而.*?则表示非贪婪匹配
print('非贪婪匹配：', result.group(1))

# 修饰符
content = ""'Hello 1234567 World_This' \
          'is a Regex Demo'                                 # 此处的content与之前的区别在于中间多了一个换行符
result = re.match('^He.*?(\d+).*?Demo$', content, re.S)     # 这时我们传入修饰符re.S使得.匹配包括换行符在内的所有字符
print('修饰符', result.group(1))

# 转义匹配
content = '(百度)www.baidu.com'
result = re.match('^\(百度\)www\.baidu\.com$', content)

# search()
content = 'Extra stings Hello 1234567 World_This is a Regex Demo Extra stings'
result = re.search('Hello.*?(\d+).*?Demo', content)
print('转义匹配：', result.group(1))

# search()方法筛选爱奇艺影片
response = requests.get('https://www.iqiyi.com/dianying/?vfrm=pcw_home&vfrmblk=C&vfrmrst=712211_channel_dianying')
html = response.text
# print(html)
result = re.search('data-indexfocus-currenttitleelem=(.*)\n', html)
print(result.group(1))

# findall()方法筛选爱奇艺影片
results = re.findall('data-indexfocus-currenttitleelem=(.*)\n', html)
print(results)
for result in results:
    print(result)

# sub()方法的使用
content = '421rb4bre23eib'
content = re.sub('\d+', '', content)            # 将所有数字替换为空，即删除所有数字
print(content)

# compile()方法的使用
content1 = '2016-12-15 12:00'
content2 = '2016-12-17 12:55'
content3 = '2016-12-22 13:21'
pattern = re.compile('\d{2}:\d{2}')             # 将正则字符串编译成正则表达式类型
result1 = re.sub(pattern, '', content1)
result2 = re.sub(pattern, '', content2)
result3 = re.sub(pattern, '', content3)
print(result1, result2, result3)