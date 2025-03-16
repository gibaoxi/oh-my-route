import paramiko
import os

# 从环境变量中读取用户名和密码
username = os.getenv('SERV00N')
password = os.getenv('SERV00P')

# 检查是否成功读取环境变量
if not username or not password:
    raise ValueError("请设置环境变量 SERV00_USERNAME 和 SERV00_PASSWORD")

# 服务器信息
host = 'cache1.serv00.com'  # 服务器地址
port = 22                   # SSH 端口

# 创建 SSH 客户端
ssh = paramiko.SSHClient()

# 自动添加主机密钥（第一次连接时）
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    # 连接到服务器
    ssh.connect(host, port=port, username=username, password=password)
    print("成功连接到服务器！")

    # 执行命令（例如：列出当前目录内容）
    stdin, stdout, stderr = ssh.exec_command('ls')
    
    # 输出命令结果
    print("命令输出：")
    print(stdout.read().decode())

    # 如果有错误，输出错误信息
    if stderr.read():
        print("错误信息：")
        print(stderr.read().decode())

except Exception as e:
    print(f"连接失败: {e}")

finally:
    # 关闭连接
    ssh.close()
    print("连接已关闭。")
