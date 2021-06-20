from typing import final
from selenium import webdriver
import time


try:
    # link = 'http://suninjuly.github.io/wait1.html'
    link ='http://suninjuly.github.io/cats.html'
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.get(link)
    browser.find_element_by_id("button").click()






finally:
    browser.quit()