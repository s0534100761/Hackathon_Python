import allure


@allure.step("Verify two given strings")
def verify_text(actual_text, expected_text):
    assert actual_text == expected_text


@allure.step("Verify flag true")
def verify_true(flag):
    assert flag


@allure.step("Verify post added")
def verify_successful_post(status_code):
    assert status_code == 201


@allure.step("Verify post deleted")
def verify_successful_delete_post(actual):
    assert actual == [], "Number in the post does not exist"


@allure.step("Verify two given strings")
def verify_not_equals(actual_text):
    assert actual_text != ''
