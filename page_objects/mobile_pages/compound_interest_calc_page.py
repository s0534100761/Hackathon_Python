class CompoundInterestCalc:

    def __init__(self, driver):
        self.driver = driver

    def get_app(self):
        return self.driver.find_element_by_xpath("//*[@text='Compound Interest Calculator']")

    def get_principle_input(self):
        return self.driver.find_element_by_xpath("//*[@id='principleInput']")

    def get_monthly_deposit_input(self):
        return self.driver.find_element_by_xpath("//*[@id='monthlyDepositInput']")

    def get_period_month_input(self):
        return self.driver.find_element_by_xpath("//*[@id='periodInput']")

    def get_annual_interest_rate(self):
        return self.driver.find_element_by_xpath("//*[@id='interestRateInput']")

    def get_calc_button(self):
        return self.driver.find_element_by_xpath("//*[@id='calc']")

    def get_interest_table(self):
        return self.driver.find_element_by_xpath("//*[@id='interestTable']")

    def get_results(self):
        return self.driver.find_elements_by_xpath(
            "//*[@id='listview']/*/*[@class='android.widget.LinearLayout' and ./*[@id='text1']]")

    def get_navigation(self):
        return self.driver.find_element_by_xpath("//*[@contentDescription='נווט למעלה']")

    def get_reset(self):
        return self.driver.find_element_by_xpath("//*[@text='RESET']")