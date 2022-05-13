import time
import pyperclip
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

naver_id = "a"
naver_pw = "asdf"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(
    ChromeDriverManager().install(), chrome_options=chrome_options
)

driver.maximize_window()

driver.get("https://www.naver.com")
time.sleep(3)

driver.find_element(By.CLASS_NAME, "link_login").click()
time.sleep(2)

driver.find_element(By.ID, "id").click()
pyperclip.copy(naver_id)
driver.find_element(By.ID, "id").send_keys(Keys.COMMAND, "v")
time.sleep(1)

driver.find_element(By.ID, "pw").click()
pyperclip.copy(naver_pw)
driver.find_element(By.ID, "pw").send_keys(Keys.COMMAND, "v")
time.sleep(1)

driver.find_element(By.CLASS_NAME, "btn_login").click()
time.sleep(2)
