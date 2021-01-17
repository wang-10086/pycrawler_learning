from urllib import request, parse, error
import socket

# 设置Request请求中各个参数
url = 'http://httpbin.org/post'
headers = {
    'User-Agent': 'Mozilla/4.0(compatible;MISE 5.5;Windows NT)',        # 伪装成浏览器
    'Host': 'httpbin.org'
}
dict = {
    'name': 'Germ'
}
data = bytes(parse.urlencode(dict), encoding='utf8')        # data参数的类型一定是bytes类型，如果不是就要用parse.urlencode进行转换

# 利用Request方法得到一个Request类型的对象
req = request.Request(url=url, data=data, headers=headers, method='POST')

# 再使用urlopen发送请求
try:
    response = request.urlopen(req, timeout=1)
except error.URLError as e:
    if isinstance(e.reason, socket.timeout):
        print("TIME OUT")                                   # 如果异常类型是socket.timeout类型，说明超时

print(response.read().decode('utf8'))
print(response.status)