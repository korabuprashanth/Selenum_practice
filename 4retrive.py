#Retrieve the text between html tags
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC      # when element throws exception
from selenium.webdriver.support.ui import WebDriverWait

driver=webdriver.Chrome()             # to Launch browse

driver.maximize_window()
driver.get("https://omayo.blogspot.com/") 

#retrive text
'''enter1=driver.find_element(By.XPATH,"//td[.='Kishore']").text
print(enter1)'''

# current url print
'''print(driver.current_url)'''        

#title of the page

'''title_name=driver.title
print(title_name)

time.sleep(5)

driver.find_element(By.LINK_TEXT,"Open a popup window").click()
time.sleep(2)

title_name2=driver.title
print(title_name2)

driver.close()
driver.quit()
time.sleep(10)'''                 #   close & quit
# current url ----print(driver.current_url)
