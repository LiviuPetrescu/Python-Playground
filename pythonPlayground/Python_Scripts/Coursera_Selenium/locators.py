import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Chrome driver
from selenium.webdriver.chrome.service import Service

# Chrome
service_object = Service("C:/Users/Hp/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=service_object)

# Define driver
driver.get("https://www.letskodeit.com/")
driver.maximize_window()

# Find the Sign In using XPath/CSS and click on it
# XPath -> //tagname[@attribute=value]
sign_in_element = driver.find_element(
    By.XPATH, '//a[@href="/login" and @class="dynamic-link"]'
)
# CSS Selector -> tagname[attribute=value] -> #id, -> .classname
# sign_in_element = driver.find_element(By.CSS_SELECTOR, 'a[href="/login"]')
sign_in_element.click()

# Find the Email and Password and insert the login info
email_element = driver.find_element(By.ID, "email")
email_element.clear()
email_element.send_keys("petrescu_liviu1987@yahoo.com")
password_element = driver.find_element(By.ID, "login-password")
password_element.clear()
password_element.send_keys("Admin.06!")

# Sign in
driver.find_element(By.ID, "login").click()
login_picture = None
delay = 10
time.sleep(delay)
try:
    login_picture = driver.find_element(By.ID, "dropdownMenu1")
except Exception as e:
    print(e)

# Check if the login was successful
assert login_picture is not None
