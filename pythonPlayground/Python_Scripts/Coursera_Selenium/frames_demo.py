import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


# Chrome driver
from selenium.webdriver.chrome.service import Service


# Chrome
service_object = Service("C:/Users/Hp/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=service_object)

# Define Implicit wait
driver.implicitly_wait(2)

# Define driver
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

# Define action
action = ActionChains(driver)

# Switch to frame using ID or Name
driver.switch_to.frame("courses-iframe")

# Hover on the "More" element of the frame
action.move_to_element(
    driver.find_element(
        By.CSS_SELECTOR, "div[class='nav-outer clearfix'] a[class='dropdown-toggle']"
    )
).click().perform()
time.sleep(2)

# Click on the "About us" element
action.move_to_element(
    driver.find_element(
        By.CSS_SELECTOR, "ul[class='dropdown-menu'] a[href='about-my-mission']"
    )
).click().perform()

# Get 'ABOUT US' text and check it
assert "ABOUT US" == driver.find_element(By.CSS_SELECTOR, "h1").text

# Switch back to the default content
driver.switch_to.default_content()
assert "Practice Page" == driver.find_element(By.CSS_SELECTOR, "h1").text

time.sleep(5)
