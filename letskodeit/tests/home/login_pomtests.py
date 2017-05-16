from pages.Home.login_page import LoginPage
from utilities.statusoftesst import status
import unittest
import pytest

"""
run it from the command line
"""

@pytest.mark.usefixtures("oneTimeSetUp","setUp")
class LoginTests(unittest.TestCase):


    # defining the object for the loginpage
    # LoginPage object page for the testclass
    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):

        self.lp = LoginPage(self.driver)
        self.s = status(self.driver)




    # test method to pass
    @pytest.mark.run(order=2)
    def test_validLogin(self):

        self.lp.login("test@email.com", "abcabc")
        result1 = self.lp.verifyTitle()
        self.s.mark(result1, "Title Verified")
        result2  = self.lp.verifyLoginSuccessful()
        self.s.markFinal("test_validLogin", result2, "Login was successful")

    # test method  to fail
    @pytest.mark.run(order=1)
    def test_invalidLogin(self):

        self.lp.login("test@email.com", "wrongpassword")

        result = self.lp.verifyLoginFailed()

        assert result == True

