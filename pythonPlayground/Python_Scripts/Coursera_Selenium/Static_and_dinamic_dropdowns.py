import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

# Chrome driver
from selenium.webdriver.chrome.service import Service


# Chrome
service_object = Service("../../../../chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=service_object)

# Define driver
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.maximize_window()

# Static Dropdown (by visible text, index or value)
static_dropdown = Select(driver.find_element(By.ID, "ctl00_mainContent_DropDownListCurrency"))

# Select 'USD' currency using visible text
static_dropdown.select_by_visible_text("USD")

# Select 'INR' currency using index
static_dropdown.select_by_index(0)

# Select 'AED' currency using value
static_dropdown.select_by_value("AED")

# //////////////////Dynamic Dropdown/////////////////////////////////
# Find the dropdown and insert a value
driver.find_element(By.ID, "autosuggest").send_keys("ind")
time.sleep(2)

# Get all the list element
countries = driver.find_elements(By.CSS_SELECTOR, "li[class='ui-menu-item'] a")

for country in countries:
    if country.text == "India":
        country.click()
        break

# Get the value that was inserted using get_attribute
check_inserted_value = driver.find_element(By.ID, "autosuggest").get_attribute("value")
assert check_inserted_value =="India"

delay = 5
time.sleep(delay)

