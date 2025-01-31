import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


# Chrome driver
from selenium.webdriver.chrome.service import Service


# Chrome
service_object = Service("../../../../chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=service_object)

# Define Implicit wait
driver.implicitly_wait(2)

# Define driver
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

# Define action
action = ActionChains(driver)

# Hover over the "Mouse Hover "element
action.move_to_element(driver.find_element(By.ID, "mousehover")).perform()

# Right-click on the element
action.context_click(driver.find_element(By.LINK_TEXT, "Top")).perform()

# Click on the "Reload" element
action.move_to_element(driver.find_element(By.LINK_TEXT, "Reload")).click().perform()

time.sleep(5)
