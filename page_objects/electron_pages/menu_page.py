from selenium.webdriver.common.by import By


class MenuPage:
    def __init__(self, driver):
        self.driver = driver

    def get_btn_windows(self):
        return self.driver.find_element(By.ID, "button-windows")

    def get_btn_tray(self):
        return self.driver.find_element(By.ID, "button-tray")