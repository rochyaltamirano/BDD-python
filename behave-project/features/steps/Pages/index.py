from selenium.webdriver.common.by import By


class Index:
    def __init__(self, driver):
        self.driver = driver
        self.dresses_button = (By.PATH, '//*[@id="block_top_menu"]/ul/li[2]/a')

    def click_dresses(self):
        self.driver.find_element(*self.dresses_button).click()


