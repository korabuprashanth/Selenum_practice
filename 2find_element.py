from selenium import webdriver
from selenium.webdriver.common.by import By
import time
"""from selenium.webdriver.support import expected_conditions as EC      # when element throws exception
from selenium.webdriver.support.ui import WebDriverWait"""

driver=webdriver.Chrome()             # to Launch browse

driver.maximize_window()
driver.get("https://clickscan.terralogic.com/login")     #to enter to the url

driver.find_element(By.ID,'username').send_keys("pjkorabu")        #to find the elements  by ID
driver.find_element(By.ID,'password').send_keys("Prashanth12@")
#driver.find_element(By.CLASS_NAME,"btn-blue btn btn-primary").click()    # using  CLASS_NAME,"  "
#driver.find_element(By.LINK_TEXT,"Log in").click()                like using the text between the HYPER LINK
driver.find_element(By.XPATH,"//button [ @class='btn-blue btn btn-primary']").click()    # using XPATH
#driver.find_element(By.CSS_SELECTOR,"button [class='btn-blue btn btn-primary']").click()
"""wait = WebDriverWait(driver, 10)
button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[.='Admin']")))   # when element throws exception
button.click()"""

time.sleep(60)
driver.minimize_window()
