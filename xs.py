# coding=utf-8
import os
import requests
from bs4 import BeautifulSoup
from datetime import datetime
from notify import telegram
import base64
now = datetime.today()
now = now.strftime('%Y-%m-%d')
qbt, tr, trx, jpx, bx, trs =[], [], [], [], [], []
url, url1, url2, url4, url3, url5 = 'https://qbtr.me/tongren/', 'https://tongrenquan.org/tongren/', 'https://trxs.cc/tongren/', 'https://jpxs123.cc/', 'https://bixiange.top/','https://www.tongrenshe.cc/'

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




if __name__ == '__main__':
    urls_to_lists = {  
    url: qbt,  
    url1: tr,  
    url2: trx, 
    url4: jpx,
    url3: bx,
    url5: trs # 假设 url3 也对应 trx 列表  
}  
    qbtr(urls_to_lists)
    TITLE = "同人小说"
    CONTENT = f'全本同人{qbt}\n同人圈{tr}\n同人小说{trx}\n精品小说{jpx}\n笔仙阁{bx}\n同人社{trs}'
    with open('novel.txt', 'w',encoding='utf-8') as file:
        file.write(CONTENT)

#pushplus(TITLE, CONTENT)
#server(TITLE, CONTENT)
    telegram(CONTENT)
