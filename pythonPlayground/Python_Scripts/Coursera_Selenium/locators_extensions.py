import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Chrome driver
from selenium.webdriver.chrome.service import Service


# Chrome
service_object = Service("../../../../chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=service_object)

# Define driver
driver.get("https://rahulshettyacademy.com/client")
driver.maximize_window()

#  Find and click on 'Forgot Password' link
driver.find_element(By.LINK_TEXT,"Forgot password?").click()

#  Find and insert Email address
new_email_element = driver.find_element(By.XPATH, "//form/div[1]/input")
new_email_element.clear()
new_email_element.send_keys("petrescu_liviu1987@yahoo.com")

#  Find and insert Password using CSS Selector using ID
new_password_element = driver.find_element(By.CSS_SELECTOR, "#userPassword")
new_password_element.clear()
new_password_element.send_keys("123456@789")

#  Find and insert Password using CSS Selector //button[@type='submit']
repeat_password_element = driver.find_element(By.CSS_SELECTOR, "form div:nth-child(3) input")
repeat_password_element.clear()
repeat_password_element.send_keys("123456@789")

# Find and click on 'Submit' button
# driver.find_element(By.XPATH, "//button[@type='submit']").click()

# Find and click on 'Submit' button using TEXT
driver.find_element(By.XPATH, "//button[text()='Save New Password']").click()




delay = 10
time.sleep(delay)