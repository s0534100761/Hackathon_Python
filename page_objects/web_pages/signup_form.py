from selenium.webdriver.common.by import By


class SignUpForm:

    def __init__(self, driver):
        self.driver = driver

    def get_first_name_input(self):
        return self.driver.find_element(By.XPATH, "//input[@id='firstName']")

    def get_last_name_input(self):
        return self.driver.find_element(By.XPATH, "//input[@id='lastName']")

    def get_username_input(self):
        return self.driver.find_element(By.XPATH, "//input[@id='username']")

    def get_password_input(self):
        return self.driver.find_element(By.XPATH, "//input[@id='password']")

    def get_confirm_password_input(self):
        return self.driver.find_element(By.XPATH, "//input[@id='confirmPassword']")

    def get_signup_button(self):
        return self.driver.find_element(By.XPATH, "//form/button")