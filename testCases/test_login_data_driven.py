import os
from time import sleep

import pytest

from Configurations.readProperties import ReadConfig
from pageObjects.LoginPage import LoginPage
from utilities import ExcelUtility
from utilities.custom_logger import LogGeneration


class Test_002_Login_Data_Driven:
    baseURL = ReadConfig.get_application_url()
    path = ".\\TestData\\LoginData.xlsx"
    log = LogGeneration.logging()

    def test_login(self, setup):
        self.log.info("****************** Test login test Test_002_Login_Data_Driven *******************")
        self.log.info("****************** Verify login test *******************")
        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)

        self.total_rows = ExcelUtility.getRowCount(self.path, "Sheet1")
        print("Number of rows is {}".format(self.total_rows))
        self.total_columns = ExcelUtility.getColumnCount(self.path, "Sheet1")
        print("Number of columns is {}".format(self.total_columns))

        list_status = []
        for i in range(2, self.total_rows + 1):
            self.username = ExcelUtility.readDataFromExcel(self.path, "Sheet1", i, 1)
            self.password = ExcelUtility.readDataFromExcel(self.path, "Sheet1", i, 2)

            self.lp.set_username(self.username)
            self.lp.set_password(self.password)
            self.lp.click_login()
            sleep(5)
            actual_title = self.driver.title
            expected_title = "Dashboard / nopCommerce administration"

            if actual_title == expected_title:
                self.log.info("Passed")
                self.lp.click_logout()
                list_status.append("Pass")
            elif actual_title != expected_title:
                self.log.info("Failed")
                self.lp.click_logout()
                list_status.append("Fail")

            if "Fail" not in list_status:
                self.log.info("************* Test_002_Login_Data_Driven is passed ************")
                self.driver.close()
                assert True
            else:
                self.log.info("************* Test_002_Login_Data_Driven is failed ************")
                self.driver.close()
                assert True
