from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


link = "https://suninjuly.github.io/math.html"

try:
    driver = webdriver.Chrome()
    driver.get(link)
    
    x_element = driver.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)
    print(y)
    
    input_answer = driver.find_element(By.ID, "answer")

    input_answer.send_keys(y)

    chek_box = driver.find_element(By.ID, "robotCheckbox")
    chek_box.click()
    
    radio_butn = driver.find_element(By.CSS_SELECTOR, ".form-check.form-radio-custom .form-check-input")
    radio_butn.click()
    
    button_submit = driver.find_element(By.CSS_SELECTOR, ".btn.btn-default")
    button_submit.click()
    


finally:
    time.sleep(10)
    driver.quit()