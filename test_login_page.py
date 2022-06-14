from .pages.login_page import LoginPage
from .pages.locators import MainPageLocators
link = 'http://selenium1py.pythonanywhere.com/'

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


# pip install -r requirements.txt
# команда для запуска
# pytest -v --tb=line --language=en test_login_page.py