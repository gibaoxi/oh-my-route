from playwright.sync_api import sync_playwright

# 配置信息（请替换成你的实际信息）
login_url = "https://panel1.serv00.com/login/"
username = "gibaoxi"  # 替换为你的账号
password = "YoxWfDHf8C6B"  # 替换为你的密码

def login_and_get_cookies():
    with sync_playwright() as p:
        # 启动浏览器
        browser = p.chromium.launch(headless=False)  # headless=False 表示显示浏览器窗口
        context = browser.new_context()
        page = context.new_page()

        try:
            # 访问登录页面
            page.goto(login_url)
            print("已访问登录页面")

            # 获取 CSRF Token
            csrf_token = page.input_value('input[name="csrfmiddlewaretoken"]')
            print("CSRF Token:", csrf_token)

            # 填写登录表单
            page.fill('input[name="username"]', username)
            page.fill('input[name="password"]', password)

            # 提交表单
            page.click('button[type="submit"]')
            print("已提交登录表单")

            # 等待页面跳转完成
            page.wait_for_url("**/dashboard/**")  # 根据实际跳转后的 URL 调整
            print("登录成功，已跳转到目标页面")

            # 获取登录后的 Cookie
            cookies = context.cookies()
            cookies_str = "; ".join([f"{cookie['name']}={cookie['value']}" for cookie in cookies])
            print("\n完整的 Cookie 字符串：")
            print(cookies_str)

        except Exception as e:
            print("发生错误:", str(e))
        finally:
            # 关闭浏览器
            browser.close()

if __name__ == "__main__":
    login_and_get_cookies()
