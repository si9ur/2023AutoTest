from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
driver.find_element(By.ID, 'kw').send_keys("sigur ros")
driver.find_element(By.ID,"su").click()
time.sleep(5)
#测试
