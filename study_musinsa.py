from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import openpyxl

driver = webdriver.Chrome('C:\chromedriver.exe')
wb = openpyxl.Workbook()
ws = wb.active

driver.get('https://www.musinsa.com/app/')
time.sleep(3)

# ul = driver.find_element(By.CLASS_NAME,'ranking_category')
for i in range(1,25):
    li = driver.find_element(By.XPATH,f'//*[@id="ranking_goods_pager"]/li[{i}]')
    print(li.text)
# print(ul.text)
print("코드끝")
