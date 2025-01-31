import time
from selenium import webdriver

# Chrome driver
from selenium.webdriver.chrome.service import Service

# Create Chrome options to run headless
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("headless")

# Ignore certificate errors
chrome_options.add_argument("--ignore-certificate-errors")

# Chrome in headless mode
service_object = Service("../../../../chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=service_object, options=chrome_options)

# Define Implicit wait
driver.implicitly_wait(2)

# Define driver
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

# Scroll to the bottom of the page using JavaScript
driver.execute_script("window.scrollBy(0, document.body.scrollHeight);")


# Take a screenshot
driver.get_screenshot_as_file("screen.png")

time.sleep(5)
