from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service


options = webdriver.ChromeOptions() 
options.add_experimental_option('excludeSwitches', ['enable-logging']) 
service = Service('chromedriver.exe')
driver = webdriver.Chrome(service=service, options=options)

driver.maximize_window() 

driver.get("https://www.youtube.com/")