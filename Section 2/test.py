import os 
from selenium import webdriver

driver = webdriver.Chrome()

alert = driver.switch_to.alert
alert_text = alert.text