from pages.homepage import Homepage
from pages.product import ProductPage


def test_open_phone_galaxy_s6(driver):
    homepage = Homepage(driver)
    homepage.open()
    homepage.click_samsung_galaxy_s6()
    product = ProductPage(driver)
    product.check_title_is("Samsung Galaxy S6")


def test_two_monitors(driver):
    homepage = Homepage(driver)
    homepage.open()
    homepage.click_monitors()
    product = ProductPage(driver)
    product.check_products_count(2)

