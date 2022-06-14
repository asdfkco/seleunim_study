import time

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('C:/chromedriver.exe')
import openpyxl


def main():
    idx = 1

    wb = openpyxl.Workbook()
    ws = wb.active  # 현재 활성화된 셀을 보는것
    ws.append(["id", "분류", "상품명", "가격", "젛아요수", "설명", "이미지URL", "구매처URL"])
    driver.get("https://www.musinsa.com/ranking/best")
    for i in range(5):
        time.sleep(1)
        type = driver.find_elements(By.XPATH, '//*[@id="goodsRankForm"]/div[1]/div[2]/dl/dd/ul/li')
        typeValue = type[i].text
        print(typeValue)
        type[i].find_element(By.TAG_NAME, "a").send_keys(Keys.ENTER)
        for j in range(10):
            itemList = driver.find_element(By.ID, "goodsRankList").find_elements(By.CLASS_NAME, "li_box")
            brandName = itemList[j].find_element(By.CLASS_NAME, "item_title").text
            title = itemList[j].find_element(By.CLASS_NAME, "list_info").text
            price = itemList[j].find_element(By.CLASS_NAME, "price")
            count = itemList[j].find_element(By.NAME, "count").text
            image = itemList[j].find_element(By.CLASS_NAME, "list_img").find_element(By.TAG_NAME, "img").get_attribute(
                "data-original")
            url = itemList[j].find_element(By.CLASS_NAME, "list_img").find_element(By.TAG_NAME, "a").get_attribute(
                "href")
            gender = itemList[j].find_element(By.CLASS_NAME, "icon_group").find_element(By.TAG_NAME, "ul").text
            try:
                original_price = price.find_element(By.TAG_NAME, "del")
                result = price.text.split(original_price.text)
                result_price = result[1].strip()
            except NoSuchElementException:  # 할인하지않는것은 여기서 정리해줌
                result_price = price.text

            result = []
            result.append(idx)
            result.append(typeValue)
            result.append(title)
            result.append(result_price)
            result.append(count)
            result.append(image)
            result.append(url)
            result.append(gender)
            print(result)
            ws.append(result)
            idx += 1
        wb.save("musinsaa.xlsx")


if __name__ == '__main__':
    main()
