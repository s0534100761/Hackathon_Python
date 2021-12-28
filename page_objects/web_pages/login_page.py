from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    def get_username_input(self):
        return self.driver.find_element(By.XPATH, "//input[@id='username']")

    def get_password_input(self):
        return self.driver.find_element(By.XPATH, "//input[@id='password']")

    def get_login_button(self):
        return self.driver.find_element(By.XPATH, "//form/button")

    def get_signup_button(self):
        return self.driver.find_element(By.PARTIAL_LINK_TEXT, "Don't have an account")