from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import openpyxl

driver = webdriver.Chrome('chromedriver.exe')

wb = openpyxl.Workbook()
ws = wb.active

driver.get("https://youtube.com")
print("검색어 : ",end='')
search_word = input()
ws.append(['index','제목','링크','조회수'])

def search():
    driver.find_element(By.XPATH, '//input[@id="search"]').send_keys(search_word)
    driver.find_element(By.XPATH, '//*[@id="search-icon-legacy"]').click()




def title():
    time.sleep(3)
    for i in range(1,16):
    # ytd-section-list-renderer/div[2]/ytd-item-section-renderer[1]
        title_y = driver.find_element(By.XPATH, f'/html/body/ytd-app/div[1]/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[{i}]/div[1]/div/div[1]/div/h3/a/yt-formatted-string').text
        print(title_y)
        link = driver.find_element(By.XPATH,f'/html/body/ytd-app/div[1]/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[{i}]/div[1]/ytd-thumbnail/a').get_attribute('href')
        print(link)
        views = driver.find_element(By.XPATH,f'/html/body/ytd-app/div[1]/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[{i}]/div[1]/div/div[1]/ytd-video-meta-block/div[1]/div[2]/span[1]').text
        print(views)
        ws.append([i,title_y,link,views])


if __name__ == '__main__':
    search()
    title()
    wb.save("youtube.xlsx")
    print("코드끝")