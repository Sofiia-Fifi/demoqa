from pages.webtables import WebTables
from selenium.webdriver.common.keys import Keys
import time


def test_next_page(browser):
    next_page = WebTables(browser)

    next_page.visit()
    assert next_page.equal_url()
    next_page.rows_per_page.scroll_to_element()
    next_page.rows_per_page.click_force()
    next_page.rows_per_page.send_keys(Keys.ARROW_UP)
    next_page.rows_per_page.send_keys(Keys.ENTER)
    time.sleep(2)

    assert next_page.btn_next.get_dom_attribute('disabled') == 'true'
    assert next_page.btn_previous.get_dom_attribute('disabled') == 'true'

    for i in range(3):
        next_page.btn_add.click()
        next_page.first_name.send_keys('tester')
        next_page.last_name.send_keys('testerovich')
        next_page.email.send_keys('test@sm.ts')
        next_page.age.send_keys('26')
        next_page.salary.send_keys('100000')
        next_page.department.send_keys('Quality Assurance')
        next_page.btn_modal_submit.click()
        time.sleep(2)

    # появляется 2 страница (of2)
    assert next_page.total_pages.get_text() == '2'
    # next активна
    assert next_page.btn_next.get_dom_attribute('disabled') == False
    # next click > открывается страница 2
    next_page.btn_next.click()
    assert next_page.page_num.get_dom_attribute('value') == '2'
    time.sleep(2)
    # previous click > открывается страница 1
    next_page.btn_previous.click()
    assert next_page.page_num.get_dom_attribute('value') == '1'
    time.sleep(2)