# coding=utf-8
import os
import requests
from bs4 import BeautifulSoup
import base64

def fetch_and_save(url):
    temp_file = None
    try:
        # 获取网页内容
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        
        # 解析HTML
        soup = BeautifulSoup(response.text, 'html.parser')
        paragraphs = soup.find_all('p')  # 正确定义变量

        # 写入临时文件
        temp_file = 'gg_temp.txt'
        with open(temp_file, 'w', encoding='utf-8') as f:
            for p in paragraphs:
                if text := p.get_text().strip():
                    f.write(text + '\n')

        # 读取并编码内容
        with open(temp_file, 'r', encoding='utf-8') as f:
            encoded_content = base64.b64encode(f.read().encode('utf-8')).decode('utf-8')

        # 确保目录存在
        os.makedirs('results', exist_ok=True)  # 统一使用 'results'
        output_path = os.path.join('results', 'gg.txt')
        
        # 写入最终文件
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(encoded_content)

        print(f"成功保存并加密 {len(paragraphs)} 个节点到 {output_path}")
        return True

    except requests.exceptions.RequestException as e:
        print(f"网络请求失败: {str(e)}")
    except Exception as e:
        print(f"操作失败: {str(e)}")
    finally:
        if temp_file and os.path.exists(temp_file):
            os.remove(temp_file)
    return False

if __name__ == '__main__':
    url = 'https://gvyyb.deno.dev/'  # 测试URL
    fetch_and_save(url)