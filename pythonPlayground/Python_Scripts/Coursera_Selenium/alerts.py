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


# Find alert text-box and insert name
name = "Liviu"
driver.find_element(By.CSS_SELECTOR, "#name").send_keys(name)

# Find the Alert button and click on it
driver.find_element(By.CSS_SELECTOR, "#alertbtn").click()

# Switch to alert mode
alert = driver.switch_to.alert
alert_text = alert.text

assert name in alert_text

# Click Ok from alert button
alert.accept()

delay = 5
time.sleep(delay)
