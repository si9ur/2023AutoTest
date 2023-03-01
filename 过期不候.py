import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
t = time.time()
# 等5s后如果还未加载完成，则终止加载
driver.set_page_load_timeout(2)
try:
    driver.get("http://woqurefan.cn/")

except:
    driver.execute_script("window.stop()")

el = driver.find_element(By.ID, 'sum_text')
print(el.text)
print(time.time() - t)
