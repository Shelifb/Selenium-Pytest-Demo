# import action as action
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By

opt = Options()
opt.add_experimental_option('detach', True)
driver = webdriver.Chrome(service=ChromeService(), options=opt)
driver.get('https://rahulshettyacademy.com/AutomationPractice//')
driver.maximize_window()

action = ActionChains(driver)
# action.click_and_hold()
# action.context_click()
# action.double_click(driver.find_element(By.ID, " "))
driver.execute_script("window.scrollTo(0, 900)")

action.move_to_element(driver.find_element(By.ID, "mousehover")).perform()
top = driver.find_element(By.XPATH, "//div[@class='mouse-hover-content']/a")
assert top.is_displayed()
action.context_click(driver.find_element(By.LINK_TEXT, "Top")).perform()
action.context_click(driver.find_element(By.LINK_TEXT, "Top")).click().perform()
