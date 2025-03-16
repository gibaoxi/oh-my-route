# main.py
import os
import requests
from notify import telegram  # 导入 Telegram 通知函数

# ClouDNS API 凭证
API_ID = os.getenv('CLOUDNS_API_ID')           # 从环境变量获取 API ID
API_PASSWORD = os.getenv('CLOUDNS_API_PASSWORD')  # 从环境变量获取 API 密码

# ClouDNS API 基础 URL
BASE_URL = 'https://api.cloudns.net'

def login_to_cloudns():
    """
    登录 ClouDNS 并获取账户信息
    """
    # API 路径
    endpoint = '/login/login.json'

    # 请求参数
    params = {
        'auth-id': API_ID,
        'auth-password': API_PASSWORD
    }

    # 发送请求
    response = requests.get(f'{BASE_URL}{endpoint}', params=params)

    # 检查响应状态
    if response.status_code == 200:
        data = response.json()
        if data['status'] == 'Success':
            print("登录成功！")
            telegram("登陆成功：", data)
        else:
            print("登录失败：", data['statusDescription'])
            # 调用 Telegram 通知函数
            telegram(f"ClouDNS 登录失败：{data['statusDescription']}")
    else:
        print("请求失败，状态码：", response.status_code)
        # 调用 Telegram 通知函数
        telegram(f"ClouDNS 请求失败，状态码：{response.status_code}")

if __name__ == '__main__':
    # 调用 ClouDNS 登录函数
    login_to_cloudns()
