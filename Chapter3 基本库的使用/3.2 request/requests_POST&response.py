import requests

data = {'name': 'germey', 'age': '22'}                          # 设置data参数
r = requests.post('http://httpbin.org/post', data=data)
print(r.text)

r = requests.get('https://www.bilibili.com')
print(r.text)                                                   # 返回的内容（text）
print(r.content)                                                # 返回的内容（content）
print(type(r.status_code), r.status_code)                       # 返回的状态码
print(type(r.headers), r.headers)                               # 响应头
print(type(r.cookies), r.cookies)                               # cookies
print(type(r.url), r.url)                                       # url
print(type(r.history), r.history)                               # 请求历史

# 通过比较返回的状态码和内置的成功的返回状态码，来保证请求得到了正确响应
r = requests.get('https://www.baidu.com')
exit() if not r.status_code==requests.codes.ok else print('Request Successfully')