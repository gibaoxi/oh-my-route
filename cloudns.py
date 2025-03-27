import os
import requests
from notify import qmsg  # 导入 Telegram 通知函数

class Login:
    def __init__(self):
        """
        初始化 DNS 服务认证测试类
        """
        # 从环境变量加载所有需要的凭证
        self.credentials = {
            'cloudns': {
                'api_id': os.getenv('CLOUDNS_API_ID'),
                'api_password': os.getenv('CLOUDNS_API_PASSWORD')
            },
            'cloudflare': {
                'api_token': os.getenv('CLOUDFLARE_API_TOKEN')
            },
            'desec': {
                'email': os.getenv('EMAIL'),
                'password': os.getenv('DESEC')
            }
        }
    
    def _send_notification(self, service, success, message, data=None):
        """
        发送通知的辅助方法
        
        :param service: 服务名称
        :param success: 是否成功
        :param message: 消息内容
        :param data: 附加数据
        """
        status = "成功" if success else "失败"
        full_message = f"{service} 登录{status}: {message}"
        if data:
            full_message += f"\n详细信息: {data}"
        qmsg(full_message)
        print(full_message)
    
    def test_cloudns(self):
        """
        测试 ClouDNS API 登录
        """
        endpoint = '/login/login.json'
        params = {
            'auth-id': self.credentials['cloudns']['api_id'],
            'auth-password': self.credentials['cloudns']['api_password']
        }
        
        try:
            response = requests.get(f'https://api.cloudns.net{endpoint}', params=params)
            if response.status_code == 200:
                data = response.json()
                if data['status'] == 'Success':
                    self._send_notification("ClouDNS", True, "认证成功", data)
                    return True
                else:
                    self._send_notification("ClouDNS", False, data['statusDescription'])
                    return False
            else:
                self._send_notification("ClouDNS", False, f"HTTP状态码: {response.status_code}")
                return False
        except Exception as e:
            self._send_notification("ClouDNS", False, f"请求异常: {str(e)}")
            return False
    
    def test_cloudflare(self):
        """
        测试 Cloudflare API 登录
        """
        endpoint = '/user/tokens/verify'
        headers = {
            'Authorization': f'Bearer {self.credentials["cloudflare"]["api_token"]}',
            'Content-Type': 'application/json'
        }
        
        try:
            response = requests.get(f'https://api.cloudflare.com/client/v4{endpoint}', headers=headers)
            if response.status_code == 200:
                data = response.json()
                if data['success']:
                    self._send_notification("Cloudflare", True, "认证成功", data)
                    return True
                else:
                    self._send_notification("Cloudflare", False, data['errors'])
                    return False
            else:
                self._send_notification("Cloudflare", False, f"HTTP状态码: {response.status_code}")
                return False
        except Exception as e:
            self._send_notification("Cloudflare", False, f"请求异常: {str(e)}")
            return False
    
    def test_desec(self):
        """
        测试 deSEC API 登录
        """
        url = "https://desec.io/api/v1/auth/login/"
        headers = {"Content-Type": "application/json"}
        payload = {
            "email": self.credentials['desec']['email'],
            "password": self.credentials['desec']['password']
        }
        
        try:
            response = requests.post(url, json=payload, headers=headers)
            if response.status_code == 200:
                data = response.json()
                if data.get('owner') == self.credentials['desec']['email']:
                    self._send_notification("deSEC", True, f"认证成功 - 邮箱: {data['owner']}")
                    return True
                else:
                    self._send_notification("deSEC", False, f"owner字段不匹配 - 响应: {data}")
                    return False
            else:
                self._send_notification("deSEC", False, 
                                       f"HTTP状态码: {response.status_code}, 响应: {response.text}")
                return False
        except Exception as e:
            self._send_notification("deSEC", False, f"请求异常: {str(e)}")
            return False
    
    def alllogin(self):
        """
        测试所有 DNS 服务的认证
        """
        results = {
            'cloudns': self.test_cloudns(),
            'cloudflare': self.test_cloudflare(),
            'desec': self.test_desec()
        }
        return results


if __name__ == '__main__':
    tester = Login()
    tester.alllogin()