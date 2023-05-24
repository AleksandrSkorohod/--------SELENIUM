from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

driver = webdriver.Chrome()

link = "http://suninjuly.github.io/redirect_accept.html"

try:
    
    driver.get(link)
    
    capch = driver.find_element(By.CSS_SELECTOR, ".trollface.btn.btn-primary").click()
    
    #находим все открытые вкладки в браузере
    new_window = driver.window_handles[1]
    #window_handles возвращает массив, в котором мы можем обратиться по индексу к окну (Индексы с 0 начинаются)
    
    #переключаемся на вкладку
    driver.switch_to.window(new_window)
    
    x = driver.find_element(By.ID, "input_value").text
    
    y = calc(x)
    
    input_anser = driver.find_element(By.ID, "answer").send_keys(y)
    
    driver.find_element(By.CSS_SELECTOR, '.btn.btn-primary').click()
    
    print(driver.switch_to.alert.text)
    
    
finally:
    driver.quit()