class CalcMainPage:

    def __init__(self, driver):
        self.driver = driver

    def get_number(self, number):
        return self.driver.find_element_by_name(number)

    def get_math_sign(self, sign):
        return self.driver.find_element_by_name(sign)

    def get_result(self):
        return self.driver.find_element_by_xpath("//*[@AutomationId='CalculatorResults']")

    def get_clear_button(self):
        return self.driver.find_element_by_xpath("//*[@AutomationId='clearButton']")

    def get_result_text(self):
        result = self.get_result().text
        return result.replace("Display is", "").strip()