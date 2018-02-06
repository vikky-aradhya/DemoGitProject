class SS(object):
    def __init__(self,driver):
        self.driver = driver
        
    def Screenshot(self, path):
        directory = "C:\\Users\\vikky\\eclipse-workspace\\Demo1\\Screenshot\\"
        self.driver.get_screenshot_as_file(directory+path)