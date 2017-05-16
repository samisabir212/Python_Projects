from base.selenium_driver import SeleniumDriver
import time
import utilities.custom_logger as cl
import logging
from base.basepage import BasePage

"""
THIS IS YOUR TEST SPECIFICALLY FOR THE LOGIN PAGE
THIS HOLDS YOUR DATA AND INHERTIED METHODS FROM DIFFERENT CLASSES
THIS CLASS IS USING THE BASEPAGE WHICH IS USING SELENIUM DRIVER CLASS WHICH IS USING 
WEBDRIVERFACTORY WHICH IS INHERTED TO CONFTEST WHICH HOLDS THE SETUP
"""

# inherting from BasePage because BasePage class already inherits the SeleniumDriver class
class LoginPage(BasePage):

    log = cl.customLogger(logging.DEBUG)


    # this is a constructor
    def __init__(self,driver):
        # calling the __init__ method of super class and providing the driver
        # because it needs a driver instance to perform actions on elements
        super().__init__(driver)
        self.driver = driver

    #LOCATORS
    """
    when there is changes in the data used to test with
    only change the locators variables
    """
    _login_link = "Login"
    _email_field = "user_email"
    _password_field = "user_password"
    _login_button = "commit"




    # ONLY Methods with Actions Performed on the Elements
    def clickLoginLink(self):
        self.elementClick(self._login_link,locatorType="link")

    def enterEmail(self,email):
        self.sendKeys(email, self._email_field)

    def enterPassword(self,password):
        self.sendKeys(password,self._password_field)


    def clickLoginButton(self):
        self.elementClick(self._login_button,locatorType="name")


    # functionality that wraps all the actions
    # optional arguments by adding =""
    # this allows to verify different scenrios
    def login(self, userName="", password=""):
        self.clickLoginLink()
        time.sleep(2)
        self.enterEmail(userName)
        time.sleep(2)
        self.enterPassword(password)
        time.sleep(2)
        self.clickLoginButton()

    def verifyLoginSuccessful(self):
        result = self.isElementPresent("//*[@id='navbar']//span[text()='User Settings']",
                                       locatorType="xpath")
        return result

    def verifyLoginFailed(self):
        result = self.isElementPresent("//div[contains(text(),'Invalid email or password')]",
                                        locatorType="xpath")
        return result

    def verifyTitle(self):
        return self.verifyPageTitle("google")









    # HARD CODED CODE TO set up LOGIN TEST
    # # method to login with parameters to test with
    # def login(self,userName, password):
    #     loginLink = self.driver.find_element(By.LINK_TEXT, "Login")
    #     loginLink.click()
    #
    #     emailField = self.driver.find_element(By.ID, "user_email")
    #     emailField.send_keys(userName)
    #
    #     passwordField = self.driver.find_element(By.ID, "user_password")
    #     passwordField.send_keys(password)
    #
    #     loginButton = self.driver.find_element(By.NAME, "commit")
    #     loginButton.click()
    #







