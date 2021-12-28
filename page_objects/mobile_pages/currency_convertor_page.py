class CurrencyConvertorPage:

    def __init__(self, driver):
        self.driver = driver

    def get_convertor(self):
        return self.driver.find_element_by_xpath("//*[@text='Currency Converter']")

    def get_currency_spinner_from(self):
        return self.driver.find_element_by_xpath("//*[@id='fromCurrencySpinner']")

    def get_israeli_shekel(self):
        return self.driver.find_element_by_xpath("//*[@text='Israeli Shekel:ILS']")

    def get_currency_spinner_to(self):
        return self.driver.find_element_by_xpath("//*[@id='ToCurrencySpinner']")

    def get_usd(self):
        return self.driver.find_element_by_xpath("//*[@text='U.S. Dollar:USD']")

    def get_rate_input(self):
        return self.driver.find_element_by_xpath("//*[@id='exchRateInput']")

    def get_amount_input(self):
        return self.driver.find_element_by_xpath("//*[@id='amountInput']")

    def get_result(self):
        return self.driver.find_element_by_xpath("//*[@id='converterResult']")