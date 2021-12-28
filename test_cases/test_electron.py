import allure
import pytest

from extensions import Verifications as verifications
from work_flows.electron_work_flow import ElectronWorkFlow


@pytest.mark.usefixtures('init_electron')
class Test_Cases_Electron:
    @allure.title("Verify Resize")
    @allure.description("This test verify resize successfully")
    def test_01(self):
        result = ElectronWorkFlow.window_event()
        verifications.verify_not_equals(result)

    @allure.title("Verify Tray")
    @allure.description("This test checks whether the text is displayed")
    def test_02(self):
        txt_result, expected = ElectronWorkFlow.get_text()
        verifications.verify_text(txt_result, expected)


