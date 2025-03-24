import os
from playwright.sync_api import sync_playwright

# 从环境变量获取配置
login_url = "https://panel1.serv00.com/login/"
username = "gibaoxi"  # 从环境变量读取用户名
password = "YoxWfDHf8C6B"  # 从环境变量读取密码

def login_and_get_cookies():
    with sync_playwright() as p:
        # 启动浏览器（使用无头模式）
        browser = p.chromium.launch(headless=True)  # GitHub Actions 中必须使用 headless 模式
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

            # 等待按钮可见
            page.wait_for_selector('button[type="submit"]', state="visible", timeout=60000)

            # 滚动到按钮位置
            page.evaluate('document.querySelector("button[type=\\"submit\\"]").scrollIntoView()')

            # 点击按钮
            page.click('button[type="submit"]', timeout=60000)
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
            # 截取页面截图
            page.screenshot(path="error_screenshot.png")
            print("已保存错误截图：error_screenshot.png")
        finally:
            # 关闭浏览器
            browser.close()

if __name__ == "__main__":
    login_and_get_cookies()
