from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

s = Service(
    "C:/Users/rs561/Desktop/PCPS_College/Python_Advance/WebScraping/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=s)

driver.get("https://www.wscubetech.com/")
time.sleep(5)
driver.find_element_by_xpath("""/html/body/section[1]/div/div/div[2]/img""").screenshot(
    "C:/Users/rs561/Desktop/PCPS_College/Python_Advance/WebScraping/ss.png")
driver.save_screenshot(
    "C:/Users/rs561/Desktop/PCPS_College/Python_Advance/WebScraping/full_page.png")
