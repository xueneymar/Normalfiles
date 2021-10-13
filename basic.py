from playwright import sync_playwright
import os


#定义vpn地址   
vpnip = '10.92.2.233:4430'
#print(type(networkport),type(innerip))

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

    # Click text="应用和组"
    # page.click("text=\"应用和组\"")
    # assert page.url == "https://" + vpnip + "/admin/main.php?mid=12&p=111"
    page.goto("https://" + vpnip + "/admin/main.php?mid=12&p=111")

    # Click a[id="toolbar-add-person"] >> text=/.*添加.*/
    page.click("a[id=\"toolbar-add-person\"] >> text=/.*添加.*/")

    # Click div[id="popup-big-data"] >> text="Proxy"
    page.click("div[id=\"popup-big-data\"] >> text=\"Proxy\"")

    # Click //tr[normalize-space(.)='应用显示名称: *']/td[2]/span/input[1][normalize-space(@type)='text']
    page.click("//tr[normalize-space(.)='应用显示名称: *']/td[2]/span/input[1][normalize-space(@type)='text']")

    # Fill //tr[normalize-space(.)='应用显示名称: *']/td[2]/span/input[1][normalize-space(@type)='text']
    page.fill("//tr[normalize-space(.)='应用显示名称: *']/td[2]/span/input[1][normalize-space(@type)='text']", "proxy_auto")

    # Fill input[name="server"]
    page.fill("input[name=\"server\"]", "10.92.2.33")

    page.click('text="保存"')

    page.click('text="返回列表"')

    # Click a[id="toolbar-add-person"] >> text=/.*添加.*/
    page.click("a[id=\"toolbar-add-person\"] >> text=/.*添加.*/")

    # Click div[id="popup-big-data"] >> text="Proxy"
    page.click("div[id=\"popup-big-data\"] >> text=\"NC\"")

    # Fill //tr[normalize-space(.)='应用显示名称: *']/td[2]/span/input[1][normalize-space(@type)='text']
    page.fill("//tr[normalize-space(.)='应用显示名称: *']/td[2]/span/input[1][normalize-space(@type)='text']", "nc_auto")

    # Fill input[name="server"]
    page.fill("input[name=\"server\"]", "192.168.88.88")

    page.click('text="保存"')

    # Go to https://10.92.2.237:4430/admin/main.php?mid=12&p=113
    page.goto("https://" + vpnip + "/admin/main.php?mid=12&p=113")

    # Click div[id="tabshead"] >> text="IP地址池"
    page.click("div[id=\"tabshead\"] >> text=\"IP地址池\"")

    # Click //div[3]/div/div/div[3]/a[1]/span/span[1][normalize-space(.)=' 添加 ']
    page.click("//div[3]/div/div/div[3]/a[1]/span/span[1][normalize-space(.)=' 添加 ']")

    # Click //tr[normalize-space(.)='名字: *']/td[2]/span/input[1][normalize-space(@type)='text']
    page.click("//tr[normalize-space(.)='名字: *']/td[2]/span/input[1][normalize-space(@type)='text']")

    # Fill //tr[normalize-space(.)='名字: *']/td[2]/span/input[1][normalize-space(@type)='text']
    page.fill("//tr[normalize-space(.)='名字: *']/td[2]/span/input[1][normalize-space(@type)='text']", "pool_auto")

    # Click input[name="pool_start"]
    page.click("input[name=\"pool_start\"]")

    # Fill input[name="pool_start"]
    page.fill("input[name=\"pool_start\"]", "9.9.9.9")

    # Press Tab
    page.press("input[name=\"pool_start\"]", "Tab")

    # Fill input[name="pool_end"]
    page.fill("input[name=\"pool_end\"]", "9.9.9")

    # Click input[name="pool_end"]
    page.click("input[name=\"pool_end\"]")

    # Fill input[name="pool_end"]
    page.fill("input[name=\"pool_end\"]", "9.9.9.99")

    # Click form[id="form1"] >> text="添加"
    page.click("form[id=\"form1\"] >> text=\"添加\"")

    # Click div[id="popup1-buttons"] >> text="保存"
    page.click("div[id=\"popup1-buttons\"] >> text=\"保存\"")

    # Click //a[normalize-space(.)='NC设置']/span[2]
    page.click("//a[normalize-space(.)='NC设置']/span[2]")

    # Click a[id="toolbar-add-person"] >> text=/.*添加.*/
    page.click("a[id=\"toolbar-add-person\"] >> text=/.*添加.*/")

    # Click //tr[normalize-space(.)='名字: *']/td[2]/span/input[1][normalize-space(@type)='text']
    page.click("//tr[normalize-space(.)='名字: *']/td[2]/span/input[1][normalize-space(@type)='text']")

    # Fill //tr[normalize-space(.)='名字: *']/td[2]/span/input[1][normalize-space(@type)='text']
    page.fill("//tr[normalize-space(.)='名字: *']/td[2]/span/input[1][normalize-space(@type)='text']", "nc_auto")

    # Click //td[normalize-space(.)='--- ippool_auto']/span/span/a
    page.click("//td[normalize-space(.)='--- pool_auto']/span/span/a")

    # Click //div[3][normalize-space(.)='pool_auto']
    page.click("//div[2][normalize-space(.)='pool_auto']")

    # Click div[id="popup1-buttons"] >> text="保存"
    page.click("div[id=\"popup1-buttons\"] >> text=\"保存\"")

    # Click text="用户和组"
    # page.click("text=\"用户和组\"")
    # assert page.url == "https://" + vpnip + "/admin/main.php?mid=13&p=121"
    page.goto("https://" + vpnip + "/admin/main.php?mid=13&p=121")

    # Click div[id="top222"] >> text="添加"
    page.click("div[id=\"top222\"] >> text=\"添加\"")

    # Click //tr[normalize-space(.)='名字: *']/td[2]/span/input[1][normalize-space(@type)='text']
    page.click("//tr[normalize-space(.)='名字: *']/td[2]/span/input[1][normalize-space(@type)='text']")

    # Fill //tr[normalize-space(.)='名字: *']/td[2]/span/input[1][normalize-space(@type)='text']
    page.fill("//tr[normalize-space(.)='名字: *']/td[2]/span/input[1][normalize-space(@type)='text']", "group_auto")

    # Click text="保存"
    page.click("text=\"保存\"")

    page.click('text="返回列表"')

    # # Click //div[normalize-space(.)='提示']/div[2]/a
    # page.click("//div[normalize-space(.)='提示']/div[2]/a")

    # # Click //div[normalize-space(.)='添加组  ']/div[2]/a
    # page.click("//div[normalize-space(.)='添加组  ']/div[2]/a")

    # Click //div[3]/a[1]/span/span[1][normalize-space(.)='添加']
    page.click("//div[3]/a[1]/span/span[1][normalize-space(.)='添加']")

    # Click //tr[normalize-space(.)='名字: * ']/td[2]/span/input[1][normalize-space(@type)='text']
    page.click("//tr[normalize-space(.)='名字: * ']/td[2]/span/input[1][normalize-space(@type)='text']")

    # Fill //tr[normalize-space(.)='名字: * ']/td[2]/span/input[1][normalize-space(@type)='text']
    page.fill("//tr[normalize-space(.)='名字: * ']/td[2]/span/input[1][normalize-space(@type)='text']", "user")

    # Click //span/input[1][normalize-space(@type)='password']
    page.click("//span/input[1][normalize-space(@type)='password']")

    # Fill //span/input[1][normalize-space(@type)='password']
    page.fill("//span/input[1][normalize-space(@type)='password']", "aaaaaa")

    # Click //tr[normalize-space(.)='确认密码:  ']/td[2]/span/input[1][normalize-space(@type)='password']
    page.click("//tr[normalize-space(.)='确认密码:  ']/td[2]/span/input[1][normalize-space(@type)='password']")

    # Fill //tr[normalize-space(.)='确认密码:  ']/td[2]/span/input[1][normalize-space(@type)='password']
    page.fill("//tr[normalize-space(.)='确认密码:  ']/td[2]/span/input[1][normalize-space(@type)='password']", "aaaaaa")

    page.click("text=\"保存\"")

    page.click('text="返回列表"')
    
    page.click("//img[normalize-space(@title)='编辑']")

    # Click select[id="group_unsel"] >> text="group_auto"
    page.dblclick("select[id=\"group_unsel\"] >> text=\"group_auto\"")

    # Click select[id="group_sel"] >> text="默认组"
    page.dblclick("select[id=\"group_sel\"] >> text=\"默认组\"")

    page.waitForTimeout(5000)

    page.click("text=\"保存\"")

    page.goto("https://" + vpnip + "/admin/main.php?mid=16&p=153")

    # Click a[id="toolbar-add-person"] >> text=/.*添加.*/
    page.click("a[id=\"toolbar-add-person\"] >> text=/.*添加.*/")

    # Click form[id="form1"] input[type="text"]
    page.click("form[id=\"form1\"] input[type=\"text\"]")

    # Fill form[id="form1"] input[type="text"]
    page.fill("form[id=\"form1\"] input[type=\"text\"]", "ldap_auto")

    # Click //tr[normalize-space(.)="服务器地址: *( 域名或IP，多个服务器请用'|'连接 )"]/td[2]/span/input[1][normalize-space(@type)='text']
    page.click("//tr[normalize-space(.)=\"服务器地址: *( 域名或IP，多个服务器请用'|'连接 )\"]/td[2]/span/input[1][normalize-space(@type)='text']")

    # Fill //tr[normalize-space(.)="服务器地址: *( 域名或IP，多个服务器请用'|'连接 )"]/td[2]/span/input[1][normalize-space(@type)='text']
    page.fill("//tr[normalize-space(.)=\"服务器地址: *( 域名或IP，多个服务器请用'|'连接 )\"]/td[2]/span/input[1][normalize-space(@type)='text']", "10.92.2.250")

    # Click //tr[normalize-space(.)='帐号:  ']/td[2]/span/input[1][normalize-space(@type)='text']
    page.click("//tr[normalize-space(.)='帐号:  ']/td[2]/span/input[1][normalize-space(@type)='text']")

    # Fill //tr[normalize-space(.)='帐号:  ']/td[2]/span/input[1][normalize-space(@type)='text']
    page.fill("//tr[normalize-space(.)='帐号:  ']/td[2]/span/input[1][normalize-space(@type)='text']", "administrator")

    # Press Tab
    page.press("//tr[normalize-space(.)='帐号:  ']/td[2]/span/input[1][normalize-space(@type)='text']", "Tab")

    try:
        # Click //tr[normalize-space(.)='密码:  ']/td[2]/span/input[1][normalize-space(@type)='text']
        page.click("//tr[normalize-space(.)='密码:  ']/td[2]/span/input[1][normalize-space(@type)='text']")
        page.waitForTimeout(10000)
        # Fill //tr[normalize-space(.)='密码:  ']/td[2]/span/input[1][normalize-space(@type)='text']
        page.fill("//tr[normalize-space(.)='密码:  ']/td[2]/span/input[1][normalize-space(@type)='text']", "Admin@QAX")
    except:
        # Click input[name="admin_pass"]
        page.click("input[name=\"admin_pass\"]")
        # Fill input[name="admin_pass"]
        page.fill("input[name=\"admin_pass\"]", "Admin@QAX")

    page.waitForTimeout(2000)

    # Click //td[normalize-space(.)=' *']/span/input[1][normalize-space(@type)='text']
    page.click("//td[normalize-space(.)=' *']/span/input[1][normalize-space(@type)='text']")

    # Fill //td[normalize-space(.)=' *']/span/input[1][normalize-space(@type)='text']
    page.fill("//td[normalize-space(.)=' *']/span/input[1][normalize-space(@type)='text']", "dc=intra,dc=legendsec-cd,dc=com")

    page.waitForTimeout(10000)

    # Click text="保存"
    page.click("text=\"保存\"")

    # Click text="NC管理"
    # page.click("text=\"NC管理\"")
    # assert page.url == "https://" + vpnip + "/admin/main.php?mid=12&p=113"
    page.goto("https://" + vpnip + "/admin/main.php?mid=12&p=113")

    # Click text="nc_auto"
    page.click("text=\"nc_auto\"")

    # Double click text="默认组"
    page.dblclick("text=\"默认组\"")

    # Double click text="group_auto"
    page.dblclick("text=\"group_auto\"")

    # Double click text="ldap_auto"
    page.dblclick("text=\"ldap_auto\"")

    # Click form[id="form1"]
    page.click("form[id=\"form1\"]")

    # Click div[id="popup1-buttons"] >> text="保存"
    page.click("div[id=\"popup1-buttons\"] >> text=\"保存\"")

    # Click text="nc_auto"
    page.click("text=\"nc_auto\"")

    # Click div[id="popup1-buttons"] >> text="保存"
    page.click("div[id=\"popup1-buttons\"] >> text=\"保存\"")

    # Click text="服务控制策略"
    # page.click("text=\"服务控制策略\"")
    # assert page.url == "https://" + vpnip + "/admin/main.php?mid=14&p=131"
    page.goto("https://" + vpnip + "/admin/main.php?mid=14&p=131")

    # Click a[id="toolbar-add-person"] >> text=/.*添加.*/
    page.click("a[id=\"toolbar-add-person\"] >> text=/.*添加.*/")

    # Click //td[normalize-space(.)='   *']/span/input[1][normalize-space(@type)='text']
    page.click("//td[normalize-space(.)='   *']/span/input[1][normalize-space(@type)='text']")

    # Fill //td[normalize-space(.)='   *']/span/input[1][normalize-space(@type)='text']
    page.fill("//td[normalize-space(.)='   *']/span/input[1][normalize-space(@type)='text']", "policy_auto")

    try:
    #6.2.150之前的版本
        page.click('text="请选择组"')
        page.waitForTimeout(10000)
        page.click("//div[normalize-space(.)='默认组']/span[3]")

        page.click("//div[normalize-space(.)='ldap_auto']/span[3]")

        page.click("//div[normalize-space(.)='group_auto']/span[3]")
        
        page.click("div[id=\"popup-tree-group-buttons\"] >> text=\"确定\"")
        
        page.click("text=\"保存\"")
    except:
    #6.2.150版本
        # Double click text="group_auto(默认站点)"
        page.dblclick("text=\"group_auto(默认站点)\"")

        # Double click text="ldap_auto(默认站点)"
        page.dblclick("text=\"ldap_auto(默认站点)\"")

        # Double click text="默认组(默认站点)"
        page.dblclick("text=\"默认组(默认站点)\"")

        page.click("text=\"保存\"")

    page.goto("https://" + vpnip + "/admin/main.php?mid=14&p=131")

    page.click("text=\"policy_auto\"")

    # Click select[id="service_unsel"] >> text="nc_auto"
    page.dblclick("select[id=\"service_unsel\"] >> text=\"nc_auto\"")

    page.dblclick("select[id=\"service_unsel\"] >> text=\"proxy_auto\"")
    
    page.click("text=\"保存\"")

    #默认门户添加ldap_auto用户组
    page.goto("https://" + vpnip + "/admin/main.php?mid=11&p=102")

    # Click text="默认门户"
    page.click("text=\"默认门户\"")

    # Double click text="ldap_auto"
    page.dblclick("text=\"ldap_auto\"")

    # Click text="保存"
    page.click("text=\"保存\"")

    page.click("text=\"系统设置\"")

    # Close page
    page.close()

    # ---------------------
    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)