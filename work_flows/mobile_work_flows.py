import allure

import utilities
from extensions.UIActions import UIActions
from utilities.manage_pages import ManagePages


class MobileWorkFlows:

    @staticmethod
    @allure.step("Currency Conversion")
    def conversion():
        UIActions.click_element(utilities.manage_pages.currency_convertor_page.get_convertor())
        UIActions.click_element(utilities.manage_pages.currency_convertor_page.get_currency_spinner_from())
        UIActions.click_element(utilities.manage_pages.currency_convertor_page.get_israeli_shekel())
        UIActions.click_element(utilities.manage_pages.currency_convertor_page.get_currency_spinner_to())
        UIActions.click_element(utilities.manage_pages.currency_convertor_page.get_usd())
        UIActions.send_keys_to_element(utilities.manage_pages.currency_convertor_page.get_rate_input(), 25)
        UIActions.send_keys_to_element(utilities.manage_pages.currency_convertor_page.get_amount_input(), 5)

    @staticmethod
    @allure.step("Check compound")
    def compound_interest(principle_input, monthly_deposit_input, period_input, interest_rate_input):
        UIActions.click_element(utilities.manage_pages.compound_interest_calc_page.get_app())
        UIActions.send_keys_to_element(utilities.manage_pages.compound_interest_calc_page.get_principle_input(),
                                       principle_input)
        UIActions.send_keys_to_element(utilities.manage_pages.compound_interest_calc_page.get_monthly_deposit_input(),
                                       monthly_deposit_input)
        UIActions.send_keys_to_element(utilities.manage_pages.compound_interest_calc_page.get_period_month_input(),
                                       period_input)
        UIActions.send_keys_to_element(utilities.manage_pages.compound_interest_calc_page.get_annual_interest_rate(),
                                       interest_rate_input)
        UIActions.click_element(utilities.manage_pages.compound_interest_calc_page.get_calc_button())
        UIActions.click_element(utilities.manage_pages.compound_interest_calc_page.get_interest_table())

    @staticmethod
    @allure.step("Reset compound app")
    def reset_compound_calc():
        UIActions.click_element(utilities.manage_pages.compound_interest_calc_page.get_navigation())
        UIActions.click_element(utilities.manage_pages.compound_interest_calc_page.get_reset())

    @staticmethod
    @allure.step("Go to app home screen")
    def navigate_back():
        UIActions.click_element(utilities.manage_pages.compound_interest_calc_page.get_navigation())