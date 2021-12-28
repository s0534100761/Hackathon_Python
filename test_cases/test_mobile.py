import allure
import pytest

import utilities
from extensions import Verifications
from utilities.common_ops import CommonOps
from utilities.manage_pages import ManagePages
from work_flows.mobile_work_flows import MobileWorkFlows


@pytest.mark.usefixtures('init_appium')
class Test_Cases_Mobile:

    @allure.title("Test currency conversion")
    @allure.description("Verify currency conversions rate")
    def test_currency_conversion(self):
        MobileWorkFlows.conversion()

        Verifications.verify_text(utilities.manage_pages.currency_convertor_page.get_result().text,
                                  CommonOps.get_data("ExpectedResult"))

    @allure.title("Test compound interest")
    @allure.description("Verify compound interest added")
    @pytest.mark.parametrize(
        "principle_input, monthly_deposit_input, period_input, interest_rate_input",
        [
            ("90", "3", "2", "10"),
            ("25", "5", "4", "5"),
            ("17", "5", "9", "10")
        ]
    )
    def test_untitled(self, principle_input, monthly_deposit_input, period_input, interest_rate_input):
        MobileWorkFlows.navigate_back()
        MobileWorkFlows.compound_interest(principle_input, monthly_deposit_input, period_input, interest_rate_input)

        results = utilities.manage_pages.compound_interest_calc_page.get_results()
        Verifications.verify_text(str(len(results)), period_input)

        MobileWorkFlows.reset_compound_calc()