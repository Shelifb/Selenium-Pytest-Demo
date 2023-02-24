
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By

opt = Options()
opt.add_experimental_option('detach', True)
driver = webdriver.Chrome(service=ChromeService(), options=opt)
driver.get('https://rahulshettyacademy.com/AutomationPractice//')
driver.maximize_window()

driver.find_element(By.NAME, "enter-name").send_keys("Test")
driver.find_element(By.ID, "alertbtn").click()
alert = driver.switch_to.alert
print(alert.text)
assert "Test" in alert.text
alert.accept()

driver.find_element(By.ID, "confirmbtn").click()
alt = driver.switch_to.alert
print(alt.text)
alt.dismiss()
driver.close()