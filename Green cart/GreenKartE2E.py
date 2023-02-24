import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=ChromeService(), options=chrome_options)

driver.maximize_window()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
print(driver.current_url)
driver.implicitly_wait(3)  # implicit wait global wait

searchItem = "be"
driver.find_element(By.CSS_SELECTOR, '.search-keyword').send_keys(searchItem)
time.sleep(2)

allProducts = driver.find_elements(By.XPATH, "//div[@class='products']/div")

count = len(allProducts)
print(count)
assert count > 0
productNames = []
# chaining methods in selenium
for product in allProducts:
    product.find_element(By.XPATH, "div/button").click()
    productNames.append(product.find_element(By.XPATH, 'h4').text)
print(productNames)
actualProductLists = ['Cucumber - 1 Kg', 'Beetroot - 1 Kg', 'Beans - 1 Kg', 'Raspberry - 1/4 Kg', 'Strawberry - 1/4 Kg']
productCount = len(actualProductLists)
assert actualProductLists == productNames
time.sleep(1)
driver.find_element(By.CLASS_NAME, "cart-icon").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, '.promoCode').send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, '.promoBtn').click()
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, '.promoInfo')))
print(driver.find_element(By.CLASS_NAME, 'promoInfo').text)
# summation of Products
Prices = driver.find_elements(By.XPATH, '//td[5]/p')
sum = 0
for price in Prices:
    sum = sum + int(price.text)
print("Actual Amount = "+str(sum))
totalAmount = int(driver.find_element(By.CSS_SELECTOR, ".totAmt").text)
assert sum == totalAmount
discountedAmount = float(driver.find_element(By.CLASS_NAME, "discountAmt").text)
print("Discounted Amount = "+str(discountedAmount))
assert discountedAmount < totalAmount
driver.close()