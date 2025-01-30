import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Chrome driver
from selenium.webdriver.chrome.service import Service

# Create different Chrome options (maximized, headless, ignore certificate errors)
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("headless")
chrome_options.add_argument("--ignore-certificate-errors")

# Chrome
service_object = Service("../../../../chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=service_object, options=chrome_options)

# Define driver
driver.get("https://rahulshettyacademy.com/angularpractice/")

print(driver.title)