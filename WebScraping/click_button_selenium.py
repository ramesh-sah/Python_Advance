from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
s = Service(
    "C:/Users/rs561/Desktop/PCPS_College/Python_Advance/WebScraping/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get("https://www.wscubetech.com/")
time.sleep(5)
# copy the xpath of button
driver.find_element_by_xpath(
    """/html/body/section[1]/div/div/div[1]/div/div/a""").click()

time.sleep(3)
driver.find_element_by_xpath(
    """/html/body/section[3]/div/div/div/div/div/div[1]/a/div[1]/img""").click()
