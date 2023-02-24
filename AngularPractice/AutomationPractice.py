
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By

opt = Options()
opt.add_experimental_option('detach', True)
driver = webdriver.Chrome(service=ChromeService(), options=opt)
driver.get('https://rahulshettyacademy.com/AutomationPractice//')
driver.maximize_window()

# checkboxes
all_elements = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
print(len(all_elements))
for item in all_elements:
    if item.get_attribute("value") == "option2":
        item.click()
        assert item.is_selected()
        break

# radio buttons
buttons = driver.find_elements(By.CLASS_NAME, "radioButton")
print(len(buttons))
buttons[2].click()
assert buttons[2].is_selected()

# hidden elements
hidden = driver.find_element(By.ID, "displayed-text")
assert hidden.is_displayed()

driver.find_element(By.ID, "hide-textbox").click()
assert not hidden.is_displayed()
