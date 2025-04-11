from pages.webtables import WebTables

import time



def test_sort(browser):
    webtable_page = WebTables(browser)
    webtable_page.visit()
    webtable_page.columnheader.click()
    time.sleep(2)
    assert webtable_page.columnheader.get_dom_attribute('class') == 'rt-th rt-resizable-header -sort-asc -cursor-pointer'
