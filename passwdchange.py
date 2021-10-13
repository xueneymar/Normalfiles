from playwright import sync_playwright

def run(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.newContext()
    address = '10.92.2.190'
    
    # Open new page
    page = context.newPage()

    # Go to https://10.92.2.192:8443/admin/
    page.goto("https://%s:8443/admin/" % address)

    # Click input[placeholder="请输入管理员帐号"]
    page.click("input[placeholder=\"请输入管理员帐号\"]")

    # Fill input[placeholder="请输入管理员帐号"]
    page.fill("input[placeholder=\"请输入管理员帐号\"]", "admin")

    # Fill input[placeholder="请输入管理员密码"]
    page.fill("input[placeholder=\"请输入管理员密码\"]", "!1fw@2soc#3vpn")

    page.click("input[name=\"log_bt\"]")
    # Go to https://10.92.2.192:8443/admin/mod_pass.php
    #page.goto("https://%s:8443/admin/mod_pass.php" % address)
    # Click //span/input[1][normalize-space(@type)='password']
    page.click("//span/input[1][normalize-space(@type)='password']")

    # Fill //span/input[1][normalize-space(@type)='password']
    page.fill("//span/input[1][normalize-space(@type)='password']", "!1fw@2soc#3vpn")

    # Click //td[normalize-space(.)='(>=10位，必须包含字母，符号，数字)']/span/input[1][normalize-space(@type)='password']
    page.click("//td[normalize-space(.)='(>=10位，必须包含字母，符号，数字)']/span/input[1][normalize-space(@type)='password']")

    # Fill //td[normalize-space(.)='(>=10位，必须包含字母，符号，数字)']/span/input[1][normalize-space(@type)='password']
    page.fill("//td[normalize-space(.)='(>=10位，必须包含字母，符号，数字)']/span/input[1][normalize-space(@type)='password']", "admin@1234")

    # Click //tr[normalize-space(.)='确认密码:']/td[2]/span/input[1][normalize-space(@type)='password']
    page.click("//tr[normalize-space(.)='确认密码:']/td[2]/span/input[1][normalize-space(@type)='password']")

    # Fill //tr[normalize-space(.)='确认密码:']/td[2]/span/input[1][normalize-space(@type)='password']
    page.fill("//tr[normalize-space(.)='确认密码:']/td[2]/span/input[1][normalize-space(@type)='password']", "admin@1234")

    # Click text="保存"
    # with page.expect_navigation(url="https://10.92.2.192:8443/admin/login.php"):
    with page.expect_navigation():
        page.click("text=\"保存\"")

    # Close page
    page.close()

    # ---------------------
    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)