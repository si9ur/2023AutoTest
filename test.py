from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
# driver.find_element(By.ID, 'kw').send_keys("sigur ros")

el = driver.find_element(By.ID,'kw').send_keys("llll")
el = WebDriverWait()
# print(el.value_of_css_property())
driver.find_element(By.ID,"su").click()
driver.maximize_window()
driver.implicitly_wait(3)
print (driver.get_window_size())
time.sleep(5)
#测试
