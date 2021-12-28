import allure
import utilities
from utilities.manage_pages import ManagePages
from extensions.UIActions import UIActions


class DesktopsWorkFlows:

    @staticmethod
    @allure.step("Calculator addtion")
    def addition(first_number, second_number, math_sign):
        UIActions.click_element(utilities.manage_pages.calc_main_page.get_number(first_number))
        UIActions.click_element(utilities.manage_pages.calc_main_page.get_math_sign(math_sign))
        UIActions.click_element(utilities.manage_pages.calc_main_page.get_number(second_number))
        UIActions.click_element(utilities.manage_pages.calc_main_page.get_math_sign("Equals"))