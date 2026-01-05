import requests
import json
import os
import time

class Socks5ProxyCollectorWithNotify:
    def __init__(self):
        self.socks5_url = "https://mtpro.xyz/socks5"
        # GitHub Actions工作目录
        self.save_dir = "./tesk"
        self.filename = "telsocks.txt"
        self.proxies_by_country = {}
        self.old_proxies_by_country = {}
        
        self.telegram_bot_token = None
        self.telegram_chat_id = None
        
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
    
    def load_telegram_config(self):
        """从环境变量加载Telegram配置"""
        try:
            print("📋📋 正在从环境变量加载Telegram配置...")
            
            # 从环境变量获取TOKEN和ID
            self.telegram_bot_token = os.environ.get('TOKEN')
            self.telegram_chat_id = os.environ.get('ID')
            
            if not self.telegram_bot_token or not self.telegram_chat_id:
                print("❌❌ 环境变量TOKEN或ID未设置")
                return False
            
            print(f"✅ Bot Token: {self.telegram_bot_token[:10]}...")
            print(f"✅ Chat ID: {self.telegram_chat_id}")
            return True
            
        except Exception as e:
            print(f"❌❌ 加载配置失败: {e}")
            return False
    
    def send_telegram_message(self, message: str):
        """发送Telegram消息 - 支持HTML超链接"""
        if not self.telegram_bot_token or not self.telegram_chat_id:
            print("❌❌ Telegram配置缺失")
            return False
        
        try:
            url = f"https://api.telegram.org/bot{self.telegram_bot_token}/sendMessage"
            data = {
                'chat_id': self.telegram_chat_id,
                'text': message,
                'parse_mode': 'HTML',
                'disable_web_page_preview': True
            }
            
            print("📤📤 发送Telegram消息...")
            response = requests.post(url, data=data, timeout=30)
            
            if response.status_code == 200:
                print("✅ Telegram消息发送成功")
                return True
            else:
                print(f"❌❌ 发送失败: {response.status_code}")
                return False
                
        except Exception as e:
            print(f"❌❌ 发送消息失败: {e}")
            return False
    
    def load_old_proxies(self):
        """加载旧的代理数据"""
        filepath = os.path.join(self.save_dir, self.filename)
        if os.path.exists(filepath):
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    self.old_proxies_by_country = json.load(f)
                print(f"✅ 加载旧数据: {len(self.old_proxies_by_country)} 个国家")
                return True
            except Exception as e:
                print(f"❌❌ 加载旧数据失败: {e}")
        else:
            print("ℹℹ️ 首次运行，无历史数据")
        return False
    
    def fetch_proxies(self):
        """获取代理数据"""
        try:
            api_url = "https://mtpro.xyz/api?type=socks"
            print(f"🌐🌐 获取代理数据: {api_url}")
            
            response = self.session.get(api_url, timeout=15)
            response.raise_for_status()
            
            data = response.json()
            print(f"✅ 获取到 {len(data)} 个代理")
            return data
            
        except Exception as e:
            print(f"❌❌ 获取代理失败: {e}")
            return []
    
    def classify_proxies(self, proxies):
        """分类代理，保留完整的代理信息"""
        for proxy in proxies:
            country = proxy.get("country", "UNKNOWN")
            ip = proxy.get("ip", "")
            port = proxy.get("port", "")
            ping = proxy.get("ping", 9999)  # 获取ping值，默认9999
            
            if ip and port:
                proxy_info = {
                    "ip_port": f"{ip}:{port}",
                    "ping": ping,
                    "ip": ip,
                    "port": port
                }
                
                if country not in self.proxies_by_country:
                    self.proxies_by_country[country] = []
                
                # 检查是否已存在相同的代理
                existing = False
                for existing_proxy in self.proxies_by_country[country]:
                    if existing_proxy["ip_port"] == proxy_info["ip_port"]:
                        existing = True
                        break
                
                if not existing:
                    self.proxies_by_country[country].append(proxy_info)
    
    def find_new_proxies(self):
        """找出新增代理（新的有而旧文件没有的）"""
        new_proxies_by_country = {}
        
        for country, current_proxies in self.proxies_by_country.items():
            # 从旧数据中提取ip_port列表
            old_ip_ports = []
            if country in self.old_proxies_by_country:
                # 处理旧数据格式（可能是字符串列表或字典列表）
                for old_proxy in self.old_proxies_by_country[country]:
                    if isinstance(old_proxy, dict):
                        old_ip_ports.append(old_proxy.get("ip_port", ""))
                    else:
                        old_ip_ports.append(old_proxy)
            
            # 找出新的代理
            new_proxies = []
            for proxy in current_proxies:
                if proxy["ip_port"] not in old_ip_ports:
                    new_proxies.append(proxy)
            
            if new_proxies:
                # 按ping值排序（从低到高）
                new_proxies.sort(key=lambda x: x["ping"])
                new_proxies_by_country[country] = new_proxies
        
        return new_proxies_by_country
    
    def create_telegram_proxy_link(self, ip: str, port: str) -> str:
        """创建Telegram代理链接"""
        return f"tg://socks?server={ip}&port={port}"
    
    def format_simple_message(self, new_proxies_by_country):
        """简化版消息 - 显示代理信息和ping值"""
        message = ""
        
        for country, proxies in new_proxies_by_country.items():
            message += f"{country} (+{len(proxies)}个):\n"
            
            for i, proxy in enumerate(proxies, 1):
                telegram_link = self.create_telegram_proxy_link(proxy["ip"], proxy["port"])
                ping = proxy["ping"]
                
                # 根据ping值显示不同的状态
                if ping < 200:
                    ping_display = f"🟢🟢🟢 {ping}ms"
                elif ping < 500:
                    ping_display = f"🟡🟡🟡 {ping}ms"
                else:
                    ping_display = f"🔴🔴 {ping}ms"
                
                if telegram_link:
                    message += f'  {i}. <a href="{telegram_link}">{proxy["ip_port"]}</a> {ping_display}\n'
                else:
                    message += f'  {i}. {proxy["ip_port"]} {ping_display}\n'
            
            message += "\n"
        
        return message.strip()
    
    def save_to_file(self):
        """保存代理数据到文件"""
        filepath = os.path.join(self.save_dir, self.filename)
        
        try:
            # 确保目录存在
            os.makedirs(self.save_dir, exist_ok=True)
            
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(self.proxies_by_country, f, indent=2, ensure_ascii=False)
            print(f"💾💾 代理数据已保存到: {filepath}")
            
            # 检查文件是否成功写入
            if os.path.exists(filepath):
                file_size = os.path.getsize(filepath)
                print(f"📁📁 文件大小: {file_size} 字节")
                return True
            else:
                print("❌❌ 文件保存失败")
                return False
                
        except Exception as e:
            print(f"❌❌ 保存文件失败: {e}")
            return False
    
    def run(self):
        """主程序"""
        print("=" * 60)
        print("SOCKS5代理监控 - 带Ping值排序版")
        print("=" * 60)
        
        os.makedirs(self.save_dir, exist_ok=True)
        print(f"📁📁 工作目录: {self.save_dir}")
        
        # 1. 加载Telegram配置（从环境变量）
        telegram_ready = self.load_telegram_config()
        
        # 2. 加载旧数据
        has_old_data = self.load_old_proxies()
        
        # 3. 获取新数据
        proxies = self.fetch_proxies()
        if not proxies:
            if telegram_ready:
                self.send_telegram_message("❌❌ 无法获取SOCKS5代理数据")
            return
        
        # 4. 分类代理
        self.classify_proxies(proxies)
        
        # 5. 检测新增代理
        if has_old_data:
            new_proxies = self.find_new_proxies()
            
            if new_proxies:
                total_new = sum(len(p) for p in new_proxies.values())
                print(f"🎯🎯 发现 {total_new} 个新增代理，涉及 {len(new_proxies)} 个国家")
                
                if telegram_ready:
                    # 使用简化版消息
                    message = self.format_simple_message(new_proxies)
                    self.send_telegram_message(message)
                else:
                    print("ℹℹ️ Telegram未配置，跳过通知")
            else:
                print("ℹℹ️ 没有发现新增代理")
        else:
            # 首次运行
            print("🚀🚀 首次运行，初始化代理数据")
            if telegram_ready:
                # 首次运行也发个简单的通知
                total_countries = len(self.proxies_by_country)
                total_proxies = sum(len(proxies) for proxies in self.proxies_by_country.values())
                message = f"🚀🚀 SOCKS5监控启动\n监控 {total_countries} 个国家，共 {total_proxies} 个代理"
                self.send_telegram_message(message)
        
        # 6. 保存数据
        self.save_to_file()
        
        # 7. 显示统计
        print("\n" + "=" * 40)
        total_countries = len(self.proxies_by_country)
        total_proxies = sum(len(proxies) for proxies in self.proxies_by_country.values())
        print(f"🌍🌍 国家数: {total_countries}")
        print(f"📊📊 总代理数: {total_proxies}")

if __name__ == "__main__":
    collector = Socks5ProxyCollectorWithNotify()
    collector.run()
