from .pages.main_page import MainPage
from .pages.basket_page import BasketPage
from .pages.locators import MainPageLocators

link = MainPageLocators.MAIN_PAGE_URL


def test_guest_can_go_to_login_page(browser):
    # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page = MainPage(browser, link)
    # открываем страницу
    page.open()
    # выполняем метод страницы — переходим на страницу логина
    page.go_to_login_page()


def test_guest_should_see_login_link(browser):
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    page = BasketPage(browser, link)
    page.open()
    page.go_to_basket_page()
    page.no_goods_in_basket()
    page.is_text_empty_basket()

# команда для запуска
# pytest -v --tb=line --language=en test_main_page.py
