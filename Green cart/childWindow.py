from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By

opt = Options()
opt.add_experimental_option('detach', True)
driver = webdriver.Chrome(service=ChromeService(), options=opt)
# driver.implicitly_wait(2)
driver.get('https://the-internet.herokuapp.com/windows')
driver.maximize_window()
driver.find_element(By.LINK_TEXT, "Click Here").click()
windows = driver.window_handles
driver.switch_to.window(windows[1])
print(driver.find_element(By.TAG_NAME, "h3").text)
driver.switch_to.window(windows[0])
print(driver.find_element(By.TAG_NAME, "h3").text)
assert "Opening a new window" == driver.find_element(By.TAG_NAME, "h3").text
