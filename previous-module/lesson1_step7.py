from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    treasure = browser.find_element(By.CSS_SELECTOR, '[valuex]').get_attribute('valuex')
    browser.find_element(By.CSS_SELECTOR, '#answer').send_keys(calc(treasure))
    
    browser.find_element(By.CSS_SELECTOR, '[type="checkbox"]').click()

    browser.find_element(By.CSS_SELECTOR, '#RobotsRule').click()

    browser.find_element(By.CSS_SELECTOR, 'button').click()


finally:
    time.sleep(15)
    browser.quit()