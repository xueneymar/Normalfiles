from playwright import sync_playwright
import os,time


#定义vpn地址   
vpnip = '10.92.2.233:4430'
#print(type(networkport),type(innerip))
number = 300

def run(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.newContext(ignoreHTTPSErrors=True)

    # Open new page
    page = context.newPage()

    # Go to chrome-error://chromewebdata/
    #page.goto("chrome-error://chromewebdata/")

    # Go to https://10.92.2.237:4430/admin/
    page.goto("https://" + vpnip + "/admin/")

    # Click input[placeholder="请输入管理员帐号"]
    page.click("input[placeholder=\"请输入管理员帐号\"]")

    # Fill input[placeholder="请输入管理员帐号"]
    page.fill("input[placeholder=\"请输入管理员帐号\"]", "admin")

    # Fill input[placeholder="请输入管理员密码"]
    page.fill("input[placeholder=\"请输入管理员密码\"]", "admin@1234")
    
    page.click("input[name='log_bt']")

    # Go to https://10.92.2.237:4430/admin/home.php
    page.goto("https://" + vpnip + "/admin/home.php")

    # Click a:nth-child(3) img
    page.click("a:nth-child(3) img")
    # assert page.url == "https://" + vpnip + "/admin/main.php?mid=12"

    for i in range(number):
        i = i + 1
        temp = str(int(time.time()*1000))
        ncname = 'nc_auto' + temp
        # Click text="应用和组"
        # page.click("text=\"应用和组\"")
        # assert page.url == "https://" + vpnip + "/admin/main.php?mid=12&p=111"
        page.goto("https://" + vpnip + "/admin/main.php?mid=12&p=111")

        # Click a[id="toolbar-add-person"] >> text=/.*添加.*/
        page.click("a[id=\"toolbar-add-person\"] >> text=/.*添加.*/")
    
        # Click div[id="popup-big-data"] >> text="Proxy"
        page.click("div[id=\"popup-big-data\"] >> text=\"NC\"")
    
        # Fill //tr[normalize-space(.)='应用显示名称: *']/td[2]/span/input[1][normalize-space(@type)='text']
        page.fill("//tr[normalize-space(.)='应用显示名称: *']/td[2]/span/input[1][normalize-space(@type)='text']", ncname)
    
        # Fill input[name="server"]
        page.fill("input[name=\"server\"]", "192.168.88.88")
    
        page.click('text="保存"')

    # Close page
    page.close()

    # ---------------------
    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)