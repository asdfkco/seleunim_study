from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import openpyxl

driver = webdriver.Chrome('C:\chromedriver.exe')
wb = openpyxl.Workbook()
ws = wb.active

driver.get('https://www.musinsa.com/app/')
driver.implicitly_wait(3)
driver.set_window_size(1920,1080)
# ul = driver.find_element(By.CLASS_NAME,'ranking_category')
# ws.append(['제품명','조회수','','',''])
for i in range(1,25):
    driver.find_element(By.XPATH,f'//*[@id="ranking_goods_pager"]/li[{i}]').click()
    for J in range(1,15):
        driver.find_element(By.XPATH,f'//*[@id="ranking_goods_pager"]/li[{i}]').click()
        #한바퀴  돌고 입력키가 안먹는 오류생김
        driver.find_element(By.XPATH, f'//*[@id="ranking_goods"]/div[{J}]').find_element(By.TAG_NAME,'a').send_keys(Keys.CONTROL,Keys.ENTER)
        driver.switch_to.window(driver.window_handles[-1])
        title = driver.find_element(By.CLASS_NAME,'product_title').find_element(By.TAG_NAME,'em')
        views = driver.find_element(By.ID,'pageview_1m')
        like = driver.find_element(By.CLASS_NAME,'prd_like_cnt')
        defult_price = driver.find_element(By.CLASS_NAME,'price-del')
        sale_price = driver.find_element(By.ID,'list_price')
        print(title.text,views.text,like.text,defult_price.text,sale_price.text)
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
# print(ul.text)
print("코드끝")
