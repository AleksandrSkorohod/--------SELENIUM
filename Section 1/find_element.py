
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/simple_form_find_task.html"

try:
    
    driver = webdriver.Chrome()
    driver.get(link)
    button = driver.find_element(By.ID, "submit_button")
    button.click()

finally:
    driver.quit()
