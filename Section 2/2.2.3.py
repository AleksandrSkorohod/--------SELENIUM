
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


link = "http://suninjuly.github.io/file_input.html"



try:
    driver = webdriver.Chrome()
    driver.get(link)
    
    name = driver.find_element(By.CSS_SELECTOR, "div .form-control")
    name.send_keys("alex")
    
    last_name = driver.find_element(By.NAME, "lastname")
    last_name.send_keys("skor")
    
    email = driver.find_element(By.NAME, "email")
    email.send_keys("alex@mail.ru")
    
    #определяем путь к папки с файлом
    current_dir = os.path.abspath(os.path.dirname(__file__))
    #имя файла в переменную
    file_name = "file.txt"
    #собираем обсалютный путь к файлу
    file_path = os.path.join(current_dir, file_name)
    
    
    
    #определяем кнопку выбора файла
    send_file = driver.find_element(By.ID, "file")
    #прикрепляем файл
    send_file.send_keys(file_path)
    
    btn = driver.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
    btn.click()
    
    

    
    
    
finally:
    time.sleep(10)
    driver.quit()
    
    
    