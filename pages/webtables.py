from pages.base_page import BasePage
from components.components import WebElement


class WebTables(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/webtables'
        super().__init__(driver, self.base_url)

        self.no_rows = WebElement(driver, 'div.rt-noData')
        self.delete_record = WebElement(driver,'.action-buttons [title="Delete"]')