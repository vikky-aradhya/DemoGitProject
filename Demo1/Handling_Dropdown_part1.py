import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from time import sleep


class Dropdown(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get("https://www.facebook.com/")
        cls.driver.implicitly_wait(10)
        
        
    def test_1_Dropdown_Day(self):
        select1 = Select(self.driver.find_element_by_xpath("//select[@id='day']"))
        select1.select_by_index(21)
        sleep(2)
        selected_day = select1.first_selected_option.get_attribute("value")
        print("Selected day is :", selected_day)
        
        
    def test_2_Dropdown_Month(self):
        select2 = Select(self.driver.find_element_by_xpath("//select[@id='month']"))
        select2.select_by_visible_text("Jun")
        sleep(2)
        selected_month = select2.first_selected_option.get_attribute("innerHTML")
        print("Selected month is :", selected_month)
        length = len(select2.options)
        print("length is :",length)
        values = self.driver.find_elements_by_xpath("//select[@id='month']/option")
        for value in values:
            print("Values in the drop down", value.get_attribute("value"))
        self.assertEqual(length, 14, "pass")
        
        
        
    def test_3_Dropdown_Year(self):
        select3 = Select(self.driver.find_element_by_xpath("//select[@id='year']"))
        select3.select_by_value("1990")
        sleep(2)
        selected_year = select3.first_selected_option.get_attribute("value")
        print("Selected year is :", selected_year)
        
        
    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        
if __name__ == "__main__":
    unittest.main()