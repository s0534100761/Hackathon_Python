from selenium.webdriver.common.by import By


class BankAccount:

    def __init__(self, driver):
        self.driver = driver

    def get_create_button(self):
        return self.driver.find_element(By.XPATH, "//a[@data-test='bankaccount-new']")

    def get_bank_name_input(self):
        return self.driver.find_element(By.XPATH, "//input[@name='bankName']")

    def get_bank_routing_number_input(self):
        return self.driver.find_element(By.XPATH, "//input[@name='routingNumber']")

    def get_account_number_input(self):
        return self.driver.find_element(By.XPATH, "//input[@name='accountNumber']")

    def get_save_button(self):
        return self.driver.find_element(By.XPATH, "//button[@data-test='bankaccount-submit']")

    def get_banks_list(self):
        return self.driver.find_elements(By.XPATH, "//ul[@data-test='bankaccount-list']//li")

    def get_last_bank(self):
        list_len = len(self.get_banks_list())
        last_elem = self.get_banks_list()[list_len - 1]
        return last_elem.find_element(By.TAG_NAME, "p")