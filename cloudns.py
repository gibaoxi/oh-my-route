# main.py
import os
import requests
from notify import qmsg  # 导入 Telegram 通知函数

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
            qmsg(f"cloudns登陆成功:{data}")
        else:
            print("登录失败：", data['statusDescription'])
            # 调用 Telegram 通知函数
            qmsg(f"ClouDNS 登录失败：{data['statusDescription']}")
    else:
        print("请求失败，状态码：", response.status_code)
        # 调用 Telegram 通知函数
        qmsg(f"ClouDNS 请求失败，状态码：{response.status_code}")
# Cloudflare API 凭证
def login_to_desec():
    """
    登录 deSEC 并返回响应

    :return: requests.Response 对象，登录请求的响应
    """
    # 从环境变量中获取邮箱和密码
    email = os.getenv('EMAIL')
    password = os.getenv('DESEC')

    # 检查是否成功获取环境变量
    if not email or not password:
        raise ValueError("请确保环境变量 EMAIL 和 DESEC 已正确设置")

    # deSEC API 登录端点
    url = "https://desec.io/api/v1/auth/login/"

    # 请求头
    headers = {
        "Content-Type": "application/json"
    }

    # 请求体
    payload = {
        "email": email,  # 使用环境变量中的邮箱
        "password": password  # 使用环境变量中的密码
    }

    # 发送 POST 请求
    response = requests.post(url, json=payload, headers=headers)
    
# 检查响应状态码
    if response.status_code == 200:
        data = response.json()
        if data.get('owner') == email:  # 检查 owner 字段的值是否与邮箱一致
            qmsg(f"deSEC 登录成功！邮箱: {data['owner']}")
        else:
            qmsg(f"deSEC 登录失败：owner 字段不匹配，响应结果: {data}")
    else:
        qmsg(f"deSEC 请求失败，状态码: {response.status_code}, 响应内容: {response.text}")


def login_to_cloudflare():
    """
    登录 Cloudflare 并验证 API 凭证
    """
    # API 路径
    CLOUDFLARE_API_TOKEN = os.getenv('CLOUDFLARE_API_TOKEN')  # 从环境变量获取 API Ke     # 从环境变量获取邮箱

# Cloudflare API 基础 URL
    BASE_URL = 'https://api.cloudflare.com/client/v4'
    endpoint = '/user/tokens/verify'

    # 请求头
    headers = {
        'Authorization': f'Bearer {CLOUDFLARE_API_TOKEN}',
        'Content-Type': 'application/json'
    }

    # 发送请求
    response = requests.get(f'{BASE_URL}{endpoint}', headers=headers)

    # 检查响应状态
    if response.status_code == 200:
        data = response.json()
        if data['success']:
            print("Cloudflare 登录成功！")
            print("账户信息：", data)
            # 调用 Telegram 通知函数
            qmsg(
                f"Cloudflare 登录成功！账户信息： {data}")
        else:
            print("Cloudflare 登录失败：", data['errors'])
            # 调用 Telegram 通知函数
            qmsg(f"Cloudflare 登录失败：{data['errors']}")
    else:
        print("请求失败，状态码：", response.status_code)
        # 调用 Telegram 通知函数
        qmsg(f"Cloudflare 请求失败，状态码：{response.status_code}")

if __name__ == '__main__':
    # 调用 Cloudflare 登录函数
    login_to_cloudflare()
    # 调用 ClouDNS 登录函数
    login_to_cloudns()
    login_to_desec()
