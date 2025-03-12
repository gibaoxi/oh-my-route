import requests
from bs4 import BeautifulSoup
import re
import os  # 引入 os 模块读取环境变量

# 从环境变量中读取 Qmsg 的 Key
QMSG_KEY = os.getenv('QMSG_KEY')  # 从环境变量中读取
QMSG_API = f'https://qmsg.zendee.cn/send/{QMSG_KEY}'

# 目标网址
URL = 'https://www.serv00.com'

def get_user_count():
    # 发送请求获取网页内容
    response = requests.get(URL)
    if response.status_code != 200:
        print("无法访问网站")
        return None, None

    # 解析网页内容
    soup = BeautifulSoup(response.text, 'html.parser')

    # 找到包含用户数量的标签
    user_count_tag = soup.find('span', class_='button is-large is-flexible')
    if not user_count_tag:
        print("未找到用户数量信息")
        return None, None

    # 提取文本内容
    user_count_text = user_count_tag.get_text(strip=True)

    # 使用正则表达式提取数字部分
    # 匹配格式为 "数字 / 数字"
    match = re.search(r'(\d+)\s*/\s*(\d+)', user_count_text)
    if not match:
        print("未找到用户数量信息")
        return None, None

    current_users = int(match.group(1))
    total_users = int(match.group(2))

    return current_users, total_users

def send_qmsg(message):
    # 发送消息到 QQ
    data = {'msg': message}
    response = requests.post(QMSG_API, data=data)
    if response.status_code == 200:
        print("消息发送成功")
    else:
        print("消息发送失败")

def main():
    # 获取用户数量
    current_users, total_users = get_user_count()
    if current_users is None or total_users is None:
        return

    if current_users == total_users:
        result = "无"
    else:
        result = "有"

    # 发送结果到 QQ
    message = f"{current_users}/{total_users},{result}"
    send_qmsg(message)

if __name__ == '__main__':
    main()
