from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "https://suninjuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element(By.CSS_SELECTOR, '#input_value').text
    browser.find_element(By.CSS_SELECTOR, '#answer').send_keys(calc(x))
    browser.execute_script("window.scrollBy(0, 100);")
    browser.find_element(By.CSS_SELECTOR, '[type="checkbox"]').click()
    browser.find_element(By.CSS_SELECTOR, '#RobotsRule').click()
    button = browser.find_element(By.CSS_SELECTOR, "button")
    button.click()

finally:
    time.sleep(3)
    browser.quit()