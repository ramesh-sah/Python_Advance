from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

s = Service(
    "C:/Users/rs561/Desktop/PCPS_College/Python_Advance/WebScraping/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=s)

driver.get("https://www.wscubetech.com/")
height = driver.execute_script("return document.body.scrollHeight")
print(height)

while True:
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
