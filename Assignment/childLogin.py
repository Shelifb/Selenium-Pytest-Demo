import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

opt = Options()
opt.add_experimental_option('detach', True)
driver = webdriver.Chrome(service=ChromeService(), options=opt)
# driver.implicitly_wait(2)
driver.get('https://rahulshettyacademy.com/loginpagePractise/')
driver.maximize_window()
driver.find_element(By.LINK_TEXT, "Free Access to InterviewQues/ResumeAssistance/Material").click()
windows = driver.window_handles
driver.switch_to.window(windows[1])
email = driver.find_element(By.LINK_TEXT, "mentor@rahulshettyacademy.com").text
print(email)
driver.switch_to.window(windows[0])
driver.find_element(By.ID, "username").send_keys(email)
driver.find_element(By.ID, "password").send_keys("Test@123")
driver.find_element(By.ID, "terms").click()
driver.find_element(By.ID, "signInBtn").click()
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".alert-danger")))
error = driver.find_element(By.XPATH, "//div[contains(@class,'alert-danger')]").text
print(error)
driver.quit()

