from playwright import sync_playwright

def run(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.newContext()

    # Open new page
    page = context.newPage()

    # Go to chrome-error://chromewebdata/
    page.goto("chrome-error://chromewebdata/")

    # Go to https://10.92.2.194:8443/admin/
    page.goto("https://10.92.2.194:8443/admin/")

    # Click input[placeholder="请输入管理员帐号"]
    page.click("input[placeholder=\"请输入管理员帐号\"]")

    # Fill input[placeholder="请输入管理员帐号"]
    page.fill("input[placeholder=\"请输入管理员帐号\"]", "admin")

    # Fill input[placeholder="请输入管理员密码"]
    page.fill("input[placeholder=\"请输入管理员密码\"]", "admin@1234")

    # Fill input[placeholder="请输入验证码"]
    page.fill("input[placeholder=\"请输入验证码\"]", "iwcg")

    # Go to https://10.92.2.194:8443/admin/login_action.php?id=0
    page.goto("https://10.92.2.194:8443/admin/login_action.php?id=0")

    # Click text="点击返回登录页面！"
    page.click("text=\"点击返回登录页面！\"")
    # assert page.url == "https://10.92.2.194:8443/admin/login.php"

    # Click input[placeholder="请输入管理员帐号"]
    page.click("input[placeholder=\"请输入管理员帐号\"]")

    # Fill input[placeholder="请输入管理员帐号"]
    page.fill("input[placeholder=\"请输入管理员帐号\"]", "admin")

    # Press Tab
    page.press("input[placeholder=\"请输入管理员帐号\"]", "Tab")

    # Fill input[placeholder="请输入管理员密码"]
    page.fill("input[placeholder=\"请输入管理员密码\"]", "admin@1234")

    # Press Tab
    page.press("input[placeholder=\"请输入管理员密码\"]", "Tab")

    # Fill input[placeholder="请输入验证码"]
    page.fill("input[placeholder=\"请输入验证码\"]", "m39p")

    # Click input[name="log_bt"]
    # with page.expect_navigation(url="https://10.92.2.194:8443/admin/main.php"):
    with page.expect_navigation():
        page.click("input[name=\"log_bt\"]")

    # Close page
    page.close()

    # ---------------------
    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)