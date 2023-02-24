from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
# chrome options
opt = Options()
opt.add_experimental_option('detach', True)
opt.add_argument("headless")
# opt.add_argument("--ignore-certificate-errors")
driver = webdriver.Chrome(service=ChromeService(), options=opt)
driver.get('https://rahulshettyacademy.com/AutomationPractice//')
driver.maximize_window()
driver.execute_script("window.scrollBy(0,500)")
# driver.execute_script("Window.scrollBy(0,document.body.scrollHeight);")
driver.get_screenshot_as_file("screen.png")
