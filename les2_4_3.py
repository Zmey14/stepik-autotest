from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = 'http://suninjuly.github.io/explicit_wait2.html'
    browser = webdriver.Chrome()
    browser.get(link)

    waiting = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    button = browser.find_element_by_id('book').click()



    x = browser.find_element_by_id('input_value').text
    result = calc(x)

    browser.execute_script("window.scrollBy(0, 100);")
    input1 = browser.find_element_by_id('answer').send_keys(str(result))

    
    button2 = WebDriverWait(browser, 2).until(
        EC.element_to_be_clickable((By.ID, 'solve'))
    )
    button2.click()

    alert = browser.switch_to.alert
    alert_text = alert.text
    copy = alert_text.split(': ')[-1]
    print(copy)

finally:
    browser.quit()