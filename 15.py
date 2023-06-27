import time
import math

from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    link = 'http://suninjuly.github.io/redirect_accept.html'
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element(By.XPATH, "//button[contains(@class, 'trollface')]")
    button.click()
    new_win = browser.window_handles[1]
    browser.switch_to.window(new_win)
    def calk(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    value = browser.find_element(By.CSS_SELECTOR, '#input_value')
    x = value.text
    input = browser.find_element(By.CSS_SELECTOR, '#answer')
    input.send_keys(calk(x))
    submit = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
    submit.click()
    time.sleep(5)
finally:
    browser.quit()
