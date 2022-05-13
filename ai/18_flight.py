import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(
    ChromeDriverManager().install(), chrome_options=chrome_options
)

driver.get("https://flight.naver.com/")
time.sleep(3)

driver.find_element(
    By.XPATH, '//*[@id="__next"]/div/div[1]/div[4]/div/div/div[1]/button[2]/i',
).click()
time.sleep(1)

driver.find_element(By.CLASS_NAME, "start").click()
time.sleep(1)

driver.find_element(By.CLASS_NAME, "autocomplete_input__1vVkF").send_keys("서울")
time.sleep(1)

driver.find_element(
    By.XPATH, '//*[@id="__next"]/div/div[1]/div[9]/div[2]/section/div/a[1]'
).click()
time.sleep(1)

driver.find_element(By.CLASS_NAME, "end").click()
time.sleep(1)

driver.find_element(By.CLASS_NAME, "autocomplete_input__1vVkF").send_keys("제주")
time.sleep(1)

driver.find_element(
    By.XPATH, '//*[@id="__next"]/div/div[1]/div[9]/div[2]/section/div/a[1]'
).click()
time.sleep(1)

driver.find_element(
    By.XPATH, '//*[@id="__next"]/div/div[1]/div[4]/div/div/div[2]/div[2]/button'
).click()
time.sleep(1)

month_data = driver.find_elements(By.CLASS_NAME, "month")
day_data = month_data[0].find_elements(By.CLASS_NAME, "num")
day_data[12].click()
time.sleep(1)

driver.find_element(
    By.XPATH, '//*[@id="__next"]/div/div[1]/div[4]/div/div/button'
).click()
time.sleep(10)

html = BeautifulSoup(driver.page_source, "lxml")
results = html.find_all("div", class_="result")

for temp in results:
    r_dict = {}
    r_dict["항공사"] = temp.find("img", class_="logo")["alt"]

    timedata = temp.find_all("b", class_="route_time__-2Z1T")
    r_dict["출발시간"] = timedata[0].text
    r_dict["도착시간"] = timedata[1].text

    r_dict["요금"] = temp.find("i", class_="domestic_num__2roTW").text

    print(r_dict)
