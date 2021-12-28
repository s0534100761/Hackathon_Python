import time

import allure

import utilities
from extensions.UIActions import UIActions
from test_cases import conftest
from utilities.manage_pages import ManagePages


class ElectronWorkFlow:
    @staticmethod
    @allure.step("Resize window flow")
    def window_event():
        UIActions.click_element(utilities.manage_pages.electron_menu_page.get_btn_windows())
        ElectronWorkFlow.btn_open(utilities.manage_pages.manage_windows_page.get_div(),
                                  utilities.manage_pages.manage_windows_page.get_btn_event())
        handle_original = conftest.driver.current_window_handle
        UIActions.click_element(utilities.manage_pages.manage_windows_page.get_btn_event_demo())
        time.sleep(3)
        win_handles = conftest.driver.window_handles
        for win_handle in win_handles:
            conftest.driver.switch_to.window(win_handle)
            conftest.driver.execute_script("require('electron').remote.BrowserWindow.getFocusedWindow().maximize();")
        conftest.driver.switch_to.window(handle_original)
        txt_demo = utilities.manage_pages.manage_windows_page.get_txt_event_demo()
        return txt_demo

    @staticmethod
    @allure.step("Display text")
    def get_text():
        UIActions.click_element(utilities.manage_pages.electron_menu_page.get_btn_tray())
        ElectronWorkFlow.btn_open(utilities.manage_pages.tray_page.get_div(),
                                  utilities.manage_pages.tray_page.get_btn_another_app())
        UIActions.click_element(utilities.manage_pages.tray_page.get_btn_demo())
        txt_demo = utilities.manage_pages.tray_page.get_txt_demo()
        return txt_demo, "Click demo again to remove."

    @staticmethod
    @allure.step("Checks if the window is open")
    def btn_open(element_class, element_click):
        if "is-open" in element_class.get_attribute('class'):
            pass
        else:
            UIActions.click_element(element_click)










