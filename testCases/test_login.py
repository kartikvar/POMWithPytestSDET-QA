import os
import pytest

from Configurations.readProperties import ReadConfig
from pageObjects.LoginPage import LoginPage
from utilities.custom_logger import LogGeneration


class Test_001_Login:
    baseURL = ReadConfig.get_application_url()
    print("URL is {}".format(baseURL))
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()
    log = LogGeneration.logging()

    def test_homepage_title(self, setup):
        self.log.info("****************** Test_001_Login *******************")
        self.log.info("****************** Verify home page title *******************")
        self.driver = setup
        print("URL is {}".format(self.baseURL))
        self.driver.maximize_window()
        self.driver.get(self.baseURL)
        actual_title = self.driver.title
        self.driver.close()
        if actual_title == "Your store. Login":
            assert True
            self.log.info("****************** Login test case passed *******************")
        else:
            self.log.error("****************** Login test case failed *******************")
            assert False

    def test_login(self, setup):
        self.log.info("****************** Verify login test *******************")
        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.set_username(self.username)
        self.lp.set_password(self.password)
        self.lp.click_login()
        actual_title = self.driver.title
        if actual_title == "Dashboard / nopCommerce administration":
            assert True
            self.driver.close()
            self.log.info("****************** Login test case passed *******************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
            self.driver.close()
            self.log.error("****************** Login test case failed *******************")
            assert False
