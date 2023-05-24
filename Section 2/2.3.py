from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

driver = webdriver.Chrome()

link = "http://suninjuly.github.io/alert_accept.html"

try:
    
    driver.get(link)
    
    btn = driver.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
    btn.click()
    
    #переключаемся на Алерт
    alert = driver.switch_to.alert
    #подтверждаем Алерт
    alert.accept()
    
    #можно еще отменить alert.dismiss()
    
    #если выпадает модальное окно с вводом текста, можно так
    # prompt = browser.switch_to.alert
    # prompt.send_keys("My answer")
    # prompt.accept()
    
    
    val = driver.find_element(By.ID, "input_value")
    x_val = val.text
    
    y = calc(x_val)
    
    input_form = driver.find_element(By.ID, "answer")
    input_form.send_keys(y)
    
    time.sleep(1)
    btn_send_form = driver.find_element(By.CSS_SELECTOR, ".btn.btn-primary").click()
    
    #можно вывести содержание Алерта в консоль
    print(driver.switch_to.alert.text)
    
finally:

    time.sleep(10)
    driver.quit()