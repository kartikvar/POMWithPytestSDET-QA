import configparser

config = configparser.ConfigParser()
#config.read(".\\Configurations\\config.ini")
config.read("D:\\Learn_SDET\\Selenium\\Selenium_Codes\\POMWithPytestSDET-QA\\Configurations\\config.ini")


class ReadConfig:

    @staticmethod
    def get_application_url():
        url = config.get("url", "baseURL")
        return url

    @staticmethod
    def get_username():
        username = config.get("credentials", "username")
        return username

    @staticmethod
    def get_password():
        password = config.get("credentials", "password")
        return password