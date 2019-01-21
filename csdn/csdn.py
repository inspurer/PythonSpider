# -*- coding: utf-8 -*-
# author:           inspurer(月小水长)
# pc_type           lenovo
# create_date:      2019/1/21
# file_name:        csdn
# qq_mail           2391527690@qq.com

import requests
from pyquery import PyQuery as pq

# 当前的博客列表页号
page_num = 1

account = str(input('print csdn id:'))
#account = "ygdxt"
# 首页地址
baseUrl = 'http://blog.csdn.net/' + account
# 连接页号，组成爬取的页面网址
myUrl = baseUrl + '/article/list/' + str(page_num)

headers = {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'}
# 构造请求

# 访问页面
myPage = requests.get(myUrl,headers=headers).text

doc = pq(myPage)

data_info = doc("aside .data-info dl").items()
for i,item in enumerate(data_info):
    if i==0:
        print("原创:"+item.attr("title"))
    if i==1:
        print("粉丝:"+item.attr("title"))
    if i==2:
        print("喜欢:"+item.attr("title"))
    if i==3:
        print("评论:"+item.attr("title"))

grade_box = doc(".grade-box dl").items()
for i,item in enumerate(grade_box):
    if i==0:
        childitem = item("dd > a")
        print("等级:"+childitem.attr("title")[0:2])
    if i==1:
        childitem = item("dd")
        print("访问:"+childitem.attr("title"))
    if i==2:
        childitem = item("dd")
        print("积分:"+childitem.attr("title"))
    if i==3:
        print("排名:"+item.attr("title"))


# 获取每一页的信息
while True:

    # 首页地址
    baseUrl = 'http://blog.csdn.net/' + account
    # 连接页号，组成爬取的页面网址
    myUrl = baseUrl + '/article/list/' + str(page_num)
    # 构造请求
    myPage = requests.get(myUrl,headers=headers).text
    if len(myPage) < 30000:
        break

    print('-----------------------------第 %d 页---------------------------------' % (page_num,))

    doc = pq(myPage)
    articles = doc(".article-list > div").items()
    articleList = []
    for i,item in enumerate(articles):
        if i == 0:
            continue
        title = item("h4 > a").text()[2:]
        date = item("p > .date").text()
        num_item = item("p > .read-num").items()
        ariticle = [date, title]
        for j,jitem in enumerate(num_item):
            if j == 0:
                read_num = jitem.text()
                ariticle.append(read_num)
            else:
                comment_num = jitem.text()
                ariticle.append(comment_num)
        articleList.append(ariticle)
    for item in articleList:
        if(len(item)==4):
            print("%s %s %s %s"%(item[0],item[1],item[2],item[3]))
    page_num = page_num + 1