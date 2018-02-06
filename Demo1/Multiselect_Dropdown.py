from selenium import webdriver
import unittest
from selenium.webdriver.support.ui import Select
from time import sleep

class Multidropdown(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_select_multiple")
        cls.driver.implicitly_wait(10)
        
        
    def test_1_Multiselect_Dropdown(self):
        
        'Switch frame'
        self.driver.switch_to_frame("iframeResult")
        sleep(2)
        
        'storing drop down in one variable using xpath'
        Multi = Select(self.driver.find_element_by_xpath("//select[@name='cars']"))
        
        'Selecting values'
        Multi.select_by_index(0)
        sleep(2)
        Multi.select_by_value("opel")
        sleep(2)
        Multi.select_by_visible_text("Audi")
        sleep(2)
        
        'Verifying selected values'
        Selected_value = Multi.all_selected_options
        for elements in Selected_value:
            print("Selected values are:", elements.get_attribute("value"))
        
        "let's deselect all values"
        sleep(2)
        Multi.deselect_all()
        
        
@classmethod
def tearDownClass(cls):
    cls.driver.close()
    cls.driver.quit()
            
if __name__ == "__main__":
    unittest.main()
        
        