import time
from utilities.statusoftesst import status

from base.basepage import BasePage
import utilities.custom_logger as cl
import logging



class RegisterCoursesPage(BasePage):

    log = cl.customLogger(logging.DEBUG)
    s = status

    # this is a constructor
    def __init__(self, driver):
        # calling the __init__ method of super class and providing the driver
        # because it needs a driver instance to perform actions on elements
        super().__init__(driver)
        self.driver = driver

    # declare locators for elements

     # xpath
    _allCourses_Button = ".//ul[@class='nav navbar-nav navbar-right']//a[contains(text(),'All Courses')]"

    # by ID
    _search_field = "search-courses"

    # by xpath
    _javascriptcourse = ".//div[@class='course-listing']//div[contains(text(),' JavaScript for beginners' )]"

    # by id
    _enrollInCourseButton = "enroll-button-top"

    _paymentPageVerify = ""
    # by id
    _cc_num = "cc_field"

    # by id
    _cc_exp = "cc_exp"

    # by id
    _cc_cvc = "cc_cvc"

    # by xpath
    _country = ".//div[@class='col-sm-12 section-country']//select[@id='country-select-inside']//*[text()[contains(.,'United States')]]"

    # by id
    _verifyCardButton = "verify_cc_btn"

    # by class
    _enroll_error_message = "payment-errors invalid_number"



    # functionality that wraps all the actions
    # optional arguments by adding =""
    # this allows to verify different scenrio
    # methods to perform actions

    def clickAllCourses(self):
        self.elementClick(self._allCourseButton,locatorType="xpath")

    def enter_search_Course(self,name):
        self.sendKeys(name, self._search_field,locatorType="id")

    def clickCourse(self):
        self.elementClick(self._javascriptcourse,locatorType="xpath")

    def clickEnrollSubmitButton(self):
        self.elementClick(self._enrollInCourseButton,locatorType="id")

    # ---------------------------------------------------

    def enterCardnum(self, num):
        self.sendKeys(num, self._cc_num)

    def enterCardExp(self,exp):
        self.sendKeys(exp,self._cc_exp)


    def enterCardCVV(self, cvv):
        self.sendKeys(cvv, self._cc_cvc)

    def clickCountry(self):
        self.elementClick(self._country,locatorType="xpath")


    # -------------------------------------------------

    def javaScriptCourseAfterLogin(self,name):
        # self.clickAllCourses()
        time.sleep(2)
        self.enter_search_Course(name)
        time.sleep(2)
        self.clickCourse()
        time.sleep(2)
        result1 = self.verifyTitle("javascript for beginners")
        self.s.mark(result1, "Title Verified")
        time.sleep(2)
        self.clickEnrollSubmitButton()




    def enterCreditCardInformation(self, num, exp, cvv):
        self.enterCardnum(num)
        self.enterCardExp(exp)
        self.enterCardCVV(cvv)
        self.clickCountry()


    # MUST WAIT FOR INSTRUCTOR TO GIVE ME GOOD XPATH FOR THIS VERIFICATION
    def verifyPaymentInfoPageIsPresent(self):
        result = self.isElementPresent(".//*[@id='product-tax-information']/div/div[2]/div/div/h1[2]",
                                       locatorType="xpath")
        return result



    def verifyCreditCardFailure(self):
        result = self.isElementPresent(".//div[@id='checkout_form_errors']/div[5]",
                                       locatorType="xpath")
        return result



    def verifyTitle(self,title):
        return self.verifyPageTitle(title)








