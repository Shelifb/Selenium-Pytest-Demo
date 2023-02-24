from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
opt = Options()
opt.add_experimental_option('detach', True)
driver = webdriver.Chrome(service=ChromeService(), options=opt)
driver.get('https://rahulshettyacademy.com/angularpractice/')
driver.maximize_window()
# driver.find_element(By.NAME, "name").send_keys("Test")
driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("Test")
driver.find_element(By.NAME, "email").send_keys("Test@gmail.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("Test@123")
driver.find_element(By.CSS_SELECTOR, "input[value='option1']").click()
driver.find_element(By.ID, "exampleCheck1").click()
driver.find_element(By.CLASS_NAME, "btn-success").click()
message = driver.find_element(By.CLASS_NAME, "alert-success").text
print(message)
assert "Success" in message
driver.find_element(By.LINK_TEXT, "Shop").click()
print(driver.current_url)
print(driver.title)
driver.back()






