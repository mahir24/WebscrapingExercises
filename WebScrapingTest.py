import selenium
import os

# webdriver is what links with browser to perform actions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
os.environ['PATH'] += r"C:\Program Files (x86)\chromedriver.exe"  # add path value to already existing path
driver = webdriver.Chrome()

# driver.get opens up the website
driver.get("https://jqueryui.com/resources/demos/progressbar/download.html")

driver.implicitly_wait(8)
# get the object from website in this case the button whose id is downloadButton
# this will return an object that can stored into a variable to manipulate further
my_element = driver.find_element(By.ID, "downloadButton")
# clicks on the element
my_element.click()

# getting new element
# progress_element = driver.find_element(By.CLASS_NAME, 'progress-label')
# print(f"{progress_element.text) # print the text that is found at that class name --> This will just return
# "Starting Download"

# This method will wait x amout of seconds before checking the element by class name and checking the expected text as
# shown in inspector
# doing this will automatically wait until the completed element is acquired before closing the browser
WebDriverWait(driver, 30).until(
    EC.text_to_be_present_in_element(
        (By.CLASS_NAME, 'progress-label'),  # element filtration
        'Complete!'  # expected text
    )
)

# Wait for user input before closing the browser
# input("Press any key to exit...")

# driver.quit()