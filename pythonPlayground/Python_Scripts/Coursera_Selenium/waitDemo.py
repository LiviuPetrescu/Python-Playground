import time
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
driver.implicitly_wait(2)

# Define driver
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()

# Define the expected list and the actual list
expected_list = ['Cucumber - 1 Kg', 'Raspberry - 1/4 Kg', 'Strawberry - 1/4 Kg']
actual_list = []

# Find the 'Search' button and insert a text
driver.find_element(By.CSS_SELECTOR,'.search-keyword' ).send_keys("ber")
time.sleep(2)

product_list = driver.find_elements(By.XPATH, "//div[@class='products']/div")
number_of_products  = (len(product_list))

# Check the number of products
assert number_of_products > 0

# Chain parent element with a child element
for product in product_list:
    actual_list.append(product.find_element(By.XPATH, "h4").text)
    product.find_element(By.XPATH, "div/button").click()

# Check lists
assert expected_list == actual_list

# Find 'Cart' button and click on it
driver.find_element(By.XPATH , "//img[@alt='Cart']").click()

# Find the 'Proceed to Checkout' button and click on it
driver.find_element(By.XPATH, "//button[normalize-space()='PROCEED TO CHECKOUT']").click()

# Sum validation
total = 0
prices = driver.find_elements(By.CSS_SELECTOR, "tr td:nth-child(5) p")
for price in prices:
    total = total + int(price.text)

web_total = int(driver.find_element(By.CSS_SELECTOR,'.totAmt').text)

# Check web total
assert total == web_total

# Apply promo code
driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()

# Wait for the discount to be applied with EXPLICIT wait
wait  = WebDriverWait(driver, 10)
wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".promoInfo")))
promo_text = driver.find_element(By.CSS_SELECTOR, ".promoInfo").text
promo_check ="Code applied ..!"
assert promo_text == promo_check

# Check if the discount is correct
discount_percent = 0.1
discount_value = web_total - web_total * discount_percent
web_discount_amount = float(driver.find_element(By.CSS_SELECTOR, '.discountAmt').text)
assert discount_value == web_discount_amount


