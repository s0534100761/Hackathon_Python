import allure

import utilities
from extensions.UIActions import UIActions
from utilities.common_ops import CommonOps
from utilities.manage_pages import ManagePages


class WebWorkFlows:

    @staticmethod
    @allure.step("Login to RWA")
    def login():
        UIActions.send_keys_to_element(utilities.manage_pages.login_page.get_username_input(),
                                       CommonOps.get_data("UserName"))
        UIActions.send_keys_to_element(utilities.manage_pages.login_page.get_password_input(),
                                       CommonOps.get_data("Password"))
        UIActions.click_element(utilities.manage_pages.login_page.get_login_button())

    @staticmethod
    @allure.step("Login new user")
    def login_new_user():
        UIActions.send_keys_to_element(utilities.manage_pages.login_page.get_username_input(),
                                       CommonOps.get_data("NewUserName"))
        UIActions.send_keys_to_element(utilities.manage_pages.login_page.get_password_input(),
                                       CommonOps.get_data("NewUserPassword"))
        UIActions.click_element(utilities.manage_pages.login_page.get_login_button())

    @staticmethod
    @allure.step("Sign up new user")
    def sign_up():
        UIActions.click_element(utilities.manage_pages.login_page.get_signup_button())
        UIActions.click_element(utilities.manage_pages.login_page.get_signup_button())
        UIActions.send_keys_to_element(utilities.manage_pages.signup_form.get_first_name_input(),
                                       CommonOps.get_data("NewUserFirstName"))
        UIActions.send_keys_to_element(utilities.manage_pages.signup_form.get_last_name_input(),
                                       CommonOps.get_data("NewUserLastName"))
        UIActions.send_keys_to_element(utilities.manage_pages.signup_form.get_username_input(),
                                       CommonOps.get_data("NewUserName"))
        UIActions.send_keys_to_element(utilities.manage_pages.signup_form.get_password_input(),
                                       CommonOps.get_data("NewUserPassword"))
        UIActions.send_keys_to_element(utilities.manage_pages.signup_form.get_confirm_password_input(),
                                       CommonOps.get_data("NewUserPassword"))
        UIActions.click_element(utilities.manage_pages.signup_form.get_signup_button())

    @staticmethod
    @allure.step("First login after sign up")
    def after_first_sign_up():
        UIActions.click_element(utilities.manage_pages.home_page.get_signup_next_button())
        UIActions.send_keys_to_element(utilities.manage_pages.home_page.get_signup_bank_acc_input(),
                                       CommonOps.get_data("NewUserBankAccount"))
        UIActions.send_keys_to_element(utilities.manage_pages.home_page.get_routing_number_input(),
                                       CommonOps.get_data("NewUserRoutingNumber"))
        UIActions.send_keys_to_element(utilities.manage_pages.home_page.get_account_number_input(),
                                       CommonOps.get_data("NewUserAccountNumber"))
        UIActions.click_element(utilities.manage_pages.home_page.get_save_button())
        UIActions.click_element(utilities.manage_pages.home_page.get_done_button())

    @staticmethod
    @allure.step("Logout RWA")
    def logout():
        UIActions.click_element(utilities.manage_pages.home_page.get_logout_button())

    @staticmethod
    @allure.step("Money transactions")
    def make_transaction():
        UIActions.click_element(utilities.manage_pages.home_page.get_transaction_button())
        UIActions.click_element(utilities.manage_pages.transactions_page.get_users()[1])
        UIActions.send_keys_to_element(utilities.manage_pages.transactions_page.get_amount_input(),
                                       CommonOps.get_data("Amount"))
        UIActions.send_keys_to_element(utilities.manage_pages.transactions_page.get_description_input(),
                                       CommonOps.get_data("Note"))
        UIActions.click_element(utilities.manage_pages.transactions_page.get_pay_button())
        UIActions.click_element(utilities.manage_pages.transactions_page.get_return_to_transactions_button())
        UIActions.click_element(utilities.manage_pages.transactions_page.get_transactions_list()[0])

    @staticmethod
    @allure.step("Bank account cration")
    def create_bank_account():
        UIActions.click_element(utilities.manage_pages.home_page.get_bank_accounts_button())
        UIActions.click_element(utilities.manage_pages.bank_account_page.get_create_button())
        UIActions.send_keys_to_element(utilities.manage_pages.bank_account_page.get_bank_name_input(),
                                       CommonOps.get_data("NewUserBankAccount"))
        UIActions.send_keys_to_element(utilities.manage_pages.bank_account_page.get_bank_routing_number_input(),
                                       CommonOps.get_data("NewUserRoutingNumber"))
        UIActions.send_keys_to_element(utilities.manage_pages.bank_account_page.get_account_number_input(),
                                       CommonOps.get_data("NewUserAccountNumber"))
        UIActions.click_element(utilities.manage_pages.bank_account_page.get_save_button())

    @staticmethod
    @allure.step("Navigate to notfications")
    def navigate_to_notifications():
        UIActions.click_element(utilities.manage_pages.home_page.get_notification_button())

    @staticmethod
    @allure.step("Delete notification")
    def delete_notification():
        UIActions.click_element(utilities.manage_pages.notifications_page.get_notification_dismiss_button())