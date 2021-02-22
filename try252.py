from playwright import sync_playwright

user = 'xyl'
passwd = '123456'

def run(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.newContext()

    # Open new page
    page = context.newPage()

    # Go to http://10.92.2.252:5000/login
    page.goto("http://10.92.2.252:5000/login")

    # Click input[name="username"]
    page.click("input[name=\"username\"]")

    # Fill input[name="username"]
    page.fill("input[name=\"username\"]", user)

    # Press Tab
    page.press("input[name=\"username\"]", "Tab")

    # Fill input[name="password"]
    page.fill("input[name=\"password\"]", passwd)

    # Click input[type="submit"]
    page.click("input[type=\"submit\"]")
    # assert page.url == "http://10.92.2.252:5000/"
    

    # Click text=/.*退出.*/
    page.click("text=/.*退出.*/")
    # assert page.url == "http://10.92.2.252:5000/login"

    # Close page
    #page.close()

    # ---------------------
    #context.close()
    #browser.close()

with sync_playwright() as playwright:
    run(playwright)