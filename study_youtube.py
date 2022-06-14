from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome('chromedriver.exe')

driver.get("https://youtube.com")

def search():
    driver.find_element(By.XPATH, '//input[@id="search"]').send_keys('먹방')
    driver.find_element(By.XPATH, '//*[@id="search-icon-legacy"]').click()


search()


def title():
    time.sleep(3)
    # 패스가 애매할뗀 fullxpath로
    for i in range(1,13):
    # ytd-section-list-renderer/div[2]/ytd-item-section-renderer[1]
        title = driver.find_element(By.XPATH, f'/html/body/ytd-app/div[1]/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[{i}]/div[1]/div/div[1]/div/h3/a/yt-formatted-string')
        print(title.text)
title()
print("코드끝")
