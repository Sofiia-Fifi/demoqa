from pages.webtables import WebTables

import time



def test_sort(browser):
    webtable_page = WebTables(browser)
    webtable_page.visit()

    for header in webtable_page.columnheader.find_elements():
        header.click()
        time.sleep(2)
        assert header.get_dom_attribute('class') == 'rt-th rt-resizable-header -sort-asc -cursor-pointer'
