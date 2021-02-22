from typing import Sized
from playwright import sync_playwright
import os,time



def run(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.newContext(ignoreHTTPSErrors=True)

    tac = '10.92.2.160'
    usernumber = 2
    i = 0
    # temp = str(int(time.time()*1000))

    # Open new page
    page = context.newPage()

    # Go to https://tac:8443/admin/
    page.goto("https://" + tac + ":8443/admin/")

    # Click input[placeholder="请输入管理员帐号"]
    page.click("input[placeholder=\"请输入管理员帐号\"]")

    # Fill input[placeholder="请输入管理员帐号"]
    page.fill("input[placeholder=\"请输入管理员帐号\"]", "admin")

    # Press Tab
    page.press("input[placeholder=\"请输入管理员帐号\"]", "Tab")

    # Fill input[placeholder="请输入管理员密码"]
    page.fill("input[placeholder=\"请输入管理员密码\"]", "admin@1234")

    # Click input[name="log_bt"]
    # with page.expect_navigation(url="https://" + tac + ":8443/admin/main.php"):
    with page.expect_navigation():
        page.click("input[name=\"log_bt\"]")

    # Click text="身份访问管理"
    page.click("text=\"身份访问管理\"")
    
    for i in range(usernumber):
        i = i + 1
        temp = str(int(time.time()*1000))
        groupname = '组' + temp
        username = 'user' + temp

        # Click text="身份管理"
        # with page.expect_navigation(url="https://" + tac + ":8443/admin/main.php?mid=13"):
        with page.expect_navigation():
            page.click("text=\"身份管理\"")

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

        # Fill //tr[normalize-space(.)='登录名: * ']/td[2]/span/input[1][normalize-space(@type)='text']
        page.fill("//tr[normalize-space(.)='登录名: * ']/td[2]/span/input[1][normalize-space(@type)='text']", username)

        # Fill //span/input[1][normalize-space(@type)='password']
        page.fill("//span/input[1][normalize-space(@type)='password']", "123123")

        # Fill //tr[normalize-space(.)='确认密码:  ']/td[2]/span/input[1][normalize-space(@type)='password']
        page.fill("//tr[normalize-space(.)='确认密码:  ']/td[2]/span/input[1][normalize-space(@type)='password']", "123123")

        #os.system("pause")
        page.waitForSelector("text=\"请选择组\"")
        
        # Click text="请选择组"
        page.click("text=\"请选择组\"")
        
        chosenbox =  "//div[@id='popup-tree-group']//span[text()='"+groupname+"']/preceding-sibling::span[1]"
        #print(chosenbox)  
        page.click(chosenbox)

        # Click text="确定"
        page.click("text=\"确定\"")
        
        # Click text="保存"
        page.click("text=\"保存\"")
        
        # Click text="返回列表"
        page.click("text=\"返回列表\"")

    appnamegroup = ['一级应用','三级应用']
    appurlgroup = ['xxx33.com','xxx250.com']
    appipgroup = ['10.92.2.33','10.92.2.250']
    appportgroup = ['80','80']
    appnumber = len(appnamegroup)
    j = 0
    for j in range(appnumber):
        temp = str(int(time.time()*1000))
        appname = appnamegroup[j]
        appurl =appurlgroup[j]
        appip = appipgroup[j]
        appport = appportgroup[j]
        j = j + 1

        # Click text="资源管理"
        # with page.expect_navigation(url="https://" + tac + ":8443/admin/main.php?mid=114"):
        with page.expect_navigation():
            page.click("text=\"资源管理\"")
 
        # Click a[id="toolbar-add-person"] >> text=/.*添加.*/
        page.click("a[id=\"toolbar-add-person\"] >> text=/.*添加.*/")

        # Click //td[normalize-space(.)='  *']/span/input[1][normalize-space(@type)='text']
        page.click("//td[normalize-space(.)='  *']/span/input[1][normalize-space(@type)='text']")

        # Fill //td[normalize-space(.)='  *']/span/input[1][normalize-space(@type)='text']
        page.fill("//td[normalize-space(.)='  *']/span/input[1][normalize-space(@type)='text']", appname + temp)

        # Click //td[normalize-space(.)='  删除 ']/span/input[1][normalize-space(@type)='text']
        page.click("//td[normalize-space(.)='  删除 ']/span/input[1][normalize-space(@type)='text']")
        # fill
        page.fill("//td[normalize-space(.)='  删除 ']/span/input[1][normalize-space(@type)='text']", appurl)

         # Click text="后台服务"
        page.click("text=\"后台服务\"")

        # Click td[id="update_server_list_add"] >> text="新增一组"
        page.click("td[id=\"update_server_list_add\"] >> text=\"新增一组\"")

        # Click //tr[normalize-space(.)='删除 ']/td[1]/span/input[1][normalize-space(@type)='text']
        page.click("//tr[normalize-space(.)='删除 ']/td[1]/span/input[1][normalize-space(@type)='text']")

        # Fill //tr[normalize-space(.)='删除 ']/td[1]/span/input[1][normalize-space(@type)='text']
        page.fill("//tr[normalize-space(.)='删除 ']/td[1]/span/input[1][normalize-space(@type)='text']", appip)

        # Fill //tr[normalize-space(.)='删除 ']/td[2]/span/input[1][normalize-space(@type)='text']
        page.fill("//tr[normalize-space(.)='删除 ']/td[2]/span/input[1][normalize-space(@type)='text']", appport)

        # Click text="保存"
        page.click("text=\"保存\"")
    
    temp1 = str(int(time.time()*1000))
    ippoolname = '薛ip池'

    # Click text="资源管理"
    # with page.expect_navigation(url="https://" + tac + ":8443/admin/main.php?mid=114"):
    with page.expect_navigation():
        page.click("text=\"资源管理\"")

    # Click div[id="subnav_2_15"] >> text="NC管理"
    # with page.expect_navigation(url="https://" + tac + ":8443/admin/main.php?mid=114&p=113"):
    # with page.expect_navigation():
    #     page.click("div[id=\"subnav_2_15\"] >> text=\"NC管理\"")
    page.goto("https://" + tac + ":8443/admin/main.php?mid=114&p=113")

    # Click div[id="tabshead"] >> text="IP地址池"
    page.click("div[id=\"tabshead\"] >> text=\"IP地址池\"")

    # Click //div[2]/div/div/div[3]/a[1]/span/span[1][normalize-space(.)=' 添加 ']
    page.click("//div[2]/div/div/div[3]/a[1]/span/span[1][normalize-space(.)=' 添加 ']")

    # Click //tr[normalize-space(.)='名字: *']/td[2]/span/input[1][normalize-space(@type)='text']
    page.click("//tr[normalize-space(.)='名字: *']/td[2]/span/input[1][normalize-space(@type)='text']")

    # Fill //tr[normalize-space(.)='名字: *']/td[2]/span/input[1][normalize-space(@type)='text']
    page.fill("//tr[normalize-space(.)='名字: *']/td[2]/span/input[1][normalize-space(@type)='text']", ippoolname + temp1)

    # Click input[name="pool_start"]
    page.click("input[name=\"pool_start\"]")

    # Fill input[name="pool_start"]
    page.fill("input[name=\"pool_start\"]", "1.1.1.2")

    # Click input[name="pool_end"]
    page.click("input[name=\"pool_end\"]")

    # Fill input[name="pool_end"]
    page.fill("input[name=\"pool_end\"]", "1.1.1.22")

    # Click form[id="form1"] >> text="添加"
    page.click("form[id=\"form1\"] >> text=\"添加\"")

    # Click div[id="popup1-buttons"] >> text="保存"
    page.click("div[id=\"popup1-buttons\"] >> text=\"保存\"")

    temp2 = str(int(time.time()*1000))
    ncname = '薛nc设置'

    # Click //a[normalize-space(.)='资源管理']/img
    # with page.expect_navigation(url="https://" + tac + ":8443/admin/main.php?mid=114"):
    with page.expect_navigation():
        page.click("//a[normalize-space(.)='资源管理']/img")

    # Click div[id="subnav_2_15"] >> text="NC管理"
    # with page.expect_navigation(url="https://" + tac + ":8443/admin/main.php?mid=114&p=113"):
    # with page.expect_navigation():
    #     page.click("div[id=\"subnav_2_15\"] >> text=\"NC管理\"")
    page.goto("https://" + tac + ":8443/admin/main.php?mid=114&p=113")

    # Click a[id="toolbar-add-person"] >> text=/.*添加.*/
    page.click("a[id=\"toolbar-add-person\"] >> text=/.*添加.*/")

    # Click //tr[normalize-space(.)='名字: *']/td[2]/span/input[1][normalize-space(@type)='text']
    page.click("//tr[normalize-space(.)='名字: *']/td[2]/span/input[1][normalize-space(@type)='text']")

    # Fill //tr[normalize-space(.)='名字: *']/td[2]/span/input[1][normalize-space(@type)='text']
    page.fill("//tr[normalize-space(.)='名字: *']/td[2]/span/input[1][normalize-space(@type)='text']", ncname + temp2)

    #to do 1.19 //finish 1.21
    # Click //td[normalize-space(.)='--- 11']/span/span/a
    page.click("//td[normalize-space(.)='--- "+ ippoolname +"']/span/span/a")

    # Click //div[2][normalize-space(.)='ip池的名称']
    #1.21——此处的元素顺序是依据IP池创建的顺序加1，若存在多个设置，需要特殊处理
    page.click("//div[2][normalize-space(.)='"+ ippoolname +"']")

    # Click div[id="popup1-buttons"] >> text="保存"
    page.click("div[id=\"popup1-buttons\"] >> text=\"保存\"")

#2021.01.19截至以上均调试完毕
#to do 1.21 // 11：00调试完毕
    with page.expect_navigation():
        page.click("//a[normalize-space(.)='资源管理']/img")

    #page.goto("https://" + tac + ":8443/admin/main.php?mid=114&p=12018")
    # Click text="NC应用"
    # with page.expect_navigation():
    #     page.click("text=\"NC应用\"")
    page.goto("https://" + tac + ":8443/admin/main.php?mid=114&p=12018")
    
    # Click a[id="toolbar-add-person"] >> text=/.*添加.*/
    page.click("a[id=\"toolbar-add-person\"] >> text=/.*添加.*/")

    # Click //td[normalize-space(.)='  *']/span/input[1][normalize-space(@type)='text']
    page.click("//td[normalize-space(.)='  *']/span/input[1][normalize-space(@type)='text']")

    # Fill //td[normalize-space(.)='  *']/span/input[1][normalize-space(@type)='text']
    page.fill("//td[normalize-space(.)='  *']/span/input[1][normalize-space(@type)='text']", "NC应用")

    # Click //td[2]/div[2]/a[1]/span/span[2][normalize-space(.)=' ']
    page.click("//td[2]/div[2]/a[1]/span/span[2][normalize-space(.)=' ']")

    # Click //td[normalize-space(.)='*']/span/input[1][normalize-space(@type)='text']
    page.click("//td[normalize-space(.)='*']/span/input[1][normalize-space(@type)='text']")

    # Fill //td[normalize-space(.)='*']/span/input[1][normalize-space(@type)='text']
    page.fill("//td[normalize-space(.)='*']/span/input[1][normalize-space(@type)='text']", "10.92.2.170")

    # Click //td[normalize-space(.)='TCP UDP ICMP ANY   ']/div/span/input[1][normalize-space(@type)='text']
    page.click("//td[normalize-space(.)='TCP UDP ICMP ANY   ']/div/span/input[1][normalize-space(@type)='text']")

    # Fill //td[normalize-space(.)='TCP UDP ICMP ANY   ']/div/span/input[1][normalize-space(@type)='text']
    page.fill("//td[normalize-space(.)='TCP UDP ICMP ANY   ']/div/span/input[1][normalize-space(@type)='text']", "8443")

    # Click //td[2]/a[2]/span[normalize-space(.)='  ']
    page.click("//td[2]/a[2]/span[normalize-space(.)='  ']")

    # Click div[id="bb"] >> text="保存"
    page.click("div[id=\"bb\"] >> text=\"保存\"")
    # assert page.url == "https://" + tac + ":8443/admin/main.php?mid=114&p=12018#"

    # Click //td[normalize-space(.)=' ']/span/input[1][normalize-space(@type)='text']
    page.click("//td[normalize-space(.)=' ']/span/input[1][normalize-space(@type)='text']")

    # Fill //td[normalize-space(.)=' ']/span/input[1][normalize-space(@type)='text']
    page.fill("//td[normalize-space(.)=' ']/span/input[1][normalize-space(@type)='text']", "https://10.92.2.170:8443")

    # Click text="保存"
    page.click("text=\"保存\"")

    with page.expect_navigation():
        page.click("//a[normalize-space(.)='资源管理']/img")

    # Click text="代理应用"
    # with page.expect_navigation(url="https://" + tac + ":8443/admin/main.php?mid=114&p=2012"):
    # with page.expect_navigation():
    #     page.click("text=\"代理应用\"")
    page.goto("https://" + tac + ":8443/admin/main.php?mid=114&p=2012")

    # Click a[id="toolbar-add-person"] >> text=/.*添加.*/
    page.click("a[id=\"toolbar-add-person\"] >> text=/.*添加.*/")

    # Click //td[normalize-space(.)='  *']/span/input[1][normalize-space(@type)='text']
    page.click("//td[normalize-space(.)='  *']/span/input[1][normalize-space(@type)='text']")

    # Fill //td[normalize-space(.)='  *']/span/input[1][normalize-space(@type)='text']
    page.fill("//td[normalize-space(.)='  *']/span/input[1][normalize-space(@type)='text']", "代理应用")

    # Click //td[2]/div[2]/a[1]/span/span[2][normalize-space(.)=' ']
    page.click("//td[2]/div[2]/a[1]/span/span[2][normalize-space(.)=' ']")

    # Click //td[normalize-space(.)='*']/span/input[1][normalize-space(@type)='text']
    page.click("//td[normalize-space(.)='*']/span/input[1][normalize-space(@type)='text']")

    # Fill //td[normalize-space(.)='*']/span/input[1][normalize-space(@type)='text']
    page.fill("//td[normalize-space(.)='*']/span/input[1][normalize-space(@type)='text']", "10.92.2.250")

    # Click //tr[3]/td[2][normalize-space(.)='*']/span/input[1][normalize-space(@type)='text']
    page.click("//tr[3]/td[2][normalize-space(.)='*']/span/input[1][normalize-space(@type)='text']")

    # Fill //tr[3]/td[2][normalize-space(.)='*']/span/input[1][normalize-space(@type)='text']
    page.fill("//tr[3]/td[2][normalize-space(.)='*']/span/input[1][normalize-space(@type)='text']", "80")

    # Click div[id="bb"] >> text="保存"
    page.click("div[id=\"bb\"] >> text=\"保存\"")
    # assert page.url == "https://" + tac + ":8443/admin/main.php?mid=114&p=2012#"

    # Click //td[normalize-space(.)=' ']/span/input[1][normalize-space(@type)='text']
    page.click("//td[normalize-space(.)=' ']/span/input[1][normalize-space(@type)='text']")

    # Fill //td[normalize-space(.)=' ']/span/input[1][normalize-space(@type)='text']
    page.fill("//td[normalize-space(.)=' ']/span/input[1][normalize-space(@type)='text']", "http://10.92.2.250:80")

    # Click text="保存"
    page.click("text=\"保存\"")

#1.21 11：00 以下待调试

    # Click //a[normalize-space(.)='权限管理']/img
    with page.expect_navigation():
        page.click("//a[normalize-space(.)='权限管理']/img")

    # Click text="授权策略"
    # with page.expect_navigation(url="https://tac:8443/admin/main.php?mid=115&p=10007"):
    with page.expect_navigation():
        page.click("text=\"授权策略\"")

    # Click a[id="toolbar-add-person"] >> text="添加"
    # with page.expect_navigation(url="https://tac:8443/admin/main.php?mid=115&p=10008"):
    with page.expect_navigation():
        page.click("a[id=\"toolbar-add-person\"] >> text=\"添加\"")

    # Click //span/input[1][normalize-space(@type)='text']
    page.click("//span/input[1][normalize-space(@type)='text']")

    # Fill //span/input[1][normalize-space(@type)='text']
    page.fill("//span/input[1][normalize-space(@type)='text']", "xue")

    # Click text="编辑"
    page.click("text=\"编辑\"")

    # Check input[name="ck"]
    page.check("input[name=\"ck\"]")

    # Check tr[id="datagrid-row-r3-2-1"] input[name="ck"]
    page.check("tr[id=\"datagrid-row-r3-2-1\"] input[name=\"ck\"]")

    # Check tr[id="datagrid-row-r3-2-2"] input[name="ck"]
    page.check("tr[id=\"datagrid-row-r3-2-2\"] input[name=\"ck\"]")

    # Check tr[id="datagrid-row-r3-2-3"] input[name="ck"]
    page.check("tr[id=\"datagrid-row-r3-2-3\"] input[name=\"ck\"]")

    # Click div[id="popup-resource-buttons"] >> text="确定"
    page.click("div[id=\"popup-resource-buttons\"] >> text=\"确定\"")

    # Click //li[normalize-space(.)='3.用户']
    page.click("//li[normalize-space(.)='3.用户']")

    # Click div[id="entity-subject"] >> text="编辑"
    page.click("div[id=\"entity-subject\"] >> text=\"编辑\"")

    # Click //div[normalize-space(.)='组1612321180054']/span[4]
    page.click("//div[normalize-space(.)='组1612321180054']/span[4]")

    # Click div[id="popup-user-buttons"] >> text="确定"
    page.click("div[id=\"popup-user-buttons\"] >> text=\"确定\"")

    # Click text="保存"
    page.click("text=\"保存\"")

    # Click //div[28]/div[3]/a[1]/span/span[normalize-space(.)='确定']
    # with page.expect_navigation(url="https://tac:8443/admin/main.php?mid=115&p=10007"):
    with page.expect_navigation():
        page.click("//div[28]/div[3]/a[1]/span/span[normalize-space(.)='确定']")

    # Click //a[normalize-space(.)='认证服务']/img
    with page.expect_navigation():
        page.click("//a[normalize-space(.)='认证服务']/img")
    
    # Click text="认证模块"
    # with page.expect_navigation(url="https://tac:8443/admin/main.php?mid=1024&p=1025"):
    with page.expect_navigation():
        page.click("text=\"认证模块\"")

    # Click //span/span[normalize-space(.)='奇安信ID']
    # with page.expect_navigation(url="https://tac:8443/admin/main.php?mid=1024&p=1028&"):
    with page.expect_navigation():
        page.click("//span/span[normalize-space(.)='奇安信ID']")

    # Click form[id="form1"] input[type="text"]
    page.click("form[id=\"form1\"] input[type=\"text\"]")

    # Fill form[id="form1"] input[type="text"]
    page.fill("form[id=\"form1\"] input[type=\"text\"]", "奇安信ID")

    # Go to https://tac:8443/admin/main.php?mid=1024&p=1025
    page.goto("https://tac:8443/admin/main.php?mid=1024&p=1025")

    # Click text="认证策略"
    # with page.expect_navigation(url="https://tac:8443/admin/main.php?mid=1024&p=1026"):
    with page.expect_navigation():
        page.click("text=\"认证策略\"")

    # Click a[id="toolbar-add-person"] >> text=/.*添加.*/
    # with page.expect_navigation(url="https://tac:8443/admin/main.php?mid=1024&p=10261"):
    with page.expect_navigation():
        page.click("a[id=\"toolbar-add-person\"] >> text=/.*添加.*/")

    # Click input[type="text"]
    page.click("input[type=\"text\"]")

    # Fill input[type="text"]
    page.fill("input[type=\"text\"]", "Agent策略")

    # Fill input[name="app[trigger_method]"]
    page.fill("input[name=\"app[trigger_method]\"]", "0")

    # Go to https://tac:8443/admin/main.php?mid=1024&p=1026
    page.goto("https://tac:8443/admin/main.php?mid=1024&p=1026")

    # Click text="认证门户"
    # with page.expect_navigation(url="https://tac:8443/admin/main.php?mid=1024&p=1024"):
    with page.expect_navigation():
        page.click("text=\"认证门户\"")

    # Click text="PC端默认门户"
    page.click("text=\"PC端默认门户\"")

    # Click //td[normalize-space(.)='默认策略 Agent策略']/span/span/a
    page.click("//td[normalize-space(.)='默认策略 Agent策略']/span/span/a")

    # Click //div[normalize-space(.)='Agent策略']
    page.click("//div[normalize-space(.)='Agent策略']")

    # Click text="保存"
    page.click("text=\"保存\"")

    # Click //div[13]/div[3]/a/span/span[normalize-space(.)='确定']
    page.click("//div[13]/div[3]/a/span/span[normalize-space(.)='确定']")

    # # Go to https://tac:8443/admin/main.php?mid=115&p=10005
    # page.goto("https://" + tac + ":8443/admin/main.php?mid=115&p=10005")

    # # Click a[id="toolbar-add-person"] >> text="添加"
    # # with page.expect_navigation(url="https://" + tac + ":8443/admin/main.php?mid=115&p=10006"):
    # with page.expect_navigation():
    #     page.click("a[id=\"toolbar-add-person\"] >> text=\"添加\"")

    # # Click //span/input[1][normalize-space(@type)='text']
    # page.click("//span/input[1][normalize-space(@type)='text']")

    # # Fill //span/input[1][normalize-space(@type)='text']
    # page.fill("//span/input[1][normalize-space(@type)='text']", "薛资源")

    # # Go to https://tac:8443/admin/main.php?mid=115&p=10005
    # page.goto("https://" + tac + ":8443/admin/main.php?mid=115&p=10005")

    # # Click text="授权策略"
    # # with page.expect_navigation(url="https://" + tac + ":8443/admin/main.php?mid=115&p=10007"):
    # with page.expect_navigation():
    #     page.click("text=\"授权策略\"")

    # # Click a[id="toolbar-add-person"] >> text="添加"
    # # with page.expect_navigation(url="https://" + tac + ":8443/admin/main.php?mid=115&p=10008"):
    # with page.expect_navigation():
    #     page.click("a[id=\"toolbar-add-person\"] >> text=\"添加\"")

    # # Click //span/input[1][normalize-space(@type)='text']
    # page.click("//span/input[1][normalize-space(@type)='text']")

    # # Fill //span/input[1][normalize-space(@type)='text']
    # page.fill("//span/input[1][normalize-space(@type)='text']", "薛授权策略")

    # # Go to https://tac:8443/admin/main.php?mid=115&p=10007
    # page.goto("https://" + tac + ":8443/admin/main.php?mid=115&p=10007")

    # # Click text="认证门户"
    # # with page.expect_navigation(url="https://" + tac + ":8443/admin/main.php?mid=1024&p=1024"):
    # with page.expect_navigation():
    #     page.click("text=\"认证门户\"")

    # # Click a[id="toolbar-add-person"] >> text=/.*添加.*/
    # page.click("a[id=\"toolbar-add-person\"] >> text=/.*添加.*/")

    # # Click text=/.*输入门户名字.*/ >> input[type="text"]
    # page.click("text=/.*输入门户名字.*/ >> input[type=\"text\"]")

    # # Fill text=/.*输入门户名字.*/ >> input[type="text"]
    # page.fill("text=/.*输入门户名字.*/ >> input[type=\"text\"]", "薛路由门户")

    # # Go to https://tac:8443/admin/main.php?mid=1024&p=1032
    # page.goto("https://" + tac + ":8443/admin/main.php?mid=1024&p=1032")

    # # Click a[id="toolbar-add-person"] >> text=/.*添加.*/
    # page.click("a[id=\"toolbar-add-person\"] >> text=/.*添加.*/")

    # # Click form[id="form1"] input[type="text"]
    # page.click("form[id=\"form1\"] input[type=\"text\"]")

    # # Fill form[id="form1"] input[type="text"]
    # page.fill("form[id=\"form1\"] input[type=\"text\"]", "薛路由门户的路由")

    # # Fill //tr[normalize-space(.)='域名:     域名']/td[2]/span/input[1][normalize-space(@type)='text']
    # page.fill("//tr[normalize-space(.)='域名:     域名']/td[2]/span/input[1][normalize-space(@type)='text']", "rzdoor.com")

    # # Go to https://tac:8443/admin/main.php?mid=1024&p=1024
    # page.goto("https://" + tac + ":8443/admin/main.php?mid=1024&p=1024")

    # # Click text="薛路由门户"
    # page.click("text=\"薛路由门户\"")

    # # Click //span/a
    # page.click("//span/a")

    # # Click //td[normalize-space(.)='默认策略']
    # page.click("//td[normalize-space(.)='默认策略']")

    # # Click text="保存"
    # page.click("text=\"保存\"")

    # # Click //div[13]/div[3]/a/span/span[normalize-space(.)='确定']
    # page.click("//div[13]/div[3]/a/span/span[normalize-space(.)='确定']")

    # # Click text="认证策略"
    # # with page.expect_navigation(url="https://" + tac + ":8443/admin/main.php?mid=1024&p=1026"):
    # with page.expect_navigation():
    #     page.click("text=\"认证策略\"")

    # # Click a[id="toolbar-add-person"] >> text=/.*添加.*/
    # # with page.expect_navigation(url="https://" + tac + ":8443/admin/main.php?mid=1024&p=10261"):
    # with page.expect_navigation():
    #     page.click("a[id=\"toolbar-add-person\"] >> text=/.*添加.*/")

    # # Click input[type="text"]
    # page.click("input[type=\"text\"]")

    # # Fill input[type="text"]
    # page.fill("input[type=\"text\"]", "薛路由门户的认证策略")

    # # Fill input[name="app[trigger_method]"]
    # page.fill("input[name=\"app[trigger_method]\"]", "0")

    # # Click //span[normalize-space(.)='多因子']/em
    # page.frame(url="https://" + tac + ":8443/admin/aas/views/mfa_rules.php?id=0").click("//span[normalize-space(.)='多因子']/em")

    # # Click text=/.*取消.*/
    # page.frame(url="https://" + tac + ":8443/admin/aas/views/mfa_rules.php?id=0").click("text=/.*取消.*/")

    # # Go to https://tac:8443/admin/main.php?mid=1024&p=1026
    # page.goto("https://" + tac + ":8443/admin/main.php?mid=1024&p=1026")

    # # Click text="认证模块"
    # # with page.expect_navigation(url="https://" + tac + ":8443/admin/main.php?mid=1024&p=1025"):
    # with page.expect_navigation():
    #     page.click("text=\"认证模块\"")

    # # Click //span/span[normalize-space(.)='奇安信ID']
    # # with page.expect_navigation(url="https://" + tac + ":8443/admin/main.php?mid=1024&p=1028&"):
    # with page.expect_navigation():
    #     page.click("//span/span[normalize-space(.)='奇安信ID']")

    # # Click form[id="form1"] input[type="text"]
    # page.click("form[id=\"form1\"] input[type=\"text\"]")

    # # Fill form[id="form1"] input[type="text"]
    # page.fill("form[id=\"form1\"] input[type=\"text\"]", "奇安信ID")

    # # Go to https://tac:8443/admin/main.php?mid=1024&p=1026
    # page.goto("https://" + tac + ":8443/admin/main.php?mid=1024&p=1026")

    # # Click text="薛路由门户的认证策略"
    # # with page.expect_navigation(url="https://" + tac + ":8443/admin/main.php?mid=1024&p=10261&id=2"):
    # with page.expect_navigation():
    #     page.click("text=\"薛路由门户的认证策略\"")

    # # Click //td[normalize-space(.)='奇安信ID']/span/span/a
    # page.click("//td[normalize-space(.)='奇安信ID']/span/span/a")

    # # Click //div[6]/div/div[normalize-space(.)='奇安信ID']
    # page.click("//div[6]/div/div[normalize-space(.)='奇安信ID']")

    # # Click text="保存"
    # page.click("text=\"保存\"")

    # # Go to https://tac:8443/admin/main.php?mid=1024&p=1026
    # page.goto("https://" + tac + ":8443/admin/main.php?mid=1024&p=1026")

    # # Click text="认证门户"
    # # with page.expect_navigation(url="https://" + tac + ":8443/admin/main.php?mid=1024&p=1024"):
    # with page.expect_navigation():
    #     page.click("text=\"认证门户\"")

    # # Click text="薛路由门户"
    # page.click("text=\"薛路由门户\"")

    # # Click //span/a
    # page.click("//span/a")

    # # Click //div[normalize-space(.)='薛路由门户的认证策略']
    # page.click("//div[normalize-space(.)='薛路由门户的认证策略']")

    # # Click //div[5]/div[3]/a[1]/span/span[2][normalize-space(.)=' ']
    # page.click("//div[5]/div[3]/a[1]/span/span[2][normalize-space(.)=' ']")

    # # Click //div[13]/div[3]/a/span/span[normalize-space(.)='确定']
    # page.click("//div[13]/div[3]/a/span/span[normalize-space(.)='确定']")

    # # Click text="可信代理管理"
    # # with page.expect_navigation(url="https://" + tac + ":8443/admin/main.php?mid=11&p=2002"):
    # with page.expect_navigation():
    #     page.click("text=\"可信代理管理\"")

    # # Click text="资源管理"
    # # with page.expect_navigation(url="https://" + tac + ":8443/admin/main.php?mid=114"):
    # with page.expect_navigation():
    #     page.click("text=\"资源管理\"")

    # # Click text=/.*同步到可信代理.*/
    # # with page.expect_navigation(url="https://" + tac + ":8443/admin/main.php?mid=11&p=2007&op=sync&push_type=wag"):
    # with page.expect_navigation():
    #     page.click("text=/.*同步到可信代理.*/")

    # # Click //div[8]/div[3]/a[1]/span/span[2][normalize-space(.)=' ']
    # page.click("//div[8]/div[3]/a[1]/span/span[2][normalize-space(.)=' ']")

    # # Go to https://tac:8443/admin/main.php?mid=11&p=2007
    # page.goto("https://" + tac + ":8443/admin/main.php?mid=11&p=2007")

    # # Click text="NC应用"
    # # with page.expect_navigation(url="https://" + tac + ":8443/admin/main.php?mid=114&p=12018"):
    # with page.expect_navigation():
    #     page.click("text=\"NC应用\"")

    # # Click text=/.*同步到可信代理.*/
    # # with page.expect_navigation(url="https://" + tac + ":8443/admin/main.php?mid=11&p=2007&op=sync&push_type=l3_proxy"):
    # with page.expect_navigation():
    #     page.click("text=/.*同步到可信代理.*/")

    # # Click a[id="push_save_btn"] >> text="保存"
    # # with page.expect_navigation(url="https://" + tac + ":8443/admin/main.php?mid=11&p=2007"):
    # with page.expect_navigation():
    #     page.click("a[id=\"push_save_btn\"] >> text=\"保存\"")

    # # Click text="代理应用"
    # # with page.expect_navigation(url="https://" + tac + ":8443/admin/main.php?mid=114&p=2012"):
    # with page.expect_navigation():
    #     page.click("text=\"代理应用\"")

    # # Click text=/.*同步到可信代理.*/
    # # with page.expect_navigation(url="https://" + tac + ":8443/admin/main.php?mid=11&p=2007&op=sync&push_type=l4_proxy"):
    # with page.expect_navigation():
    #     page.click("text=/.*同步到可信代理.*/")

    # # Click a[id="push_save_btn"] >> text="保存"
    # # with page.expect_navigation(url="https://" + tac + ":8443/admin/main.php?mid=11&p=2007"):
    # with page.expect_navigation():
    #     page.click("a[id=\"push_save_btn\"] >> text=\"保存\"")

    # # Close page
    # page.close()

    # ---------------------
    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)
