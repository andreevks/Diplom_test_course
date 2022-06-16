from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, 'span.btn-group a.btn.btn-default')
    USER_ICON = (By.CSS_SELECTOR, 'i.icon-user')

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_PAGE_URL = 'http://selenium1py.pythonanywhere.com/ru/accounts/login'
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTRATION_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTRATION_PASSWORD_1 = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTRATION_PASSWORD_2 = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTRATION_SUBMIT_BTN = (By.CSS_SELECTOR, "button[name='registration_submit']")

class BasketPageLocators():
    BASKET_GOODS = (By.CSS_SELECTOR, "div.basket-items")
    BASKET_EMPTY_TEXT = (By.CSS_SELECTOR, "#content_inner")

class ProductPageLocators():
    # product_link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    # product_link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'
    product_link_3 = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207'
    ADD_TO_CART_BTN = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    PRODUCT_NAME_IN_CART = (By.CSS_SELECTOR, "div.alertinner strong")
    PRODUCT_NAME_ON_PAGE = (By.CSS_SELECTOR, "div.product_main h1")
    CART_PRICE = (By.CSS_SELECTOR, "div.alertinner p strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "p.price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages div:nth-child(1)")
