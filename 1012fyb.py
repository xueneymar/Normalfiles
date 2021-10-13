'''
Author: your name
Date: 2021-10-12 16:59:43
LastEditTime: 2021-10-12 19:33:40
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \PYTHON\1012fyb.py
'''

import time
from selenium import webdriver

browser = webdriver.Firefox()
browser.get('https://business.oceanengine.com/site/login')
username="zjkaihu1@bocmof.cn"
passwd="Bocweb123!@#"
elem=browser.find_element_by_name("email")
elem.send_keys(username)
elem=browser.find_element_by_name("password")
elem.send_keys(passwd)
account=browser.find_element_by_css_selector('button.account-center-action-button')
account.click()
time.sleep(15)
# js='window.open("https://ad.oceanengine.com/bp/ads/ad_create?campaign_id=1713034988078110&landing_type=1&aadvid=1710506411413518&temp_id=ADTUh");'
# browser.execute_script(js)
browser.get('https://ad.oceanengine.com/bp/ads/ad_create?campaign_id=1713034988078110&landing_type=1&aadvid=1710506411413518&temp_id=ADTUh')
time.sleep(10)
handlers=browser.window_handles
browser.find_element_by_xpath('//*[@id="ad-main"]/div[4]/div[3]/div[1]/div[1]/div[2]/div/button[2]').click()