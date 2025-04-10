from pages.webtables import WebTables


def test_webtable(browser):
    webtable_page = WebTables(browser)

    webtable_page.visit()
    assert not webtable_page.no_rows.exist()

    while webtable_page.delete_record.exist():
        webtable_page.delete_record.click()

    assert webtable_page.no_rows.exist()