from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
from .pages.locators import ProductPageLocators
from .pages.locators import LoginPageLocators
import pytest
import time

link = ProductPageLocators.PRODUCT_LINK


@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    product_page = ProductPage(browser, link)
    # открываем страницу
    product_page.open()
    # запускаем все тесты из класса
    product_page.should_be_on_product_page()


def test_guest_cant_see_success_message(browser):
    # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    product_page = ProductPage(browser, link)
    # открываем страницу
    product_page.open()
    product_page.should_not_be_success_message()


@pytest.mark.xfail(reason="This test can be failed")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    product_page = ProductPage(browser, link)
    # открываем страницу
    product_page.open()
    # добавляем товар в корзину
    product_page.add_product_to_cart()
    product_page.should_not_be_success_message()


@pytest.mark.xfail(reason="This test can be failed")
def test_message_disappeared_after_adding_product_to_basket(browser):
    # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    product_page = ProductPage(browser, link)
    # открываем страницу
    product_page.open()
    # добавляем товар в корзину
    product_page.add_product_to_cart()
    product_page.success_message_is_disappeared()


def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = BasketPage(browser, link)
    page.open()
    page.go_to_basket_page()
    page.no_goods_in_basket()
    page.is_text_empty_basket()


class TestUserAddToBasketFromProductPage():

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        # создаем email и пароль
        email = str(time.time()) + "@fakemail.org"
        password = 'ABcO_132*1654+Isdlkfj'
        # открываем страницу регистрации
        page = LoginPage(browser, LoginPageLocators.LOGIN_PAGE_URL)
        page.open()
        # регистрируем нового пользователя
        page.register_new_user(email, password)
        # проверяем, что пользователь залогинен
        page.should_be_authorized_user()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):  # , link):
        # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        product_page = ProductPage(browser, link)
        # открываем страницу
        product_page.open()
        # запускаем все тесты из класса
        product_page.should_be_on_product_page()

    def test_user_cant_see_success_message(self, browser):
        # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        product_page = ProductPage(browser, link)
        # открываем страницу
        product_page.open()
        product_page.should_not_be_success_message()

# команда для запуска теста
# pytest -s test_product_page.py
