from utilities.statusoftesst import status
import unittest
import pytest
from pages.courses.register_courses_page import RegisterCoursesPage
from pages.Home.login_page import LoginPage

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class RegisterCoursesTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):

        self.lp = LoginPage(self.driver)
        self.s = status(self.driver)
        self.rct = RegisterCoursesPage(self.driver)



    @pytest.mark.run(order=1)
    def test_invalidJavaScriptEnrollment(self):

        self.lp.login("test@email.com","abcabc")
        self.rct.javaScriptCourseAfterLogin("JavaScript")
        self.rct.enterCreditCardInformation("212","10/01","2")
        self.rct.verifyPaymentInfoPageIsPresent()
        self.rct.verifyCreditCardFailure()


    @pytest.mark.run(order=2)
    def verifyCreditCardFailure_TEST(self):

        result = self.rct.verifyCreditCardFailure()
        assert result == True




