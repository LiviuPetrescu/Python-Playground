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
driver.get("https://the-internet.herokuapp.com/windows")
driver.maximize_window()

# Find and click on the 'Click Here' element
driver.find_element(By.LINK_TEXT, "Click Here").click()

# Get the list with all the open windows
windows_open = driver.window_handles

# Switch to the new window
driver.switch_to.window(windows_open[1])

# Find and click on "New Window" element from the child page
print(driver.find_element(By.TAG_NAME, "h3").text)

# Close the child window
driver.close()

# Switch to the parent window
driver.switch_to.window(windows_open[0])
assert "Opening a new window" == driver.find_element(By.TAG_NAME, "h3").text
