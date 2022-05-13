import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(
    ChromeDriverManager().install(), chrome_options=chrome_options
)

driver.maximize_window()

driver.get("https://www.naver.com")
time.sleep(3)

driver.find_element(By.XPATH, '//*[@id="query"]').send_keys("커피")
driver.find_element(By.ID, 'search_btn').click()

# html = driver.page_source
# print(html)

# driver.back()
# driver.forward()
# driver.quit()
