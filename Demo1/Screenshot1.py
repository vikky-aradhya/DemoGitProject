from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get("http://www.google.com/")
driver.maximize_window()
driver.implicitly_wait(10)

driver.get_screenshot_as_file("Screenshot.png")
sleep(5)

driver.close()
driver.quit()