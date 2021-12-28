import allure
import pytest

import utilities
from extensions import Verifications
from utilities.manage_db import ManageDB
from utilities.manage_pages import ManagePages
from work_flows.desktop_work_flows import DesktopsWorkFlows


@pytest.mark.usefixtures('init_desktop')
class Test_Cases_Desktop:

    @allure.title("Test Calculator addition")
    @allure.description("Verify result after addition")
    def test_addition(self):
        DesktopsWorkFlows.addition(ManageDB.get_db_data()[0][0], ManageDB.get_db_data()[0][1],
                                   ManageDB.get_db_data()[0][2])
        Verifications.verify_text(utilities.manage_pages.calc_main_page.get_result_text(), ManageDB.get_db_data()[0][3])