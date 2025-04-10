from pages.koup_base_page import Heroku
from pages.koup_Add_Remove_page import AddRemove
import time


def test_btn_add(browser):
    add_remove = Heroku(browser)
    add_element = AddRemove(browser)

    add_remove.visit()
    assert add_remove.btn_remove_elements.get_text() == 'Add/Remove Elements'
    add_remove.btn_remove_elements.click()
    assert add_element.equal_url()
    assert add_element.btn_add_element.get_text() == 'Add Element'
    assert add_element.btn_add_element.get_dom_attribute('onclick') == 'addElement()'

    for i in range(4):
        add_element.btn_add_element.click()

    time.sleep(3)
    assert add_element.btn_delete.check_count_elements(4)

    for element in add_element.btn_delete.find_elements():
        assert element.text == 'Delete'

    while add_element.btn_delete.exist():
        add_element.btn_delete.click()

    time.sleep(3)
    assert not add_element.btn_delete.exist()
