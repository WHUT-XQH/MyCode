from selenium import webdriver
from selenium.webdriver.common.actions.interaction import KEY
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import ssl
from selenium.webdriver.common.action_chains import ActionChains
import pyautogui


header= {
        'Host': 'i3.mmzztt.com',
        'Accept-Encoding': 'gzip, deflate,br',
        'Upgrade-Insecure-Requests': '1',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:78.0) Gecko/20100101 Firefox/78.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
         }

driver = webdriver.Chrome()
driver.get("https://www.mzitu.com/")
driver.maximize_window()
time.sleep(1)
input = driver.find_element_by_class_name('search-input')
input.send_keys('美女')
button = driver.find_element_by_class_name('search-btn')
button.click()
img = driver.find_element_by_class_name('postlist').find_element_by_tag_name('li').find_element_by_tag_name('span').find_element_by_tag_name('a')
img.click()

time.sleep(3)
driver.quit()
