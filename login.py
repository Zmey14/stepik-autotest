from selenium import webdriver
import time


class log():
    login = 'Вводим свой email'
    passw = 'Вводим свой пароль'
    


link = 'https://lk.sut.ru/cabinet/?login=no'
browser = webdriver.Chrome()
browser.get(link)

try:
    input_log = browser.find_element_by_css_selector('input#users').send_keys(log.login)
    input_pas = browser.find_element_by_css_selector('input#parole').send_keys(log.passw)
    button_1 = browser.find_element_by_css_selector('input#logButton').click()
    time.sleep(2)
finally:
    browser.quit()
