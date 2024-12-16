from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "https://suninjuly.github.io/math.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.CSS_SELECTOR, '#input_value')
    x = x_element.text
    answer = browser.find_element(By.CSS_SELECTOR, '#answer')
    answer.send_keys(calc(x))

    checkbox = browser.find_element(By.CSS_SELECTOR, '[type="checkbox"]')
    checkbox.click()

    radio = browser.find_element(By.CSS_SELECTOR, '#RobotsRule')
    radio.click()

    submit_button = browser.find_element(By.CSS_SELECTOR, 'button')
    submit_button.click()

finally:
    time.sleep(15)
    browser.quit()