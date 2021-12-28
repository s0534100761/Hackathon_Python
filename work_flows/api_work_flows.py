import allure
from extensions.APIActions import APIActions
from utilities.common_ops import CommonOps as common
import test_cases.conftest


class ApiWorkFlows:
    @staticmethod
    @allure.step("Returns a list of posts by ID")
    def get_post_by_post_id():
        number = common.get_data('Number_Get_Api')
        value = common.get_data('Value_Get_Api')
        response_json = APIActions.get_server(test_cases.conftest.url_api, value + str(number) + "/comments")
        flag = True
        for item in response_json:
            if str(item["postId"]) != number:
                flag = False
        return flag

    @staticmethod
    @allure.step("Post new post")
    def post_params():
        value = common.get_data('Value_Get_Api')
        params = ApiWorkFlows.init_params_post()
        response = APIActions.post_params(test_cases.conftest.url_api, value, params)
        return response

    @staticmethod
    @allure.step("Delete post")
    def delete_post():
        value = common.get_data('Value_Get_Api')
        id = common.get_data('Id_Delete')
        if ApiWorkFlows.filter_post_by_id(id) != []:
            APIActions.delete_post(test_cases.conftest.url_api, value, id)
            return ApiWorkFlows.filter_post_by_id(id)
        else:
            return ""

    @staticmethod
    @allure.step("Filter post by ID")
    def filter_post_by_id(id):
        value = common.get_data('Url_Filter')
        response = APIActions.get_server(test_cases.conftest.url_api, value + id)
        return response

    @staticmethod
    @allure.step("Initializes a parameter for the post")
    def init_params_post():
        params = {}
        params["postId"] = common.get_data("User_Id_Post")
        params["id"] = common.get_data("Id_Post")
        params["title"] = common.get_data("Title_Post")
        params["body"] = common.get_data("Body_Post")
        return params


