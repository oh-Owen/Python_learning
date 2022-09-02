from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

url = 'https://www.economist.com/'

driver = webdriver.Chrome()
driver.implicitly_wait(10) #抛出任何错误之前等待 10 秒
driver.get(url)
title = driver.title
html = driver.page_source
wait = WebDriverWait(driver, 10)
time.sleep(30)
'''
# 报错：未找到元素
cookies_button = driver.find_element(By.CLASS_NAME, "message-component message-button no-children focusable teg-button sp_choice_type_11")

cookies_button.click()
x_path = '//*[@id="notice"]/div[4]/div[1]/button'
class = 'message-component message-button no-children focusable teg-button sp_choice_type_11'
parent_class = 'message-component message-column'
cookies_button = driver.switch_to.alert
print(cookies_button.text)
cookies_button.accept
wait.until(EC.element_to_be_clickable((By.XPATH,'/html/body/div/div[2]/div[4]/div[1]/button'))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="notice"]/div[4]/div[1]/button'))).click()

'''

# 处理cookies弹窗
#cookies_button = driver.find_element(By.CSS_SELECTOR, "button[title = 'button']")
cookies_button = driver.find_element(By.XPATH, '/html/body/div/div[2]/div[4]/div[1]/button')
cookies_button.click()
