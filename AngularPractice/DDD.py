import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By

opt = Options()
opt.add_experimental_option('detach', True)
driver = webdriver.Chrome(service=ChromeService(), options=opt)
driver.get('https://rahulshettyacademy.com/dropdownsPractise/')
driver.maximize_window()
driver.find_element(By.ID, "autosuggest").send_keys("ind")
time.sleep(2)
countries = driver.find_elements(By.CSS_SELECTOR, "li[class='ui-menu-item'] a")
print(len(countries))
for country in countries:
    if country.text == "India":
        country.click()
        break
country = driver.find_element(By.ID, "autosuggest").get_attribute("value")
print(country)
assert "India" in country



