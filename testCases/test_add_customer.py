from time import sleep

from Configurations.readProperties import ReadConfig
from pageObjects.AddCustomerPage import AddCustomerPage
from pageObjects.CustomerListPage import CustomerListPage
from pageObjects.LoginPage import LoginPage


class Test_003_AddCustomers:
    baseURL = ReadConfig.get_application_url()
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()

    def test_add_customer(self, setup):
        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(self.baseURL)

        # login into the application. using already created loginpage
        self.lp = LoginPage(self.driver)
        self.lp.set_username(self.username)
        self.lp.set_password(self.password)
        self.lp.click_login()

        # now adding customer
        self.acp = AddCustomerPage(self.driver)
        self.acp.expand_customer_section()
        sleep(2)
        self.acp.navigate_to_customer_list_page()
        sleep(2)
        self.acp.click_add_customer_button()
        self.acp.enter_email_id("abc@gmail.com")
        self.acp.enter_password("abcd")
        self.acp.enter_first_name("Swapnil")
        self.acp.enter_last_name("Tomar")
        self.acp.select_gender_male()
        self.acp.enter_date_of_birth("12/04/1986")
        self.acp.enter_company("TCS")
        self.acp.select_if_tax_exempt()
        self.acp.select_customer_roles("Registered")
        self.acp.enter_vendor("Vendor1")
        self.acp.select_active()
        self.acp.enter_admin_comment("Adding swapnil as customer")
        self.acp.click_save_button()

        assert self.acp.actual_success_message() == "The new customer has been added successfully."

    def test_search_customer(self, setup):
        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(self.baseURL)

        # login into the application. using already created loginpage
        self.lp = LoginPage(self.driver)
        self.lp.set_username(self.username)
        self.lp.set_password(self.password)
        self.lp.click_login()

        self.acp = AddCustomerPage(self.driver)
        self.acp.expand_customer_section()
        sleep(2)
        self.acp.navigate_to_customer_list_page()
        sleep(2)

        self.clp = CustomerListPage(self.driver)
        self.clp.enter_email_id("abc@gmail.com")
        self.clp.click_search_button()
        sleep(2)
        status = self.clp.search_customer_by_email("abc@gmail.com")
        assert status == True
        # print(self.clp.search_customer_by_email("abc@gmail.com"))
