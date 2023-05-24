import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/execute_script.html"

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    driver = webdriver.Chrome()
    driver.get(link)
    
    val = driver.find_element(By.ID, "input_value")
    #получаем значение элемента
    x_val = val.text
    
    y = calc(x_val)
    print(y)
    
    anser = driver.find_element(By.ID, "answer")
    anser.send_keys(y)
    
    chek = driver.find_element(By.ID, "robotCheckbox").click()
    
    
    
    button = driver.find_element(By.TAG_NAME, "button")
    #так выполняется javascript
    driver.execute_script("return arguments[0].scrollIntoView(true);", button)
    
    radio = driver.find_element(By.ID, "robotsRule").click()
    
    
    button.click()
    
    
finally:
    time.sleep(10)
    driver.quit()