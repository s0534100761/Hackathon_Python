from selenium.webdriver.common.by import By


class TransactionsPage:

    def __init__(self, driver):
        self.driver = driver

    def get_users(self):
        return self.driver.find_elements(By.XPATH, "//ul[@data-test='users-list']//li")

    def get_amount_input(self):
        return self.driver.find_element(By.XPATH, "//input[@id='amount']")

    def get_description_input(self):
        return self.driver.find_element(By.XPATH, "//input[@name='description']")

    def get_pay_button(self):
        return self.driver.find_element(By.XPATH, "//button[@data-test='transaction-create-submit-payment']")

    def get_return_to_transactions_button(self):
        return self.driver.find_element(By.XPATH, "//a[@data-test='new-transaction-return-to-transactions']")

    def get_transactions_list(self):
        return self.driver.find_elements(By.XPATH, "//div[@data-test='transaction-list']/div/div/div")

    def get_transaction_amount(self):
        return self.driver.find_element(By.XPATH, "//div[@class='MuiGrid-root MuiGrid-item']//span[contains(@class, 'makeStyles-amountNegative')]")