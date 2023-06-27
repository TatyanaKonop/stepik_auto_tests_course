import time
import math


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

try:
    link = 'http://suninjuly.github.io/explicit_wait2.html'
    browser = webdriver.Chrome()
    browser.get(link)
    def calk(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    WebDriverWait(browser, 10).until(EC.text_to_be_present_in_element((By.ID, "price"), "100"))

    button = browser.find_element(By.CSS_SELECTOR, "#book")
    button.click()
    input = browser.find_element(By.CSS_SELECTOR, "#answer")
    browser.execute_script('return arguments[0].scrollIntoView(true);', input)
    value = browser.find_element(By.CSS_SELECTOR, '#input_value')
    x = value.text
    input.send_keys(calk(x))
    submit = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
    submit.click()
    time.sleep(5)
finally:
    browser.quit()
