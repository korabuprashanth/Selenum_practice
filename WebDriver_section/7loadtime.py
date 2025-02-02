from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC      # when element throws exception
from selenium.webdriver.support.ui import WebDriverWait

driver=webdriver.Chrome()             # to Launch browse

driver.get("https://omayo.blogspot.com/")
driver.maximize_window()
#driver.set_page_load_timeout(100)

# mutliple element locate
'''links1=driver.find_elements(By.XPATH,"//link")
print(len(links1))
print(links1)
for link in links1:
    print(link)'''

#locate using tag name

'''var1=driver.find_elements(By.TAG_NAME,"textarea")
for var in var1:
    var.send_keys("Hi PJ")
    var.send_keys("Hi JK")'''


    
#print(driver.find_element(By.CSS_SELECTOR,"table[id='table1']").get_attribute("border"))

time.sleep(10)

driver.quit()

