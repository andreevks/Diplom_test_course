from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    # product_link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    product_link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'
    ADD_TO_CART_BTN = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    PRODUCT_NAME_IN_CART = (By.CSS_SELECTOR, "div.alertinner strong")
    PRODUCT_NAME_ON_PAGE = (By.CSS_SELECTOR, "div.product_main h1")
    CART_PRICE = (By.CSS_SELECTOR, "div.alertinner p strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "p.price_color")
