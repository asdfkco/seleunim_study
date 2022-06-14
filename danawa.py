from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome('C:/chromedriver.exe')


def main():
    driver.get("https://www.danawa.com/")
    time.sleep(2)
    driver.find_element(By.XPATH, '//input[@id="search"]').send_keys('뭉탱이월드')


if __name__ == '__main__':
    main()