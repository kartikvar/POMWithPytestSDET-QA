from selenium.webdriver.common.by import By


class CustomerListPage:

    search_by_email_id = "SearchEmail"
    click_search_button_id = "search-customers"
    table_search_result_id = "customers-grid"
    table_row_xpath = "//table[@id='customers-grid']/tbody/tr"
    table_column_xpath = "//table[@id='customers-grid']/tbody/tr/td"

    def __init__(self, driver):
        self.driver = driver

    def enter_email_id(self, emailID):
        self.driver.find_element(By.ID, self.search_by_email_id).send_keys(emailID)

    def click_search_button(self):
        self.driver.find_element(By.ID, self.click_search_button_id).click()

    def get_total_rows(self):
        return len(self.driver.find_element(By.XPATH, self.table_row_xpath))

    def get_total_column(self):
        return len(self.driver.find_element(By.XPATH, self.table_column_xpath))

    def search_customer_by_email(self, emailID):
        flag = False
        for i in range(1, self.get_total_rows()+1):
            table = self.driver.find_element(By.ID, self.table_search_result_id)
            email_id_searched = table.find_element(By.XPATH, "//table[@id='customers-grid']/tbody/tr[" + str(i) + "/td[2]").text
            if email_id_searched == emailID:
                flag = True
                break
            else:
                flag = False
                break
        return flag

