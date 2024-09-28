from selenium.webdriver.common.by import By


class AddCustomerPage:
    customer_expand_linktext = "//a[@href='#']/p[contains(text(),'Customers')]"
    customer_list_page_xpath = "//a[@href='/Admin/Customer/List']/p"
    customer_create_button_xpath = "//a[@href='/Admin/Customer/Create']"
    customer_email_id = "Email"
    customer_password_id = "Password"
    customer_first_name_id = "FirstName"
    customer_last_name_id = "LastName"
    customer_gender_male_id = "Gender_Male"
    customer_gender_female_id = "Gender_Female"
    customer_date_of_birth_id = "DateOfBirth"
    customer_company_id = "Company"
    customer_is_tax_exempt_id = "IsTaxExempt"
    customer_roles_xpath = "//span[@data-select2-id='12']/span/span/ul/li/input"
    customer_registered_role_xpath = "//li[@id='select2-SelectedCustomerRoleIds-result-mq11-3']"
    customer_vendor_id = "VendorId"
    customer_active_id = "Active"
    customer_admin_comment_id = "AdminComment"
    customer_save_button_xpath = "//button[@name='save']"
    customer_added_successfully_message_xpath = "//div[@class='alert alert-success alert-dismissable']"

    def __init__(self, driver):
        self.driver = driver

    def expand_customer_section(self):
        self.driver.find_element(By.XPATH, self.customer_expand_linktext).click()

    def navigate_to_customer_list_page(self):
        self.driver.find_element(By.XPATH, self.customer_list_page_xpath).click()

    def click_add_customer_button(self):
        self.driver.find_element(By.XPATH, self.customer_create_button_xpath).click()

    def enter_email_id(self, emailID):
        self.driver.find_element(By.ID, self.customer_email_id).send_keys(emailID)

    def enter_password(self, password):
        self.driver.find_element(By.ID, self.customer_password_id).send_keys(password)

    def enter_first_name(self, firstName):
        self.driver.find_element(By.ID, self.customer_first_name_id).send_keys(firstName)

    def enter_last_name(self, lastName):
        self.driver.find_element(By.ID, self.customer_last_name_id).send_keys(lastName)

    def select_gender_male(self):
        self.driver.find_element(By.ID, self.customer_gender_male_id).click()

    def select_gender_female(self):
        self.driver.find_element(By.ID, self.customer_gender_female_id).click()

    def enter_date_of_birth(self, dateOfBirth):
        self.driver.find_element(By.ID, self.customer_date_of_birth_id).send_keys(dateOfBirth)

    def enter_company(self, company):
        self.driver.find_element(By.ID, self.customer_company_id).send_keys(company)

    def select_if_tax_exempt(self):
        self.driver.find_element(By.ID, self.customer_is_tax_exempt_id).click()

    def select_customer_roles(self, customerRoles):
        self.driver.find_element(By.XPATH, self.customer_roles_xpath).send_keys(customerRoles)

    def enter_vendor(self, vendor):
        self.driver.find_element(By.ID, self.customer_vendor_id).send_keys(vendor)

    def select_active(self):
        self.driver.find_element(By.ID, self.customer_active_id).click()

    def enter_admin_comment(self, adminComment):
        self.driver.find_element(By.ID, self.customer_admin_comment_id).send_keys(adminComment)

    def click_save_button(self):
        self.driver.find_element(By.XPATH, self.customer_save_button_xpath).click()

    def actual_success_message(self):
        success_msg = self.driver.find_element(By.XPATH, self.customer_added_successfully_message_xpath).text
        return success_msg
