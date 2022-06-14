from .pages.product_page import ProductPage
from .pages.locators import ProductPageLocators

def test_product_page(browser):
    # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    product_page = ProductPage(browser, ProductPageLocators.product_link)
    # открываем страницу
    product_page.open()
    # # добавляем товар в корзину
    # product_page.add_product_to_cart()
    # # решаем задачку
    # product_page.solve_quiz_and_get_code()

    # запускаем все тесты из класса
    product_page.should_be_on_product_page()


# pytest -s test_guest_can_add_product_to_basket.py