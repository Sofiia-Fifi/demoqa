from urllib3.util import wait_for_write

from pages.webtables import WebTables
import time

def test_add_record(browser):
    webtables_page = WebTables(browser)

    webtables_page.visit()

# на странице имеется кнопка Add
    assert webtables_page.btn_add.exist()

# по клику на кнопку Add открывается диалоговое окно
    webtables_page.btn_add.click()
    assert webtables_page.modal_content.exist()

# в диалоге нельзя сохранить пустую форму
    webtables_page.btn_modal_submit.click()
    time.sleep(2)
    assert webtables_page.registration_form.get_dom_attribute('class') == 'was-validated'

# заполнить все поля и нажать на кнопку Submit
    webtables_page.first_name.send_keys('tester')
    webtables_page.last_name.send_keys('testerovich')
    webtables_page.email.send_keys('test@sm.ts')
    webtables_page.age.send_keys('26')
    webtables_page.salary.send_keys('100000')
    webtables_page.department.send_keys('Quality Assurance')
    time.sleep(2)
    webtables_page.btn_modal_submit.click()
    time.sleep(2)

# диалог закрывается
    assert not webtables_page.registration_form.exist()

# в таблицу добавляется новая запись с введенными данными
    assert webtables_page.record_4.exist()
    record_4_current = webtables_page.record_4.get_text()

# если кликнуть на карандаш на строке записи
    webtables_page.btn_edit.click()

# открывается диалог с введенными данными
    assert webtables_page.modal_content.exist()

# если изменить имя и сохранить, то в таблице обновятся данные
    webtables_page.first_name.clear()
    webtables_page.first_name.send_keys('engineer')
    webtables_page.btn_modal_submit.click_force()
    time.sleep(2)
    record_4_new = webtables_page.record_4.get_text()
    assert not record_4_current == record_4_new
    time.sleep(2)


# если нажать на корзину в строке записи - запись удаляется
    webtables_page.delete_record.click()
    time.sleep(2)
    assert webtables_page.record_4.get_text() == "       "
