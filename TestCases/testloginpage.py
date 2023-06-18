import pytest

from ProjectObject.LoginPage import Login
import pytest

@pytest.mark.usefixtures()
class Test_Login:

    def test_login_001(self,setup):
        self.driver = setup
        self.log = Login(self.driver)
        self.log.Enter_Clinic('XYZ')
        self.log.Enter_Username('Jasmin')
        self.log.Enter_Password('Jasmin123')
        self.log.Click_RemenberMe()
        self.log.Click_Login()
        self.driver.close()

    def test_login_002(self,setup):
        self.driver = setup
        self.log = Login(self.driver)
        self.log.Enter_Clinic('XYZ')
        self.log.Enter_Password('Jasmin123')
        self.log.Click_RemenberMe()
        self.log.Click_Login()
        if self.log.Error_Msg == ' Invalid username or password ':
            assert True
        else:
            assert False
        self.driver.close()

    def test_login_003(self,setup):
        self.driver = setup
        self.log = Login(self.driver)
        self.log.Enter_Clinic('XYZ')
        self.log.Enter_Username('Jasmin')
        self.log.Click_RemenberMe()
        self.log.Click_Login()
        if self.log.Error_Msg == ' Invalid username or password ':
            assert True
        else:
            assert False
        self.driver.close()

