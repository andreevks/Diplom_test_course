from .pages.product_page import ProductPage
from .pages.locators import ProductPageLocators
import pytest


def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    product_page = ProductPage(browser, ProductPageLocators.product_link)
    # открываем страницу
    product_page.open()
    # добавляем товар в корзину
    product_page.add_product_to_cart()
    product_page.should_not_be_success_message()


# pytest -s test_guest_cant_see_success_message_after_adding_product_to_basket.py