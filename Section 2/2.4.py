from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/explicit_wait2.html"

driver = webdriver.Chrome()

try:
    driver.get(link)
    
    btn = driver.find_element(By.ID, "book")
    #говорим WebDriver ждать все элементы в течение 12 секунд
    #говорим EC.text_to_be_present_in_element((By.ID, "где ждем"), "что ждем"))
    WebDriverWait(driver, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "100"))
    btn.click()
    
    x_val = driver.find_element(By.ID, 'input_value').text
    
    y = calc(x_val)
    
    anser = driver.find_element(By.ID, 'answer').send_keys(y)
    
    driver.find_element(By.ID, 'solve').click()
    #выводим в консоль текст с алерта.
    print(driver.switch_to.alert.text)
    
    
    
finally:
    time.sleep(5)
    
    driver.quit()