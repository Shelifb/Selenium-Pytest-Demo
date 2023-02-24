# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
#
# service_obj = Service("C:\work\Chromedriver.exe");
# driver = webdriver.Chrome(service=service_obj)
# driver.get("https://google.com")
# driver.maximize_window()
# input('Execution completed, Press Enter: ')


# Detach Browser
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
#
#
# chrome_options = Options()
# chrome_options.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(options=chrome_options)
#
# driver.get('https://www.google.com')


# Selenium manager with detach option
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService

opt = Options()
opt.add_experimental_option('detach', True)
driver = webdriver.Chrome(service=ChromeService(), options=opt)
driver.get('https://rahulshettyacademy.com/')
driver.maximize_window()
print(driver.title)
print(driver.current_url)
driver.get('https://rahulshettyacademy.com/seleniumPractise/#/')
driver.back()
driver.refresh()
driver.forward()
# driver.close()
