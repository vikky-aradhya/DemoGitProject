from selenium import webdriver
import unittest
from time import sleep

class Bootstrap(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get("https://getbootstrap.com/docs/4.0/components/dropdowns/")
        cls.driver.implicitly_wait(10)
     
    def test_1_Bootstrap_dropdown(self):
        "To Click on the Bootstrap dropdown"
        
        self.driver.find_element_by_xpath("//button[@id='dropdownMenuButton']").click()
        sleep(5)
        
        expvalue = "Action","Another action","Something else here"
        
        bootstrap = self.driver.find_elements_by_xpath("/html/body/div/div/main/div[2]/div/div/a")
        i = 0
        count = 0
        for text1 in bootstrap:
            actvalue = text1.text
            print(actvalue)
            count = count+1
            if(expvalue[i]==actvalue):
                i=i+1
        if(count==expvalue.__len__()):
            print("Dropdown values are matched")
        else:
            print("Dropdown values are not matched")
       
    
    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        
        
if __name__ == "__main__":
    unittest.main()