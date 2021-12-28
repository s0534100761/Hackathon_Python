import pytest
import allure
from work_flows.api_work_flows import ApiWorkFlows
from extensions import Verifications as verifications


@pytest.mark.usefixtures('init_api')
class Test_Cases_Api:

    @allure.title("Verify ID")
    @allure.description("This test checks whether the ID of the posts is equal to the ID sent")
    def test_01(self):
        flag = ApiWorkFlows.get_post_by_post_id()
        verifications.verify_true(flag)

    @allure.title("Verify post successfully")
    @allure.description("Verify the parameter is entered into the database")
    def test_02(self):
        status_code = ApiWorkFlows.post_params()
        verifications.verify_successful_post(status_code)

    @allure.title("Verify delete post")
    @allure.description("Verify the post is deleted")
    def test_03(self):
        response = ApiWorkFlows.delete_post()
        verifications.verify_successful_delete_post(response)