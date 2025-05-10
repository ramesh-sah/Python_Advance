from selenium import webdriver
from selenium.webdriver.chrome.service import Service

s = Service(
    "C:/Users/rs561/Desktop/PCPS_College/Python_Advance/WebScraping/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=s)

driver.get("https://www.wscubetech.com/")
driver.find_element_by_xpath("""/html/body/section[1]/div/div/div[2]/img""")
