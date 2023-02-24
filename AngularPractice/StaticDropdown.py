from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

opt = Options()
opt.add_experimental_option('detach', True)
driver = webdriver.Chrome(service=ChromeService(), options=opt)
driver.get('https://rahulshettyacademy.com/angularpractice/#')
driver.maximize_window()
dropdown = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
dropdown.select_by_index(1)
# dropdown.select_by_visible_text('Male')
# dropdown.select_by_value(())
option = dropdown.first_selected_option
print(option.text)

