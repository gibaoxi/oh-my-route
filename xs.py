# coding=utf-8
import os
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import base64
now = datetime.today()
now = now.strftime('%Y-%m-%d')
qbt, tr, trx, jpx, bx =[], [], [], [], []
url, url1, url2, url4, url3 = 'https://qbtr.me/tongren/', 'https://tongrenquan.org/tongren/', 'https://trxs.cc/tongren/', 'https://jpxs123.cc/', 'https://bixiange.top/'

def qbtr(urls_to_lists):  
    now = datetime.now().date()  
    for url, lb in urls_to_lists.items():  
        res = requests.get(url)  
        res.encoding = 'gb2312'  
        html = res.text  
        soup = BeautifulSoup(html, 'html.parser')  
        qbtr3 = soup.find_all('div', class_='infos')  
        for re in qbtr3:  
            r = re.find('label', class_='date')  
            if r is not None:  
                date = r.text  
                if date == str(now):  
                    p = re.find('h3')  
                    if p is not None:  
                        lb.append(p.text)  
   
  
# 创建 URL 到列表的映射  
urls_to_lists = {  
    url: qbt,  
    url1: tr,  
    url2: trx, 
    url4: jpx,
    url3: bx # 假设 url3 也对应 trx 列表  
}  
  
# 调用函数  
qbtr(urls_to_lists)  
  
# 此时，tr 列表应该包含 url1 对应的数据（如果日期匹配的话）  
# trx 列表应该包含 url2 和 url3 对应的数据（如果日期匹配的话）


def server(title, content):
    access_token = "SCT242760TeNxiWHrdLtFYqmJkeQnqE2Xq"
    urls = "https://sctapi.ftqq.com/" + access_token + ".send"
    data = {
        "text": content,
        "desp": content,  # 有些Server酱版本可能需要这个字段
    }
    if title:
        data["title"] = title

    headers = {
        "Content-Type": "application/x-www-form-urlencoded;charset=utf-8"
    }


    try:
        response = requests.post(urls, data=data, headers=headers)
        if response.status_code == 200:
            print("server推送成功")
        else:
            print("s消息推送失败")
    except requests.exceptions.RequestException as e:
        print("s消息推送出错:", e)

def pushplus(title, content):
    api_token = 'c204e4622c9f4e3e8bf06591c7f6e89d'

    # PushPlus请求URL
    urlp = 'http://www.pushplus.plus/send'

    # 发送POST请求
    data = {
        "token": api_token,
        "title": title,
        "content": content
    }

    try:
        response = requests.post(urlp, json=data)
        if response.status_code == 200:
            print("pushplus推送成功")
        else:
            print("p消息推送失败")
    except requests.exceptions.RequestException as e:
        print("s消息推送出错:", e)
def tel(title, content):
    chatid = 6776513150
    key = os.environ('TELG')
    if not key :
        print ('请输入telegram')
    
        
    # PushPlus请求URL
    urlp = "https://api.telegram.org/bot" + key + "/sendMessage"
    headers1 = {
        "Content-Type": "application/json"
    }
    # 发送POST请求
    data = {
  "text": content,
  "chat_id": chatid
}

    try:
        response = requests.post(urlp, json=data,headers=headers1)
        print(response.text)
        if response.status_code == 200:
            print("tele推送成功")
            print(response.text)
        else:
            print("p消息推送失败")
    except requests.exceptions.RequestException as e:
        print("s消息推送出错:", e)
        



TITLE = "同人小说"
CONTENT = f'全本同人{qbt}\n同人圈{tr}\n同人小说{trx}\n精品小说{jpx}\n笔仙阁{bx}'
#pushplus(TITLE, CONTENT)
#server(TITLE, CONTENT)
tel(TITLE, CONTENT)
