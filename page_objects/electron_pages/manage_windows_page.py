from selenium.webdriver.common.by import By


class ManageWindowsPage:

    def __init__(self, driver):
        self.driver = driver

    def get_btn_event(self):
        return self.driver.find_element(By.ID, "manage-window-demo-toggle")

    def get_btn_event_demo(self):
        return self.driver.find_element(By.ID, "manage-window")

    def get_txt_event_demo(self):
        return self.driver.find_element(By.ID, "manage-window-reply").text

    def get_div(self):
        return self.driver.find_element(By.XPATH, "//*[@id='windows-section']/div[2]/div")




