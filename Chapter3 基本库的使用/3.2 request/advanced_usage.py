import requests

# 文件上传
files = {'file': open('favicon.ico', 'rb')}                 # 该部分是固定的files参数设置
r = requests.post('http://httpbin.org/post', files=files)   # 传递files参数发送请求
print(r.text)

# 获取Cookies
r = requests.get('https://www.baidu.com')
print(r.cookies)                                            # 直接调用cookies属性即可
for key, value in r.cookies.items():
    print(key+'='+value)                                    # 遍历用items（）方法转化得到的由元组组成的列表，输出每个Cookie的值

# 会话维持
s = requests.Session()
s.get('http://httpbin.org/cookies/set/number/123456789')
r = s.get('http://httpbin.org/cookies')
print(r.text)

# SSL证书验证
# from requests.packages import urllib3
# import logging

# urllib3.disable_warnings()                                        # 直接设置忽略警告
# logging.captureWarnings(True)                                     # 捕获警告到日志
response = requests.get('https://www.12306.cn', verify=False)       # 设置verify参数为False，从而不进行证书验证
print(response.status_code)

# 指定一个本地证书作为客户端证书（注意：该部分代码仅供演示，缺少crt文件和key文件无法运行）
# r = requests.get('https://www.12306.cn', cert=('/path/server.crt', '/path/key'))
# print(r.status_code)

# 代理设置
#  直接进行代理设置
# proxies = {
#     'http': 'http://10.10.1.10:3128',
#     'https': 'http://10.10.1.10:1080',
# }
#  当代理需要使用HTTP Basic Auth时，可以按照以下语法进行设置代理
proxies = {
    'http': 'http://user:password@10.10.1.10:3128'
}
requests.get('https://www.taobao.com', proxies=proxies)

# 超时设置
r = requests.get('https://www.taobao.com', timeout=1)               # 直接设置超时时长
# r = requests.get('https://www.taobao.com', timeout=(0.5, 0.5))    # 对连接时间和读取时间分别进行超时设置
print(r.status_code)

# 身份验证
from requests.auth import HTTPBasicAuth

r = requests.get('http://localhost:5000', auth=HTTPBasicAuth('username', 'password'))
# r = requests.get('http://localhost:5000', auth=('username', 'password'))                # 也可以这么写，直接传元组会更简便
print(r.status_code)

# Prepared Request
from requests import Request, Session

url = 'http://httpbin.org/post'
data = {
    'name': 'germey'
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebkit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36'
}
s = Session()
req = Request('POST', url, data=data, headers=headers)
prepped = s.prepare_request(req)
r = s.send(prepped)
print(r.text)