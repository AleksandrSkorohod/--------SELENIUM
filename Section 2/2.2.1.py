import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects1.html"

try:
    driver = webdriver.Chrome()
    driver.get(link)
    
    num1 = driver.find_element(By.ID, "num1")
    num2 = driver.find_element(By.ID, "num2")
    result = int(num1.text) + int(num2.text)
    
    #селект открывает выпадающее окно, ненадо клик
    select = Select(driver.find_element(By.ID, "dropdown"))
    
    result1 = str(result)
    #селект выбирает строку и кликает на нее. Клик писать ненадо
    select.select_by_value(result1)
    time.sleep(1)
    
    btn = driver.find_element(By.XPATH, "/html/body/div[1]/form/button").click()
    
    
    
    
    
finally:
    time.sleep(10)
    driver.quit()