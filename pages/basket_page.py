from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def no_goods_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_GOODS), \
        'There are goods in the basket, while basket is empty.'

    def is_text_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY_TEXT), \
                'Text "Your basket is now empty" not found.'