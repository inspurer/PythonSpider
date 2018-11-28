from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

from config import *

import time
broswer = webdriver.Chrome()
wait = WebDriverWait(broswer, 10)

def search():
    try:
        broswer.get("http://csujwc.its.csu.edu.cn/jsxsd/kscj/yscjcx_list")
        account = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#userAccount"))
        )
        password = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#userPassword"))
        )

        submit = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#btnSubmit"))
        )
    except TimeoutException:
        return search()

    #登录
    account.send_keys(ACCOUNT)
    password.send_keys(PASSWORD)
    submit.click()

   #进入我的成绩界面
    my_score = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR,"body > div.wap > a:nth-child(3) > div"))
    )
    my_score.click()


#成绩和平均分
    # my_rank = wait.until(
    #     EC.presence_of_element_located((By.CSS_SELECTOR, "#LeftMenu1_divChildMenu > ul > li:nth-child(4) > a"))
    # )
    # my_rank.click()
    #
    # rank = wait.until(
    #     EC.presence_of_element_located((By.CSS_SELECTOR, "#dataList > tbody > tr:nth-child(2) > td:nth-child(3)"))
    # )
    # #http://www.w3school.com.cn/cssref/selector_nth-child.asp nth-child(n)的用法
    # average_score = wait.until(
    #     EC.presence_of_element_located((By.CSS_SELECTOR, "#dataList > tbody > tr:nth-child(2) > td:nth-child(4)"))
    # )
    #
    # print('您的平均成绩是:'+average_score.text+"\n排名:"+rank.text)


#逐次展示 我的成绩八个子项
    # css_selector = "#LeftMenu1_divChildMenu > ul > li:nth-child({0}) > a"
    # for i in range(8):
    #     # 将滚动条移动到页面的顶部
    #     js = "var q=document.documentElement.scrollTop=0"
    #     broswer.execute_script(js)
    #     time.sleep(2)
    #
    #     aviable_score = wait.until(
    #         EC.presence_of_element_located((By.CSS_SELECTOR, css_selector.format(str(i+1))))
    #     )
    #     aviable_score.click()
    #
    #
    #     #将滚动条移动到页面的底部
    #     for j in range(8):
    #         js="var q=document.documentElement.scrollTop="+str(j*200)
    #         broswer.execute_script(js)
    #         time.sleep(1)


    #处理select https://www.cnblogs.com/imyalost/p/7846653.html
    yxcj = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#LeftMenu1_divChildMenu > ul > li:nth-child(1) > a"))
    )
    select_score_element = broswer.find_element_by_css_selector("#xnxq01id")
    select_score = Select(select_score_element)

    #得到下拉列表的所有子项
    select_score_items = broswer.find_elements_by_css_selector("#xnxq01id option")
    select_score_items_text = []
    for item in select_score_items:
        select_score_items_text.append(item.text)
        #print(item.text)

    scores_dic = {}
    for i in range(len(select_score.options)):
        #不加这两行会报错，原因： https://blog.csdn.net/ulebo/article/details/52128033
        print("*****************************************************"+select_score_items_text[i]+
              "*****************************************************")
        select_score_element = broswer.find_element_by_css_selector("#xnxq01id")
        select_score = Select(select_score_element)
        select_score.select_by_index(i)
        time.sleep(1)
        score_table = broswer.find_element_by_css_selector("#dataList")
        data = score_table.text.replace("+","")
        data = data.split("\n")
        datalist = []
        for line in data:
            datalist.append(line.split())
        scores_dic[select_score_items_text[i]] = datalist

    return scores_dic[select_score_items_text[0]]





def main():
    search()

if __name__ =="__main__":
    main()