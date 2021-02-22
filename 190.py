from playwright import sync_playwright
from time import time

def run(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.newContext()
    i = 0
    usernumber = 10

    # Open new page
    page = context.newPage()

    # Go to https://10.92.2.190:8443/admin/
    page.goto("https://10.92.2.196:8443/admin/")

    # Click input[placeholder="请输入管理员帐号"]
    page.click("input[placeholder=\"请输入管理员帐号\"]")

    # Fill input[placeholder="请输入管理员帐号"]
    page.fill("input[placeholder=\"请输入管理员帐号\"]", "admin")

    # Press Tab
    page.press("input[placeholder=\"请输入管理员帐号\"]", "Tab")

    # Fill input[placeholder="请输入管理员密码"]
    page.fill("input[placeholder=\"请输入管理员密码\"]", "admin@12345")

    # Click input[name="log_bt"]
    # with page.expect_navigation(url="https://10.92.2.190:8443/admin/main.php"):
    with page.expect_navigation():
        page.click("input[name=\"log_bt\"]")

    # Click text="身份访问管理"
    page.click("text=\"身份访问管理\"")

    # Click text="身份管理"
    # with page.expect_navigation(url="https://10.92.2.190:8443/admin/main.php?mid=13"):
    with page.expect_navigation():
        page.click("text=\"身份管理\"")

    for i in range(usernumber):
        i = i + 1
        temp = str(int(time()*1000))
        groupname = '组' + temp
        username = 'user' + temp
        # Click div[id="top222"] >> text="添加"
        page.click("div[id=\"top222\"] >> text=\"添加\"")

        # Click //tr[normalize-space(.)='名字: *']/td[2]/span/input[1][normalize-space(@type)='text']
        page.click("//tr[normalize-space(.)='名字: *']/td[2]/span/input[1][normalize-space(@type)='text']")

        # Fill //tr[normalize-space(.)='名字: *']/td[2]/span/input[1][normalize-space(@type)='text']
        page.fill("//tr[normalize-space(.)='名字: *']/td[2]/span/input[1][normalize-space(@type)='text']", groupname)

        # Click text="保存"
        page.click("text=\"保存\"")

        # Click text="返回列表"
        page.click("text=\"返回列表\"")
    
        # Click //div[3]/a[1]/span/span[1][normalize-space(.)='添加']
        page.click("//div[3]/a[1]/span/span[1][normalize-space(.)='添加']")
    
        # Click //tr[normalize-space(.)='登录名: * ']/td[2]/span/input[1][normalize-space(@type)='text']
        page.click("//tr[normalize-space(.)='登录名: * ']/td[2]/span/input[1][normalize-space(@type)='text']")
    
        # Fill //tr[normalize-space(.)='登录名: * ']/td[2]/span/input[1][normalize-space(@type)='text']
        page.fill("//tr[normalize-space(.)='登录名: * ']/td[2]/span/input[1][normalize-space(@type)='text']", username)
    
        # Click //span/input[1][normalize-space(@type)='password']
        page.click("//span/input[1][normalize-space(@type)='password']")
    
        # Fill //span/input[1][normalize-space(@type)='password']
        page.fill("//span/input[1][normalize-space(@type)='password']", "123456")
    
        # Click //tr[normalize-space(.)='确认密码:  ']/td[2]/span/input[1][normalize-space(@type)='password']
        page.click("//tr[normalize-space(.)='确认密码:  ']/td[2]/span/input[1][normalize-space(@type)='password']")
    
        # Fill //tr[normalize-space(.)='确认密码:  ']/td[2]/span/input[1][normalize-space(@type)='password']
        page.fill("//tr[normalize-space(.)='确认密码:  ']/td[2]/span/input[1][normalize-space(@type)='password']", "123456")
    
        # Click text="请选择组"
        page.click("text=\"请选择组\"")
    
        chosenbox =  "//div[@id='popup-tree-group']//span[text()='"+groupname+"']/preceding-sibling::span[1]"
        #print(chosenbox)  
        # Click //div/ul/li[7]/div[normalize-space(.)='zz']/span[3]
        page.click(chosenbox)
        
        # Click text="确定"
        page.click("text=\"确定\"")
    
        # Click text="保存"
        page.click("text=\"保存\"")
    
        # Click text="返回列表"
        page.click("text=\"返回列表\"")
        #print(i)
    
   
    # Close page
    page.close()

    # ---------------------
    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)