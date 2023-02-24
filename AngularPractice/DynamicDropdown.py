import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By

opt = Options()
opt.add_experimental_option('detach', True)
driver = webdriver.Chrome(service=ChromeService(), options=opt)
driver.get('https://www.goibibo.com/')
driver.maximize_window()
time.sleep(3)
driver.find_element(By.CLASS_NAME, 'login__tab_wrapper').click()




