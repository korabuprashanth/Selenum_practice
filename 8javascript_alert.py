from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC      # when element throws exception
from selenium.webdriver.support.ui import WebDriverWait

driver=webdriver.Chrome()             # to Launch browse

'''driver.get("https://the-internet.herokuapp.com/")
driver.maximize_window()
driver.find_element(By.LINK_TEXT,"JavaScript Alerts").click()
driver.find_element(By.XPATH,"(//button)[3]").click()
#information alert'''
'''info_alert= driver.switch_to.alert
print(info_alert.text)
info_alert.accept()'''
#  prompt alert need to enter the data
'''prompt_alert=driver.switch_to.alert
print(prompt_alert.text)
prompt_alert.send_keys("Hi Prashanth")
prompt_alert.accept()
time.sleep(3)'''
#driver.find_element(By.XPATH,"//button[text()='Click for JS Confirm']").click()

# for authentication pop up  add user and pwd in browser link
driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")

time.sleep(2)


driver.quit()