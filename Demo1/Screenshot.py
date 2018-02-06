from selenium import webdriver
from time import sleep
import unittest
from Capture_Screenshot import SS

class screenshot(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get("http://www.google.com/")
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)
    
    def test_1_Screenshot(self):
        ss = SS(self.driver)
        ss.Screenshot("Screenshot.png")
        
    @classmethod
    def tearDownClass(cls):        
        cls.driver.close()
        cls.driver.quit()
        
if __name__ == "__main__":
    unittest.main()