from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time 

link = "https://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = browser.find_element(By.CSS_SELECTOR, '#num1').text
    num2 = browser.find_element(By.CSS_SELECTOR, '#num2').text
    answer = int(num1) + int(num2)
    select = Select(browser.find_element(By.CSS_SELECTOR, 'select'))
    select.select_by_value(str(answer))
    browser.find_element(By.CSS_SELECTOR, 'button').click()

finally:
    time.sleep(10)
    browser.quit()