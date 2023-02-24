import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By

opt = Options()
opt.add_experimental_option('detach', True)
driver = webdriver.Chrome(service=ChromeService(), options=opt)
driver.get('https://rahulshettyacademy.com/seleniumPractise/')
driver.maximize_window()

empty = []

driver.find_element(By.CLASS_NAME, "search-keyword").send_keys("be")
time.sleep(2)
veggies = driver.find_elements(By.CSS_SELECTOR, "h4")
print(len(veggies))

for i in veggies:
    i.find_element(By.XPATH, "//button[text()='ADD TO CART']").click()

driver.find_element(By.CLASS_NAME, "cart-icon").click()
driver.find_element(By.XPATH, "//div[@class='action-block']/button").click()

# driver.find_element(By.XPATH, "//b[text()='Product Name']")
vegWebElements = driver.find_elements(By.CLASS_NAME, "product-name")
sorted = vegWebElements.copy()
for veg in sorted:
    empty.append(veg.text)
empty.sort()

