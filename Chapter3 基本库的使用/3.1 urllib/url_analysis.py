from urllib import parse

# urlparse()的使用
print('1')
url = 'www.baidu.com/index.html;user?id=5#comment'
result = parse.urlparse(url, scheme='https', allow_fragments=True)
print(type(result), result)
print(result.scheme, result[0])

# urlunparse()的使用
print('2')
data = ['http', 'www.baidu.com', 'index.html', 'user', 'id=5', 'comment']
print(parse.urlunparse(data))

# urlsplit()的使用
print('3')
url = 'http://www.baidu.com/index.html;user?id=5?comment'
result = parse.urlsplit(url)
print(result)

# urlunsplit()的使用
print('4')
data = ['http', 'www.baidu.com', 'index.html;user', 'id=5', 'comment']
print(parse.urlunsplit(data))

# urljoin()的使用
print('5')
base_url = 'http://www.baidu.com/index.html;user?id=5#comment'
new_url = parse.urljoin(base_url, 'costmer?id=8#comments')
print(new_url)

# urlencode()的使用
print('6')
params = {
    'name': 'germey',
    'age': 22
}
print(parse.urlencode(params))
print('http://www.baidu.com/index.html;user?'+parse.urlencode(params))

# parse_qs()和parse_qsl()的使用
print('7')
query = 'name=germey&age=22'
print(parse.parse_qs(query))        # 返回的是字典
print(parse.parse_qsl(query))       # 返回的是元组列表

# quote()的使用
print('8')
keyword = '壁纸'
url = 'http://www.baidu.com/s?wd='+parse.quote(keyword)
print(url)

# unquote()的使用
print('9')
url = 'http://www.baidu.com/s?wd=%E5%A3%81%E7%BA%B8'
print(parse.unquote(url))
