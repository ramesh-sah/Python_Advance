from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

s = Service(
    "C:/Users/rs561/Desktop/PCPS_College/Python_Advance/WebScraping/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=s)
for i in range(1, 50):
    driver.get("http://ncm.edu.np/contact-us/")
    time.sleep(3)
    first_name = driver.find_element_by_xpath(
        """/html/body/div[1]/div[1]/div/div/div/main/div[2]/div[1]/form/p[1]/label/span/input""")
    first_name.send_keys("raghav"+str(i))

    email = driver.find_element_by_xpath(
        """/html/body/div[1]/div[1]/div/div/div/main/div[2]/div[1]/form/p[2]/label/span/input""")
    email.send_keys(f"testing{str(i)}@gmail.com")
    sub = driver.find_element_by_xpath(
        """/html/body/div[1]/div[1]/div/div/div/main/div[2]/div[1]/form/p[3]/label/span/input""")
    sub.send_keys(f"testing{str(i)}")

    message = driver.find_element_by_xpath(
        """/html/body/div[1]/div[1]/div/div/div/main/div[2]/div[1]/form/p[4]/label/span/textarea""")
    message.send_keys(f"testing{str(i)}")

    submit = driver.find_element_by_xpath(
        """/html/body/div[1]/div[1]/div/div/div/main/div[2]/div[1]/form/p[5]/input""")
    submit.send_keys(Keys.ENTER)
