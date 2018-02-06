from selenium import webdriver
from time import sleep
from Highlight import highlight_element

driver = webdriver.Chrome("chromedriver.exe")

driver.get("http://newtours.demoaut.com/")
driver.maximize_window()

'Login'

highlight_element(driver.find_element_by_xpath("//input[@name='userName']"))
sleep(2)
driver.find_element_by_xpath("//input[@name='userName']").send_keys("mercury")
driver.find_element_by_xpath("//input[@name='password']").send_keys("mercury")
driver.find_element_by_xpath("//input[@name='login']").click()

sleep(5)
driver.find_element_by_xpath("//a[text()='SIGN-OFF']").click()