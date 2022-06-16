from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_on_product_page(self):
        self.add_product_to_cart()
        # self.solve_quiz_and_get_code()
        self.check_product_name_in_cart()
        self.check_product_price_in_cart()

    def add_product_to_cart(self):
        add_to_cart_btn = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BTN)
        add_to_cart_btn.click()

    def check_product_name_in_cart(self):
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_ON_PAGE).text == \
               self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_CART).text, \
               'Наименование товара не совпадает'

    def check_product_price_in_cart(self):
        assert self.browser.find_element(*ProductPageLocators.CART_PRICE).text == \
               self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text, \
               'Цена товара не совпадает'


    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def success_message_is_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is not disappeared, but should be"
