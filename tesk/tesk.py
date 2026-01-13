import requests
import json
import os
import time
import socket
from datetime import datetime

class Socks5ProxyCollectorWithNotify:
    def __init__(self):
        self.socks5_url = "https://mtpro.xyz/socks5"
        self.save_dir = "./tesk"
        self.filename = "telsocks.json"
        self.target_countries = ["SG", "HK", "KR", "JP"]  # 只关注这四个国家
        
        # 测试配置
        self.test_url = "https://httpbin.org/ip"  # 链接1的测试地址
        
        # 存储当前获取的所有代理（不区分国家）
        self.all_current_proxies = []
        
        # 存储从文件读取的上一次数据
        self.previous_data = {"new": {}, "old": {}}
        
        self.telegram_bot_token = None
        self.telegram_chat_id = None
        
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
    
    def test_tcp_connection(self, ip: str, port: str, timeout: int = 5) -> bool:
        """测试TCP连接"""
        try:
            print(f"🔍 测试TCP连接: {ip}:{port}")
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(timeout)
            result = sock.connect_ex((ip, int(port)))
            sock.close()
            
            if result == 0:
                print(f"✅ TCP连接成功: {ip}:{port}")
                return True
            else:
                print(f"❌ TCP连接失败: {ip}:{port}")
                return False
        except Exception as e:
            print(f"❌ TCP连接异常: {ip}:{port}, 错误: {e}")
            return False
    
    def test_socks5_proxy(self, ip: str, port: str, timeout: int = 10) -> bool:
        """测试SOCKS5代理访问"""
        try:
            print(f"🔍 测试SOCKS5代理: {ip}:{port}")
            
            proxies = {
                'http': f'socks5://{ip}:{port}',
                'https': f'socks5://{ip}:{port}'
            }
            
            start_time = datetime.now()
            response = requests.get(
                self.test_url, 
                proxies=proxies, 
                timeout=timeout,
                verify=False  # 禁用 SSL 验证
            )
            end_time = datetime.now()
            
            response_time = (end_time - start_time).total_seconds()
            print(f"✅ 代理测试成功! 状态码: {response.status_code}")
            print(f"⏱️ 响应时间: {response_time:.2f}秒")
            print("-" * 50)
            
            return True
            
        except requests.exceptions.RequestException as e:
            print(f"❌ 代理测试失败: {e}")
            print("-" * 50)
            return False
        except Exception as e:
            print(f"❌ 代理测试异常: {e}")
            print("-" * 50)
            return False
    
    def test_proxy_comprehensive(self, proxy_info: dict) -> bool:
        """综合测试代理（TCP + SOCKS5），TCP失败直接跳过SOCKS5测试"""
        ip = proxy_info.get("ip", "")
        port = proxy_info.get("port", "")
        
        if not ip or not port:
            return False
        
        # 先测试TCP连接
        tcp_success = self.test_tcp_connection(ip, port)
        if not tcp_success:
            print(f"🚫 TCP连接失败，跳过SOCKS5代理测试: {ip}:{port}")
            return False
        
        # TCP连接成功，继续测试SOCKS5代理功能
        proxy_success = self.test_socks5_proxy(ip, port)
        return proxy_success
    
    def filter_tested_proxies(self, proxies_by_country: dict) -> dict:
        """过滤并测试代理，只返回测试通过的代理"""
        tested_proxies = {}
        
        for country, proxies in proxies_by_country.items():
            tested_proxies[country] = []
            
            print(f"🧪🧪🧪 开始测试 {country} 的代理 ({len(proxies)}个)")
            
            for proxy in proxies:
                print(f"\n🎯 测试代理: {proxy['ip_port']}")
                
                # 综合测试代理
                if self.test_proxy_comprehensive(proxy):
                    print(f"✅✅✅ 代理测试通过: {proxy['ip_port']}")
                    tested_proxies[country].append(proxy)
                else:
                    print(f"❌❌❌ 代理测试失败: {proxy['ip_port']}")
            
            print(f"📊 {country} 测试结果: {len(tested_proxies[country])}/{len(proxies)} 个通过")
        
        # 移除空的国家条目
        tested_proxies = {k: v for k, v in tested_proxies.items() if v}
        return tested_proxies

    def load_telegram_config(self):
        """从环境变量加载Telegram配置"""
        try:
            print("📋📋📋📋📋📋📋📋 正在从环境变量加载Telegram配置...")
            
            self.telegram_bot_token = '7687806689:AAGa_UX9k1uW6fnGo3lI_HHoIEw1HKDkiXc'        
            self.telegram_chat_id = '6776513150'
            
            if not self.telegram_bot_token or not self.telegram_chat_id:
                print("❌❌❌❌❌❌❌❌ 环境变量TOKEN或ID未设置")
                return False
            
            print(f"✅ Bot Token: {self.telegram_bot_token[:10]}...")
            print(f"✅ Chat ID: {self.telegram_chat_id}")
            return True
            
        except Exception as e:
            print(f"❌❌❌❌❌❌❌❌ 加载配置失败: {e}")
            return False
    
    def send_telegram_message(self, message: str):
        """发送Telegram消息"""
        if not self.telegram_bot_token or not self.telegram_chat_id:
            print("❌❌❌❌❌❌❌❌ Telegram配置缺失")
            return False
        
        try:
            url = f"https://api.telegram.org/bot{self.telegram_bot_token}/sendMessage"
            data = {
                'chat_id': self.telegram_chat_id,
                'text': message,
                'parse_mode': 'HTML',
                'disable_web_page_preview': True
            }
            
            print("📤📤📤📤📤📤📤📤 发送Telegram消息...")
            response = requests.post(url, data=data, timeout=30)
            
            if response.status_code == 200:
                print("✅ Telegram消息发送成功")
                return True
            else:
                print(f"❌❌❌❌❌❌❌❌ 发送失败: {response.status_code}")
                return False
                
        except Exception as e:
            print(f"❌❌❌❌❌❌❌❌ 发送消息失败: {e}")
            return False
    
    def load_previous_data(self):
        """加载上一次保存的数据"""
        filepath = os.path.join(self.save_dir, self.filename)
        if os.path.exists(filepath):
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    self.previous_data = json.load(f)
                
                print(f"✅ 加载上一次数据:")
                print(f"  - new键: {len(self.previous_data.get('new', {}))} 个国家")
                print(f"  - old键: {len(self.previous_data.get('old', {}))} 个国家")
                
                return True
            except Exception as e:
                print(f"❌❌❌❌❌❌❌❌ 加载上一次数据失败: {e}")
                self.previous_data = {"new": {}, "old": {}}
        else:
            print("ℹℹℹℹℹℹℹℹ️ 首次运行，无历史数据")
            self.previous_data = {"new": {}, "old": {}}
        return False
    
    def fetch_proxies(self):
        """获取代理数据"""
        try:
            api_url = "https://mtpro.xyz/api?type=socks"
            print(f"🌐🌐🌐🌐🌐🌐🌐🌐 获取代理数据: {api_url}")
            
            response = self.session.get(api_url, timeout=15)
            response.raise_for_status()
            
            data = response.json()
            print(f"✅ 获取到 {len(data)} 个代理")
            return data
            
        except Exception as e:
            print(f"❌❌❌❌❌❌❌❌ 获取代理失败: {e}")
            return []
    
    def process_proxies(self, proxies):
        """处理代理数据，存储所有代理"""
        self.all_current_proxies = []
        
        for proxy in proxies:
            country = proxy.get("country", "UNKNOWN")
            ip = proxy.get("ip", "")
            port = proxy.get("port", "")
            ping = proxy.get("ping", 9999)
            
            if ip and port:
                proxy_info = {
                    "ip_port": f"{ip}:{port}",
                    "ping": ping,
                    "ip": ip,
                    "port": port,
                    "country": country
                }
                
                # 添加到所有代理列表
                self.all_current_proxies.append(proxy_info)
        
        # 按ping值排序
        self.all_current_proxies.sort(key=lambda x: x["ping"])
    
    def find_new_target_proxies(self):
        """找出新增的SG/HK/KR/JP代理（与上一次的new数据对比）"""
        new_proxies_by_country = {}
        
        # 获取当前的目标国家代理
        current_target_proxies = {}
        for proxy in self.all_current_proxies:
            country = proxy["country"]
            if country in self.target_countries:
                if country not in current_target_proxies:
                    current_target_proxies[country] = []
                current_target_proxies[country].append(proxy)
        
        # 如果上一次的new数据为空，保存所有目标国家代理
        previous_new = self.previous_data.get("new", {})
        if not previous_new:
            return current_target_proxies
        
        # 对比找出新增代理
        for country in self.target_countries:
            if country not in current_target_proxies:
                continue
                
            current_country_proxies = current_target_proxies[country]
            
            # 从上一次new数据中提取该国家的ip_port列表
            previous_ip_ports = []
            if country in previous_new:
                for old_proxy in previous_new[country]:
                    if isinstance(old_proxy, dict):
                        previous_ip_ports.append(old_proxy.get("ip_port", ""))
                    else:
                        previous_ip_ports.append(old_proxy)
            
            # 找出新增代理（当前有而上一次没有的）
            new_proxies = []
            for proxy in current_country_proxies:
                if proxy["ip_port"] not in previous_ip_ports:
                    new_proxies.append(proxy)
            
            if new_proxies:
                new_proxies_by_country[country] = new_proxies
        
        return new_proxies_by_country
    
    def find_common_proxies(self):
        """找出新旧数据中都有的代理（与上一次的old数据对比），按国家分组"""
        # 将当前所有代理按国家分组
        current_proxies_by_country = {}
        for proxy in self.all_current_proxies:
            country = proxy["country"]
            if country not in current_proxies_by_country:
                current_proxies_by_country[country] = []
            current_proxies_by_country[country].append(proxy)
        
        # 如果上一次的old数据为空，返回当前所有代理（按国家分组）
        previous_old = self.previous_data.get("old", {})
        if not previous_old:
            return current_proxies_by_country
        
        # 找出共同代理（当前和上一次都有的）
        common_proxies_by_country = {}
        
        for country, current_proxies in current_proxies_by_country.items():
            # 从上一次old数据中提取该国家的ip_port列表
            previous_ip_ports = []
            if country in previous_old:
                for old_proxy in previous_old[country]:
                    if isinstance(old_proxy, dict):
                        previous_ip_ports.append(old_proxy.get("ip_port", ""))
                    else:
                        previous_ip_ports.append(old_proxy)
            
            # 找出共同的代理（当前和上一次都有的）
            common_proxies = []
            for proxy in current_proxies:
                if proxy["ip_port"] in previous_ip_ports:
                    common_proxies.append(proxy)
            
            if common_proxies:
                common_proxies_by_country[country] = common_proxies
        
        # 如果没有共同代理，返回当前所有代理（按国家分组）
        if not common_proxies_by_country:
            return current_proxies_by_country
        
        return common_proxies_by_country
    
    def create_telegram_proxy_link(self, ip: str, port: str) -> str:
        """创建Telegram代理链接"""
        return f"tg://socks?server={ip}&port={port}"
    
    def format_target_countries_message(self, proxies_by_country, title):
        """格式化目标国家代理消息"""
        if not proxies_by_country:
            return f"{title}: 无"
        
        message = f"{title}:\n\n"
        
        for country, proxies in proxies_by_country.items():
            if country not in self.target_countries:
                continue
                
            message += f"{country} ({len(proxies)}个):"
            
            for i, proxy in enumerate(proxies, 1):
                telegram_link = self.create_telegram_proxy_link(proxy["ip"], proxy["port"])
                ping = proxy["ping"]
                
                if ping < 200:
                    ping_display = f"🟢🟢🟢 {ping}ms"
                elif ping < 500:
                    ping_display = f"🟡🟡🟡 {ping}ms"
                else:
                    ping_display = f"🔴🔴 {ping}ms"
                
                if telegram_link:
                    message += f'  {i}. <a href="{telegram_link}">{proxy["ip_port"]}</a> \n'
                else:
                    message += f'  {i}. {proxy["ip_port"]} \n'
            
            message += "\n"
        
        return message.strip()
    
    def format_all_proxies_message(self, proxies_by_country, title):
        """格式化所有代理消息（显示所有国家）"""
        if not proxies_by_country:
            return f"{title}: 无"
        
        message = f"{title}:\n\n"
        
        # 先显示目标国家
        for country in self.target_countries:
            if country in proxies_by_country:
                proxies_list = proxies_by_country[country]
                message += f"{country} ({len(proxies_list)}个):"
                
                for i, proxy in enumerate(proxies_list, 1):
                    telegram_link = self.create_telegram_proxy_link(proxy["ip"], proxy["port"])
                    ping = proxy["ping"]
                    
                    
                    if telegram_link:
                        message += f'  {i}. <a href="{telegram_link}">{proxy["ip_port"]}</a>{ping}ms\n'
                    else:
                        message += f'  {i}. {proxy["ip_port"]}{ping}ms\n'
                
                message += "\n"
        
        # 再显示其他国家
        other_countries = []
        for country, proxies_list in proxies_by_country.items():
            if country not in self.target_countries:
                other_countries.append((country, proxies_list))
        
        if other_countries:
            for country, proxies_list in other_countries:
                message += f"{country} ({len(proxies_list)}个):"
                
                for i, proxy in enumerate(proxies_list, 1):
                    telegram_link = self.create_telegram_proxy_link(proxy["ip"], proxy["port"])
                    ping = proxy["ping"]
                   
                    
                    if telegram_link:
                        message += f'  {i}. <a href="{telegram_link}">{proxy["ip_port"]}</a> {ping}ms\n'
                    else:
                        message += f'  {i}. {proxy["ip_port"]}{ping}ms\n'
                
                message += "\n"
        
        return message.strip()
    
    def save_to_file(self, new_proxies, common_proxies):
        """保存代理数据到文件"""
        filepath = os.path.join(self.save_dir, self.filename)
        
        try:
            os.makedirs(self.save_dir, exist_ok=True)
            
            # 确保new数据包含所有目标国家键，即使值为空列表
            for country in self.target_countries:
                if country not in new_proxies:
                    new_proxies[country] = []
            
            # 构建保存数据
            save_data = {
                "new": new_proxies,      # 新增的目标国家代理
                "old": common_proxies    # 共同代理（按国家分组）
            }
            
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(save_data, f, indent=2, ensure_ascii=False)
            print(f"💾💾💾💾💾💾💾💾 代理数据已保存到: {filepath}")
            
            if os.path.exists(filepath):
                file_size = os.path.getsize(filepath)
                print(f"📁📁📁📁📁📁📁📁 文件大小: {file_size} 字节")
                return True
            else:
                print("❌❌❌❌❌❌❌❌ 文件保存失败")
                return False
                
        except Exception as e:
            print(f"❌❌❌❌❌❌❌❌ 保存文件失败: {e}")
            return False
    
    def run(self):
        """主程序"""
        print("=" * 60)
        print("SOCKS5代理监控 - 目标国家版 (SG/HK/KR/JP)")
        print("=" * 60)
        
        os.makedirs(self.save_dir, exist_ok=True)
        print(f"📁📁📁📁📁📁📁📁 工作目录: {self.save_dir}")
        print(f"🎯🎯🎯🎯🎯🎯🎯🎯 目标国家: {', '.join(self.target_countries)}")
        print(f"🌐🌐🌐🌐🌐🌐🌐🌐 测试地址: {self.test_url}")
        
        # 1. 加载Telegram配置
        telegram_ready = self.load_telegram_config()
        
        # 2. 加载上一次数据
        has_previous_data = self.load_previous_data()
        
        # 3. 获取新数据
        proxies = self.fetch_proxies()
        if not proxies:
            if telegram_ready:
                self.send_telegram_message("❌❌❌❌❌❌❌❌ 无法获取SOCKS5代理数据")
            return
        
        # 4. 处理代理数据
        self.process_proxies(proxies)
        
        # 5. 找出新增的目标国家代理（与上一次new数据对比）
        new_proxies = self.find_new_target_proxies()
        
        # 6. 找出共同代理（与上一次old数据对比）
        common_proxies = self.find_common_proxies()
        
        # 7. 对代理进行测试（新增功能）
        print("🧪🧪🧪🧪🧪🧪🧪🧪 开始代理测试...")
        
        # 测试新增代理
        if new_proxies:
            print("🔍🔍🔍 测试新增代理...")
            new_proxies = self.filter_tested_proxies(new_proxies)
        else:
            print("ℹℹ️ 无新增代理需要测试")
        
        # 测试共同代理
        if common_proxies:
            print("🔍🔍🔍 测试共同代理...")
            common_proxies = self.filter_tested_proxies(common_proxies)
        else:
            print("ℹℹ️ 无共同代理需要测试")
        
        # 8. 只有在有新增代理或共同节点时才发送消息
        if telegram_ready and (new_proxies or common_proxies):
            message_parts = []
            
            # 新增代理部分（只显示目标国家）
            if new_proxies:
                total_new = sum(len(p) for p in new_proxies.values()) 
                message_parts.append(self.format_target_countries_message(new_proxies, "新增代理"))
            
            # 共同代理部分（显示所有国家）
            if common_proxies:
                total_common = sum(len(p) for p in common_proxies.values()) 
                message_parts.append(self.format_all_proxies_message(common_proxies, "稳定代理"))
            
            full_message = "\n\n".join(message_parts)
            self.send_telegram_message(full_message)
        elif not (new_proxies or common_proxies):
            print("ℹℹ️ 没有新增代理和稳定代理，不发送通知")
        else:
            print("ℹℹ️ Telegram未配置，跳过通知")
        
        # 9. 显示统计信息
        total_new = sum(len(p) for p in new_proxies.values()) if new_proxies else 0
        total_common = sum(len(p) for p in common_proxies.values()) if common_proxies else 0
        print(f"🆕🆕🆕 新增代理: {total_new} 个")
        print(f"🔁🔁 共同代理: {total_common} 个")
        print(f"🌍🌍 总代理数: {len(self.all_current_proxies)} 个")
        
        # 10. 保存数据（只保存测试通过的代理）
        self.save_to_file(new_proxies, common_proxies)
        
        print("=" * 40)
        print("✅ 程序执行完成")

if __name__ == "__main__":
    collector = Socks5ProxyCollectorWithNotify()
    collector.run()
