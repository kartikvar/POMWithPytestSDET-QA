import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from Configurations.readProperties import ReadConfig
from pageObjects.LoginPage import LoginPage


def test_login():
    os.environ['WDM_SSL_VERIFY'] = '0'
    service = Service()
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(service=service, options=options)
    baseURL = ReadConfig.get_application_url()
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()
    print("URL is {}".format(baseURL))
    print("username is {}".format(username))
    print("password is {}".format(password))
    driver.maximize_window()
    driver.get(baseURL)

    # login into the application. using already created loginpage
    lp = LoginPage(driver)
    lp.set_username(username)
    lp.set_password(password)
    lp.click_login()