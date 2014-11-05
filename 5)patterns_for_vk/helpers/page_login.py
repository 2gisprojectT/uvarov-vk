class PageLogin():

    def __init__(self, driver):
        self.driver = driver
        self._login_field = None
        self._password_field = None

    @property
    def login_field(self):
        from helpers.page_login_elements.login_field import LoginField
        if self._login_field is None:
            self._login_field = LoginField(self.driver, self.driver.find_element_by_id(LoginField.selectors['self']))
        return self._login_field

    @property
    def password_field(self):
        from helpers.page_login_elements.password_field import PasswordField
        if self._password_field is None:
            self._password_field = PasswordField(self.driver, self.driver.find_element_by_id(PasswordField.selectors['self']))
        return self._password_field

    def open(self, url):
        self.driver.get(url)

    def sign_up_with_test_credentials(self):
        self.login_field.enter_login("+79513609119")
        self.password_field.enter_password_and_confirm("test_password")