import os

import pytest
from applitools.selenium import Eyes
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from utilities.common_ops import CommonOps
from utilities.event_listener import EventListener
from utilities.manage_db import ManageDB
from utilities.manage_pages import ManagePages

driver = None
action = None
eyes = Eyes()
desired_capabilities = {}

# API
url_api = None
header = None

# xml files paths.
get_data_path = None


@pytest.fixture(scope='class')
def init_web(request):
    browser_type = os.getenv("BrowserType")
    if browser_type.lower() == "chrome":
        e_driver = webdriver.Chrome(ChromeDriverManager().install())
    elif browser_type.lower == "firefox":
        e_driver = webdriver.Firefox(GeckoDriverManager().install())
    elif browser_type.lower == "edge":
        e_driver = webdriver.Edge(EdgeChromiumDriverManager().install())
    else:
        raise Exception("Wrong browser type")

    driver = EventFiringWebDriver(e_driver, EventListener())
    driver.maximize_window()

    globals()['driver'] = driver
    globals()['get_data_path'] = "C:/Automation/Python/hackathon/files/Web_User_to_test.xml"
    globals()['action'] = ActionChains(driver)
    eyes.api_key = CommonOps.get_data("AppliToolsAPIKey")

    # request
    request.cls.eyes = eyes
    request.cls.driver = driver
    driver.implicitly_wait(5)

    ManagePages.init_web_pages(driver)

    yield
    eyes.close()
    driver.quit()
    eyes.abort()


@pytest.fixture(scope='class')
def init_appium(request):
    globals()['get_data_path'] = "C:/Automation/Python/hackathon/files/mobile_data.xml"
    desired_capabilities['reportDirectory'] = CommonOps.get_data("reportDirectory")
    desired_capabilities['reportFormat'] = CommonOps.get_data("reportFormat")
    desired_capabilities['testName'] = CommonOps.get_data("testName")
    desired_capabilities['uuid'] = CommonOps.get_data("uuid")
    desired_capabilities['appPackage'] = CommonOps.get_data("appPackage")
    desired_capabilities['appActivity'] = CommonOps.get_data("appActivity")
    desired_capabilities['platformName'] = CommonOps.get_data("platformName")
    e_driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_capabilities)
    driver = EventFiringWebDriver(e_driver, EventListener())
    globals()['driver'] = driver

    request.cls.driver = driver
    driver.implicitly_wait(5)
    ManagePages.init_mobile_pages(driver)

    yield
    driver.quit()


@pytest.fixture(scope='class')
def init_desktop(request):
    desired_capabilities["app"] = "Microsoft.WindowsCalculator_8wekyb3d8bbwe!App"
    desired_capabilities["platformName"] = "Windows"
    desired_capabilities["deviceName"] = "WindowsPC"
    e_driver = webdriver.Remote("http://127.0.0.1:4723", desired_capabilities)
    driver = EventFiringWebDriver(e_driver, EventListener())
    globals()['driver'] = driver
    globals()['get_data_path'] = "C:/Automation/Python/hackathon/files/calc_db_query.xml"

    request.cls.driver = driver

    driver.implicitly_wait(5)

    ManagePages.init_desktop_pages(driver)
    ManageDB.setup_db_connection()

    yield
    driver.quit()
    ManageDB.close_connection()


@pytest.fixture(scope="class")
def init_api():
    globals()['get_data_path'] = "C:/Automation/Python/hackathon/files/api_parameters.xml"
    globals()['url_api'] = CommonOps.get_data("ApiURL")
    globals()['header'] = {'Content-type': 'application/json'}


@pytest.fixture(scope='class')
def init_electron(request):
    globals()['get_data_path'] = "C:/Automation/Python/hackathon/files/parameters_electron.xml"
    options = webdriver.ChromeOptions()
    options.binary_location = CommonOps.get_data('Electron_App')
    e_driver = webdriver.Chrome(chrome_options=options, executable_path=CommonOps.get_data('Electron_Driver'))
    driver = EventFiringWebDriver(e_driver, EventListener())
    globals()['driver'] = driver
    request.cls.driver = driver

    ManagePages.init_electron_pages(driver)

    yield
    driver.quit()



