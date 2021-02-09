import json
import requests
from requests.exceptions import RequestException
import re
import time


def get_one_page(url):          # 定义获取网页源码函数
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/65.0.3325.162 Safari/537.36'
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None                         # 调用requests库的异常处理方法


def parse_one_page(html):       # 定义处理网页源码函数
    pattern = re.compile('<dd>.*?board-index.*?>(\d+)</i>.*?data-src="(.*?)".*?name"><a'
                         + '.*?>(.*?)</a>.*?star">(.*?)</p>.*?releasetime">(.*?)</p>'
                         + '.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>', re.S)
    # 编写好所要用的正则表达式，并将正则字符串转换为正则表达式进行复用
    items = re.findall(pattern, html)
    for item in items:
        yield {
            'index': item[0],
            'image': item[1],
            'title': item[2],
            'actor': item[3].strip()[3:],
            'time': item[4].strip()[5:],
            'score': item[5] + item[6]
        }


def write_to_file(content):       # 定义写入文件函数
    with open('result.txt', 'a', encoding='utf-8') as f:                # 调用with open()方法和.write()方法打开文件并写入内容
        f.write(json.dumps(content, ensure_ascii=False) + '\n')
        # 用JSON库的dumps()方法实现字典的序列化，指定ensure_ascii为False使得输出结果是中文而不是Unicode编码


def main(offset):                 # 定义程序运行主函数
    url = 'http://maoyan.com/board/4?offset=' + str(offset)             # 传入一个offset作为偏移量，从而构造url进行爬取
    html = get_one_page(url)
    for item in parse_one_page(html):
        print(item)
        write_to_file(item)


if __name__ == '__main__':
    for i in range(10):
        main(offset=i * 10)
        time.sleep(1)               # 增加一个延时等待，防止爬取速度过快被反爬虫发现导致无响应
