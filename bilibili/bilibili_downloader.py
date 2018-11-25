import requests
import re
import json
from contextlib import closing
from pyquery import PyQuery as pq
from requests import RequestException
class bilibili():
    def __init__(self):
        self.getHtmlHeaders={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q = 0.9'
        }

        self.downloadVideoHeaders={
            'Origin': 'https://www.bilibili.com',
            'Referer': 'https://www.bilibili.com/video/av26522634',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
        }

    #一般这里得到的网页源码和F12查看看到的不一样，因为F12开发者工具里的源码经过了浏览器的解释
    def getHtml(self,url):
        try:
            response = requests.get(url=url, headers= self.getHtmlHeaders)
            print(response.status_code)
            if response.status_code == 200:
                return response.text
        except RequestException:
            print('请求Html错误:')

    def parseHtml(self,html):
        #用pq解析得到视频标题
        doc = pq(html)
        video_title = doc('#viewbox_report > h1 > span').text()

        #用正则、json得到视频url;用pq失败后的无奈之举
        pattern = r'\<script\>window\.__playinfo__=(.*?)\</script\>'
        result = re.findall(pattern, html)[0]
        temp = json.loads(result)
        #temp['durl']是一个列表，里面有很多字典
        #video_url = temp['durl']
        for item in temp['durl']:
            if 'url' in item.keys():
                video_url = item['url']
        #print(video_url)
        return{
            'title': video_title,
            'url': video_url
        }

    def download_video(self,video):
        title = re.sub(r'[\/:*?"<>|]', '-', video['title'])  # 去掉创建文件时的非法字符
        url = video['url']
        filename = title +'.flv'
        with open(filename, "wb") as f:
            f.write(requests.get(url=url, headers=self.downloadVideoHeaders, stream=True, verify=False).content)

        #closing适用于提供了 close() 实现的对象，比如网络连接、数据库连接
        # with closing(requests.get(video['url'], headers=self.downloadVideoHeaders, stream=True, verify=False)) as res:
        #     if res.status_code == 200:
        #         with open(filename, "wb") as f:
        #             for chunk in res.iter_content(chunk_size=1024):
        #                 if chunk:
        #                     f.write(chunk)

    def run(self,url):
        self.download_video(self.parseHtml(self.getHtml(url)))

if __name__ == '__main__':
    url = 'https://www.bilibili.com/video/av18100312'
    bilibili().run(url)

