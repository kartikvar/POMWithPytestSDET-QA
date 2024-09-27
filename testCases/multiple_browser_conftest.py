import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service


@pytest.fixture()
def setup(browser):
    global driver
    if browser == "chrome":
        os.environ['WDM_SSL_VERIFY'] = '0'
        service = Service()
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(service=service, options=options)
    elif browser == "firefox":
        os.environ['WDM_SSL_VERIFY'] = '0'
        service = Service()
        options = webdriver.FirefoxOptions()
        options.add_argument("detach", True)
        driver = webdriver.Firefox(service=service, options=options)
    return driver


def pytest_addoption(parser):  # this will get value from CLI/hooks
    parser.addoption("--browser")


@pytest.fixture()  # this will return browser value to setup method
def browser(request):
    return request.config.getoption("--browser")


# fields to show in reports
def pytest_configure(config):
    config.metadata['Project Name'] = 'nop commerce'
    config.metadata['Module Name'] = 'Customers'
    config.metadata['Tester'] = 'Kartik'
