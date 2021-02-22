from typing import Sized
from playwright import sync_playwright


def run(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.newContext()

    # Open new page
    page = context.newPage()
    page.goto("https://10.92.2.190:8443/admin/")

    # Click input[placeholder="请输入管理员帐号"]
    page.click("input[placeholder=\"请输入管理员帐号\"]")

    # Fill input[placeholder="请输入管理员帐号"]
    page.fill("input[placeholder=\"请输入管理员帐号\"]", "admin")

    # Press Tab
    page.press("input[placeholder=\"请输入管理员帐号\"]", "Tab")

    # Fill input[placeholder="请输入管理员密码"]
    page.fill("input[placeholder=\"请输入管理员密码\"]", "admin@1234")

    print(page.mouse)
    

with sync_playwright() as playwright:
    run(playwright)