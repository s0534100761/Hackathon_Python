from selenium.webdriver.common.by import By


class TrayPage:
    def __init__(self, driver):
        self.driver = driver

    def get_btn_another_app(self):
        return self.driver.find_element(By.ID, "tray-demo-toggle")

    def get_btn_demo(self):
        return self.driver.find_element(By.ID, "put-in-tray")

    def get_div(self):
        return self.driver.find_element(By.XPATH, "//*[@id='tray-section']/div/div")

    def get_txt_demo(self):
        return self.driver.find_element(By.ID, "tray-countdown").text
