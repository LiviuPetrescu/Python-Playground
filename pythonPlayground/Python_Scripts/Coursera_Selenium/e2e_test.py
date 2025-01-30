from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

# Chrome driver
from selenium.webdriver.chrome.service import Service


# Chrome
service_object = Service("../../../../chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=service_object)

# Define Implicit wait
driver.implicitly_wait(4)

# Define driver
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()

# Find and click on the Shop button
driver.find_element(By.CSS_SELECTOR,"a[href*='shop']").click()

# Find all the products from the page
product_list = driver.find_elements(By.CSS_SELECTOR, "div [class= 'card h-100']")
web_products = []

# Search for a specific brand using chaining
for product in product_list:
    product_name = product.find_element(By.CSS_SELECTOR, "h4[class='card-title']").text
    if product_name == 'Blackberry':
        product.find_element(By.CSS_SELECTOR, "div button").click()

# Go to Checkout page
driver.find_element(By.CSS_SELECTOR,"a[class*= 'btn-primary']").click()

# Find and click on Checkout
driver.find_element(By.CSS_SELECTOR, "button[class*='success']").click()

# Insert delivery location
driver.find_element(By.ID, 'country').send_keys("ind")

# Wait for the discount to be applied with EXPLICIT wait
wait  = WebDriverWait(driver, 10)
wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".suggestions")))

# Get all the suggestions and click on India
driver.find_element(By.LINK_TEXT, "India").click()

# Agree on terms and conditions
driver.find_element(By.XPATH, '//div[@class="checkbox checkbox-primary"]').click()

# Find and click on Purchase
driver.find_element(By.CSS_SELECTOR, '[type="submit"]').click()

# Check if operation was successful
success_text= driver.find_element(By.CLASS_NAME, "alert-success").text
assert "Success! Thank you! " in success_text

driver.close()

