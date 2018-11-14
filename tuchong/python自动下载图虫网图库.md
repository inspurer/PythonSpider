---
title: python自动下载图虫网图库
copyright: true
date: 2018-11-14 20:58:11
tags: [python, 爬虫]
categories: python
top: 90
---
# 如何使用  
## 下载工程源码
[点击下载](https://github.com/inspurer/PythonSpider/tree/master/tuchong)    
<!-- more -->
或者git bash;`git clone git@github.com:inspurer/PythonSpider.git`    

## 下载相关依赖   
在命令行下依此输入   
	
	pip install requests   
	pip install pyquery   

## 打开图虫网     
选择你喜欢的图库链接,比如`https://tuchong.com/4293835/23849565/`    
复制并替换到tuchong_gallery.py代码里面的gallery_url,解释一下这个链接的作用,    
前一个数字串是作者的id,后一个数字串是作者该图库的id   
注意,在打开这个图库时,复制地址前最好不要左右浏览   

## 运行tuchong_gallery.py   
你就可以看到在下载这个图库的图片了   
图库保存在工程目录下,文件夹名为作者和图库的id   
每一张图片保存在该文件夹下,格式为:`imageid.jpg`  

# 计划更新  
## 增加自动搜索   
