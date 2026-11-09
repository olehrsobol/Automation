from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

class ProductPage:
    def __init__(self, driver):
        self.driver = driver

    def check_title_is(self, title):
        page_title = self.driver.find_element(By.CSS_SELECTOR, 'h2')
        assert page_title.text == "Samsung galaxy s6"

    def check_products_count(self, count):
        wait = WebDriverWait(self.driver, 10)
        cards = wait.until(
            lambda d: self.driver.find_elements(By.CSS_SELECTOR, ".card")
            if len(self.driver.find_elements(By.CSS_SELECTOR, ".card")) == 2
            else False
        )
        assert len(cards) == count