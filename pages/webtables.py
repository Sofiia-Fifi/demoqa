from pages.base_page import BasePage
from components.components import WebElement


class WebTables(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/webtables'
        super().__init__(driver, self.base_url)

        self.no_rows = WebElement(driver, 'div.rt-noData')
        self.delete_record = WebElement(driver,'.action-buttons [title="Delete"]')
        self.btn_add = WebElement(driver, '#addNewRecordButton')
        self.modal_content = WebElement(driver,'body > div.fade.modal.show > div > div')
        self.btn_modal_submit = WebElement(driver, '.text-right > #submit')
        self.registration_form = WebElement(driver, '#userForm')
        self.first_name = WebElement(driver,'#firstName')
        self.last_name = WebElement(driver, '#lastName')
        self.email = WebElement(driver, '#userEmail')
        self.age = WebElement(driver, '#age')
        self.salary = WebElement(driver, '#salary')
        self.department = WebElement(driver, '#department')
        self.record_4 = WebElement(driver, ' div.rt-tbody > div:nth-child(4) > div')
        self.btn_edit = WebElement(driver,'#edit-record-4 > svg > path')
        self.rows_per_page = WebElement(driver, 'span.select-wrap.-pageSizeOptions > select')
        self.btn_next = WebElement(driver, '.-next > button')
        self.btn_previous = WebElement(driver, '.-previous > button')
        self.total_pages = WebElement(driver, 'span.-pageInfo > span')
        self.page_num = WebElement(driver,'span.-pageInfo > div > input[type=number]')