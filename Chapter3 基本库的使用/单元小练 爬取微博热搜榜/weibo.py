import requests
import re
import json
from requests.exceptions import RequestException
import os


def get_page(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/65.0.3325.162 Safari/537.36'
        }
        response = requests.get(url, headers=headers)
        html = response.text
        if response.status_code == 200:
            return html
        return None
    except RequestException:
        return None


def parse_page(html):
    pattern = re.compile('<td.*?ranktop">(.*?)</td>.*?<a.*?target.*?>(.*?)</a>', re.S)
    items = re.findall(pattern, html)
    for item in items:
        yield{
            '实时排名': item[0],
            '热搜': item[1]
        }


def write_to_file(content):
    with open('微博热搜榜.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False)+'\n')


def main():
    url = 'https://s.weibo.com/top/summary?Refer=top_hot&topnav=1&wvr=6'
    html = get_page(url)
    for item in parse_page(html):
        print(item)
        write_to_file((item))


if __name__ == '__main__':
    print('这是今天的微博热搜榜：')
    main()

os.system('pause')
