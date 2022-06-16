from .base_page import BasePage
from .locators import LoginPageLocators
from .locators import MainPageLocators
import time


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert '/login/' in self.browser.current_url, 'Login link is not correct'

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), 'Login form not found'

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), 'Registration form not found'

    def register_new_user(self, email, password):
        # регистрация нового пользователя
        self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL).send_keys(email)
        self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD_1).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD_2).send_keys(password)