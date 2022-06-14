from .base_page import BasePage
from .locators import MainPageLocators

class ProductPage(BasePage):
    def go_to_product_page(self):
        product_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        product_link.click()