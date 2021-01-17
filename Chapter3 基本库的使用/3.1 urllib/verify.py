from urllib.request import HTTPPasswordMgrWithDefaultRealm, HTTPBasicAuthHandler, build_opener
from urllib.error import URLError

username = 'username'
password = 'password'
url = 'https://libvpn.bjtu.edu.cn/prx/000/http/localhost/login/login.html'

# 利用Handler构建Opener
p = HTTPPasswordMgrWithDefaultRealm()				# 实例化对象HTTPBasicAuthHandler，参数为HTTPPasswordMgrWithDefaultRealm
p.add_password(None, url, username, password)		# 在实例化对象中加入相关参数
auth_handler = HTTPBasicAuthHandler(p)				# 建立一个处理验证的Handler
opener = build_opener(auth_handler)					# 使用这个Handler和build_opener()方法构建一个Opener

try:
	result = opener.open(url)
	html = result.read().decode('utf-8')
	print(html)
except URLError as e:
	print(e.reason)


