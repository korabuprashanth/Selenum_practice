
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
import time

# DISABLE POP-UPS
'''chrome_options=Options()
chrome_options.add_argument("--disable-notifications")

driver=webdriver.Chrome(options=chrome_options)
driver.get("https://www.homedepot.com/")
driver.maximize_window()
time.sleep((10))'''
# to close the LIGHT BOX
'''driver=webdriver.Chrome()
driver.get("https://tutorialsninja.com/demo/")
driver.set_page_load_timeout(3)
driver.find_element(By.CSS_SELECTOR,"img.img-responsive[title='MacBook']").click()
driver.find_element(By.XPATH,"(//img[@title='MacBook'][@alt='MacBook']) [1]").click()
time.sleep(3)
driver.find_element(By.XPATH,"//button[@title='Close (Esc)']").click()'''

# handle DROPDOWN ELEMENTS
'''driver=webdriver.Chrome()
driver.get("https://omayo.blogspot.com/")
time.sleep(3)
dropdown=driver.find_element(By.CSS_SELECTOR,"select.combobox")
select=Select(dropdown)
select.select_by_index(3)
dropdown_options=select.options
for options in dropdown_options:
    print(options.text)'''

# To handle MULTIPLE SELECTION OPTIONS
'''driver=webdriver.Chrome()
driver.get("https://omayo.blogspot.com/")
driver.set_page_load_timeout(5)
multi_select=driver.find_element(By.CSS_SELECTOR,"select#multiselect1")
select= Select(multi_select)
select.select_by_value("volvox")
select.select_by_value("swiftx")
select.select_by_value("Hyundaix")
time.sleep(5)
multi_options=select.all_selected_options
for ele in multi_options:
    print(ele.text)
time.sleep(20)
driver.quit()'''


