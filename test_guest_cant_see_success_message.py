from .pages.product_page import ProductPage
from .pages.locators import ProductPageLocators
import pytest


def test_guest_cant_see_success_message(browser):
    # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    product_page = ProductPage(browser, ProductPageLocators.product_link)
    # открываем страницу
    product_page.open()
    product_page.should_not_be_success_message()


# pytest -s test_guest_cant_see_success_message.py