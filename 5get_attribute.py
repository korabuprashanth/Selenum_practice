from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC      # when element throws exception
from selenium.webdriver.support.ui import WebDriverWait

driver=webdriver.Chrome()             # to Launch browse

driver.maximize_window()
driver.get("https://clickscan.terralogic.com/login")  

#print(driver.find_element(By.CSS_SELECTOR,"table[id='table1']").get_attribute("border"))
