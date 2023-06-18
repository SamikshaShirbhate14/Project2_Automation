from selenium.webdriver.common.by import By

class Login:

    def __init__(self,driver):
        self.driver = driver
        self.clinic_Xpath = '//*[@id="clinic"]/span/input'
        self.username_xpath = '//*[@id="username"]/span/input'
        self.password_xpath = '//*[@id="password"]/span/input'
        self.checkbox_xpath = '//*[@id="rememberMe"]'
        self.login_xpath = '//*[@label="Login"]/span[1]'
        self.error_xpath = '//*[@class="text-align-center"]/span'

    def Enter_Clinic(self, ClinicText):
        self.driver.find_element(By.XPATH, self.clinic_Xpath).send_keys(ClinicText)

    def Enter_Username(self, Username):
        self.driver.find_element(By.XPATH, self.username_xpath).send_keys(Username)

    def Enter_Password(self, Password):
        self.driver.find_element(By.XPATH, self.password_xpath).send_keys(Password)

    def Click_RemenberMe(self):
        self.driver.find_element(By.XPATH, self.checkbox_xpath).click()

    def Click_Login(self):
        self.driver.find_element(By.XPATH, self.login_xpath).click()

    def Error_Msg(self):
        self.driver.find_element(By.XPATH, self.error_xpath).text()


