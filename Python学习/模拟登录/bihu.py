from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Chrome()
driver.get('http://sso.jwc.whut.edu.cn/Certification/toLogin.do')
name = driver.find_element_by_id('username')
name.send_keys('0121709361026')
pwd = driver.find_element_by_id('password')
pwd.send_keys('xuqihang123456')
button = driver.find_element_by_id('submit_id')
button.click()