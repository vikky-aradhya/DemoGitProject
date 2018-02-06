import unittest
from selenium import webdriver
from time import sleep

class Login(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome("chromedriver.exe")
        cls.driver.get("http://newtours.demoaut.com/")
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)
    
    def test_1_login(self):
        self.driver.find_element_by_xpath("//input[@name='userName']").send_keys("mercury")
        self.driver.find_element_by_xpath("//input[@name='password']").send_keys("mercury")
        self.driver.find_element_by_xpath("//input[@name='login']").click()

        sleep(5)
        self.driver.find_element_by_xpath("//a[text()='SIGN-OFF']").click()
        
    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        

if __name__ == "__main__":
    unittest.main()