import requests
import os
import re
from pyquery import PyQuery as pq
from requests.exceptions import RequestException
headers ={
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
}

def get_html(url):
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        print('请求页面出错', url)
        return None

def get_image_url(html):
    doc = pq(html)
    #这个items方法害了我半天,这样才可以迭代
    image_urls = doc('.multi-photo-image').items()
    for url in image_urls:
        download_image(url.attr("src"),url.attr("id"))

def download_image(url,imageId):
    print('当前正在下载图片',url)
    try:
        response = requests.get(url,headers=headers)
        if response.status_code == 200:
            save_image(response.content,imageId)
        return None
    except RequestException:
        print('请求图片出错',url)
        return None

def save_image(content,imageId):
    file_path = save_dic+"/"+imageId+".jpg"
    if not os.path.exists(file_path):
        with open(file_path,"wb") as f:
            f.write(content)
            f.close()


def main():
    gallery_url = "https://tuchong.com/959614/14912544/"
    global save_dic
    save_dic = re.sub('\D','',gallery_url)
    if not os.path.exists(save_dic):
        os.mkdir(save_dic)
    html = get_html(gallery_url)
    get_image_url(html)

if __name__ == "__main__":
    main()

