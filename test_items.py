import pytest
import time

def test_user_should_see_add_to_cart_button(browser):
    url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(url)
    time.sleep(10)
    button = len(browser.find_elements_by_css_selector("#add_to_basket_form > button"))
    assert button > 0, 'Кнопка добавления в Корзину отсутствует!'