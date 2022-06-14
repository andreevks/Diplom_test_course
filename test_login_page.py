from .pages.main_page import MainPage
from .pages.locators import MainPageLocators
link = 'http://selenium1py.pythonanywhere.com/'

def go_to_login_page(browser):
    login_link = browser.find_element(*MainPageLocators.LOGIN_LINK)
    login_link.click()

def test_login_link(browser):
    # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page = LoginPage(browser, link)
    # открываем страницу
    page.open()
    page.go_to_login_page()
    # выполняем метод страницы по проверке корректностии ссылки на страницу регистрации
    page.should_be_login_url()

def test_should_be_login_form(browser):
    page = LoginPage(browser, link)
    page.open()
    page.go_to_login_page()
    page.should_be_login_form()

def test_should_be_register_form(browser):
    page = LoginPage(browser, link)
    page.open()
    page.go_to_login_page()
    page.should_be_register_form()