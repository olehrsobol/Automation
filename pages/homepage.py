from selenium.webdriver.common.by import By

class Homepage:
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get("https://demoblaze.com/index.html")

    def click_samsung_galaxy_s6(self):
        self.driver.find_element(By.XPATH, '//a[text()="Samsung galaxy s6"]').click()

    def click_monitors(self):
        self.driver.find_element(By.CSS_SELECTOR, '''[onclick="byCat('monitor')"]''').click()
