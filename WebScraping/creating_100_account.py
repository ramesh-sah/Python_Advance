from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pandas as pd
from bs4 import BeautifulSoup
import requests
import time

Emails = []

s = Service(
    "C:/Users/rs561/Desktop/PCPS_College/Python_Advance/WebScraping/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get("https://mail.tm/en/")
time.sleep(5)
email = driver.find_element_by_id(
    """Dont_use_WEB_use_API""").get_attribute('value')
Emails.append(email)

print(email)
password = "ramesh@12345"

time.sleep(10)
driver.execute_script("window.open('', '_blank');")

driver.switch_to.window(driver.window_handles[-1])
driver.get("https://www.instagram.com/")
