from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

opt = Options()
opt.add_experimental_option('detach', True)
driver = webdriver.Chrome(service=ChromeService(), options=opt)
# driver.implicitly_wait(2)
# driver.get('https://the-internet.herokuapp.com/')
# driver.maximize_window()
# driver.find_element(By.LINK_TEXT, "Frames").click()
# print(driver.current_url)
# wait = WebDriverWait(driver, 10)
# wait.until(expected_conditions.title_contains("Frame"))
# driver.find_element(By.LINK_TEXT, "iFrames").click()

driver.get('https://the-internet.herokuapp.com/iframe')
driver.maximize_window()
driver.switch_to.frame("mce_0_ifr")
driver.find_element(By.ID, "tinymce").clear()
driver.find_element(By.ID, "tinymce").send_keys("Working with frames")
driver.switch_to.default_content()
heading = driver.find_element(By.CSS_SELECTOR, "h3").text
print(heading)
assert "iFrame" in heading

