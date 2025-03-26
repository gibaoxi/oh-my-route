# coding=utf-8
import os
import requests
from bs4 import BeautifulSoup
import base64
from secret import *

def fetch_and_save(url):
    # 从环境变量获取URL
    url = url
    try:
        # 获取网页内容
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        
        # 解析HTML
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # 先写入临时文件
        temp_file = 'gg_temp.txt'
        with open(temp_file, 'w', encoding='utf-8') as f:
            for p in soup.find_all('p'):
                text = p.get_text().strip()
                if text:  # 跳过空行
                    f.write(text + '\n')

        
        # 读取临时文件内容并进行Base64编码
        with open(temp_file, 'r', encoding='utf-8') as f:
            original_content = f.read()
# 对整个文件内容进行Base64编码
        encoded_content = base64.b64encode(original_content.encode('utf-8')).decode('utf-8')
        print(encode_content)
        
        # 写入最终文件

if __name__ == '__main__':
    if url:
        print(url)
        fetch_and_save(url)