import json
import os
import time
import requests
from urllib.parse import urlparse

def test_single_node(node_config, test_url="https://www.google.com.hk"):
    """测试单个节点速度"""
    result = {
        "name": node_config["name"],
        "type": node_config["type"],
        "latency": 0,
        "speed": 0,
        "status": False
    }

    try:
        # 根据协议类型设置代理
        proxy_url = convert_to_proxy_url(node_config)
        proxies = {"http": proxy_url, "https": proxy_url}

        # 测试延迟和速度
        start_time = time.time()
        r = requests.get(test_url, proxies=proxies, timeout=15)
        elapsed = time.time() - start_time

        result.update({
            "status": r.status_code == 204,
            "latency": round(elapsed * 1000, 2),
            "speed": round(len(r.content) / elapsed / 1024, 2)  # KB/s
        })
    except Exception as e:
        result["error"] = str(e)
    
    return result

def convert_to_proxy_url(node_config):
    """将节点配置转换为代理URL"""
    if node_config["type"] == "hysteria":
        return f"socks5://127.0.0.1:1080"  # Hysteria 默认端口
    elif node_config["type"] == "vmess":
        return f"socks5://127.0.0.1:1081"  # V2Ray 默认端口
    else:
        raise ValueError("Unsupported proxy type")

def find_best_node(nodes):
    """找出最优节点"""
    working_nodes = [n for n in nodes if n["status"]]
    if not working_nodes:
        return None
    return sorted(working_nodes, key=lambda x: (-x["speed"], x["latency"]))[0]

if __name__ == "__main__":
    # 1. 加载节点配置
    with open("nodes.json") as f:
        nodes = json.load(f)
    
    # 2. 测试所有节点
    results = []
    for node in nodes:
        print(f"正在测试: {node['name']}")
        result = test_single_node(node)
        results.append(result)
        print(f"结果: {result}\n")
    
    # 3. 选择最优节点
    best_node = find_best_node(results)
    
    # 4. 保存结果
    os.makedirs("results", exist_ok=True)
    with open("results/best_node.txt", "w") as f:
        if best_node:
            f.write(f"最优节点: {best_node['name']}\n")
            f.write(f"类型: {best_node['type']}\n")
            f.write(f"延迟: {best_node['latency']}ms\n")
            f.write(f"速度: {best_node['speed']}KB/s\n")
            f.write(f"配置: {best_node['config']}\n")
        else:
            f.write("没有1可用的节点\n")
    
    # 5. 生成完整报告
    with open("results/full_report.md", "w") as f:
        f.write("# 节点测速报告\n\n")
        for res in results:
            f.write(f"## {res['name']}\n")
            f.write(f"- 状态: {'✅ 可用' if res['status'] else '❌ 不可用'}\n")
            if res["status"]:
                f.write(f"- 延迟: {res['latency']}ms\n")
                f.write(f"- 速度: {res['speed']}KB/s\n")
            if "error" in res:
                f.write(f"- 错误: {res['error']}\n")
            f.write("\n")
