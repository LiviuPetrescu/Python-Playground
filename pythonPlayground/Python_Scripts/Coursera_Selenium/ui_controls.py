import time
from selenium import webdriver
from selenium.webdriver.common.by import By


# Chrome driver
from selenium.webdriver.chrome.service import Service


# Chrome
service_object = Service("../../../../chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=service_object)

# Define driver
driver.get("https://rahulshettyacademy.com/AutomationPractice")
driver.maximize_window()

# Find the checkbox and select it
checkbox = driver.find_element(By.ID, "checkBoxOption2")
checkbox.click()
assert checkbox.is_selected()

# Find the radio button and select it
radio_button = driver.find_elements(By.CSS_SELECTOR, ".radioButton")
radio_button[2].click()
assert radio_button[2].is_selected()

# Check if an element is displayed
assert driver.find_element(By.ID, "displayed-text").is_displayed()

# Click on 'Hide' button
driver.find_element(By.ID, "hide-textbox").click()

# Check if an element is not displayed
assert not driver.find_element(By.ID, "displayed-text").is_displayed()

delay = 5
time.sleep(delay)