from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service as ChromeService

opt = Options()
opt.add_experimental_option('detach', True)
driver = webdriver.Chrome(service=ChromeService())
driver.implicitly_wait(4)
driver.get('https://rahulshettyacademy.com/angularpractice/')
driver.maximize_window()
driver.find_element(By.LINK_TEXT, "Shop").click()
products = driver.find_elements(By.XPATH, "//div[@class='card h-100']")
prodName = []
for prod in products:
    prodName.append(prod.find_element(By.XPATH, "div/h4").text)
    heading = prod.find_element(By.XPATH, "div/h4").text
    if heading == "Blackberry":
        prod.find_element(By.XPATH, "//button[text()='Add ']").click()

print(prodName)
driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()
driver.find_element(By.XPATH, "//button[contains(@class,'btn-success')]").click()
driver.find_element(By.ID, "country").send_keys("ind")
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "suggestions")))
countries = driver.find_elements(By.CLASS_NAME, "suggestions")
for country in countries:
    country.find_element(By.LINK_TEXT, "India").click()
driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
print(driver.find_element(By.CLASS_NAME, "alert-success").text)
driver.close()



