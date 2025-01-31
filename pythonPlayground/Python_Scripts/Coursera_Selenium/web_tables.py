import time
from selenium import webdriver
from selenium.webdriver.common.by import By


# Chrome driver
from selenium.webdriver.chrome.service import Service


# Chrome
service_object = Service("../../../../chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=service_object)

# Define Implicit wait
driver.implicitly_wait(2)

# Define driver
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()

# Find and click on "Top Deals" button
driver.find_element(By.LINK_TEXT, "Top Deals").click()

# Get the list with all the open windows
windows_open = driver.window_handles

# Switch to the new window
driver.switch_to.window(windows_open[1])
time.sleep(3)

# Find and click the sort button
driver.find_element(By.CSS_SELECTOR, "th:nth-child(1)").click()

# Get the list of products
list_of_web_elements = driver.find_elements(By.CSS_SELECTOR, "tr td:nth-child(1)")
web_list = []

# Add elements in a list
for element in list_of_web_elements:
    web_list.append(element.text)

# Copy the web list into a new list
sorted_web_list = web_list.copy()
sorted_web_list.sort()

# Check if the list is sorted
assert sorted_web_list == web_list
time.sleep(3)

