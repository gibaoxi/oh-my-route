import requests
from bs4 import BeautifulSoup
import re
import os
import datetime
import json

# 从环境变量中读取 Qmsg 的 Key
QMSG_KEY = os.getenv('QMSG_KEY')
QMSG_API = f'https://qmsg.zendee.cn/send/{QMSG_KEY}'

def check_serv00():
    """检查Serv00用户数量"""
    URL = 'https://www.serv00.com'
    
    # 发送请求获取网页内容
    response = requests.get(URL)
    if response.status_code != 200:
        print("无法访问Serv00网站")
        return None

    # 解析网页内容
    soup = BeautifulSoup(response.text, 'html.parser')

    # 找到包含用户数量的标签
    user_count_tag = soup.find('span', class_='button is-large is-flexible')
    if not user_count_tag:
        print("未找到用户数量信息")
        return None

    # 提取文本内容
    user_count_text = user_count_tag.get_text(strip=True)

    # 使用正则表达式提取数字部分
    match = re.search(r'(\d+)\s*/\s*(\d+)', user_count_text)
    if not match:
        print("未找到用户数量信息")
        return None

    current_users = int(match.group(1))
    total_users = int(match.group(2))

    # 检查是否有空位
    if current_users < total_users:
        message = f"Serv00有空位！当前：{current_users}/{total_users}"
        send_qmsg(message)
        return True
    else:
        print("Serv00无空位")
        return False

def check_github_update():
    """检查GitHub是否有更新"""
    GITHUB_URL = "https://github.com/go4sharing/sub/commits/main/"
    
    # 抓取页面
    response = requests.get(GITHUB_URL)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # 提取日期
    script_tag = soup.find('script', {'data-target': 'react-app.embeddedData'})
    data = json.loads(script_tag.string)
    first_date = data['payload']['commitGroups'][0]['title']
    
    # 比较日期
    captured_date = datetime.datetime.strptime(first_date, "%b %d, %Y").date()
    today = datetime.date.today()
    
    print(f"今天: {today}")
    print(f"GitHub最新提交: {captured_date}")
    
    # 日期相同就发送通知
    if captured_date == today:
        message = f"🚀 GitHub有新提交！\n日期: {first_date}"
        send_qmsg(message)
        return True
    else:
        print("GitHub没有新提交")
        return False

def send_qmsg(message):
    """发送消息到QQ"""
    data = {'msg': message}
    response = requests.post(QMSG_API, data=data)
    if response.status_code == 200:
        print("消息发送成功")
    else:
        print("消息发送失败")

def main():
    """主函数"""
    print("开始检查...")
    
    # 检查Serv00空位
    serv00_result = check_serv00()
    
    # 检查GitHub更新
    github_result = check_github_update()
    
    if not serv00_result and not github_result:
        print("没有需要发送的通知")

if __name__ == '__main__':
    main()