import allure


class UIActions:

    @staticmethod
    @allure.step("Send keys to element.")
    def send_keys_to_element(web_element, value):
        web_element.send_keys(value)

    @staticmethod
    @allure.step("Click element")
    def click_element(element):
        element.click()


