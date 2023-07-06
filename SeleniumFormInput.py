import selenium
import os

# webdriver is what links with browser to perform actions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys  # keyboard keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
os.environ['PATH'] += r"C:\Program Files (x86)\chromedriver.exe"  # add path value to already existing path
driver = webdriver.Chrome()

# driver.get opens up the website
driver.get("https://www.techlistic.com/p/selenium-practice-form.html")
driver.implicitly_wait(5)

# if there is an advertisment that pops up that you want to close, put it in a try catch block
try:
    close_ad = driver.find_element(By.ID, "ezmob-footer-close")
    close_ad.click()
except:
    print('No element with this class name. Skipping...')

fname = driver.find_element(By.NAME, "firstname")
lname = driver.find_element(By.NAME, "lastname")

fname.send_keys('Mahir')
lname.send_keys('Rahman')

sex = driver.find_element(By.ID, "sex-0")
sex.click()


# Wait for user input before closing the browser
input("Press any key to exit...")

driver.quit()