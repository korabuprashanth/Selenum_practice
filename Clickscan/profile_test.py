from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC      # when element throws exception
from selenium.webdriver.support.ui import WebDriverWait

driver=webdriver.Chrome()             # to Launch browse

driver.maximize_window()
driver.get()  

#print(driver.find_element(By.CSS_SELECTOR,"table[id='table1']").get_attribute("border"))
driver.fullscreen_window()
driver.find_element(By.ID,"username").send_keys()
driver.find_element(By.ID,"password").send_keys()
time.sleep(1)
driver.find_element(By.XPATH,"//button[text()='Log in']").click()
time.sleep(1)
Admin_button=WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//button[text()='Admin']")))
Admin_button.click()
time.sleep(2)
driver.find_element(By.XPATH,"//button[text()='Continue']").click()
time.sleep(1)
if (driver.find_element(By.XPATH,"//li[text()='Dashboard']").is_displayed):
    print("loooged in")
else:
    print("not logged")
try:
    driver.get("https://clickscan.terralogic.com/dashboard")  # Replace with the URL of your application

    # Wait for the profile button to be clickable
    profile_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR,"div[class='ant-dropdown-trigger NavBar_dropdown_user__rERqt']")  # Update with the correct identifier
    ))
    profile_button.click()
    profile_button = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR,"p.NavBar_uname_txt__noomF"))  # Update with the correct identifier
    )
    profile_button.click()
    time.sleep(10)
    
    time.sleep(3)
    driver.back()
    current_url=driver.current_url
    print(current_url)
    expected_url="https://clickscan_stg.terralogic.com/folder-management"
    
    if (current_url==expected_url):
         print("Not to raise a bug- fixed")
    else:
         print("Its a bug please raise")
    time.sleep(2)
finally:
     driver.quit()
