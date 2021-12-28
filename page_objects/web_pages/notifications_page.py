from selenium.webdriver.common.by import By


class Notifications:

    def __init__(self, driver):
        self.driver = driver

    def get_notifications_list(self):
        return self.driver.find_elements(By.XPATH, "//ul[@data-test='notifications-list']//li")

    def get_notification_dismiss_button(self):
        first_notification = self.get_notifications_list()[0]
        return first_notification.find_element(By.TAG_NAME, "button")