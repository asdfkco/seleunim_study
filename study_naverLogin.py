from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome('C:\chromedriver.exe')
#암묵적으로 웹 자원 로드를 위해 3초까지 기다려 준다.
time.sleep(3)

driver.get("https://naver.com")
time.sleep(2)
driver.find_element(By.CLASS_NAME,'link_login').click()

time.sleep(5)
driver.find_element(By.CSS_SELECTOR,'#id').send_keys('rlacksdhr0630')
driver.find_element(By.NAME,'pw').send_keys('rlacksdhr')
driver.find_element(By.XPATH,'//*[@id="log.login"]').click()