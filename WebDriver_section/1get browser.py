from selenium import webdriver
import time

driver=webdriver.Chrome()  #to use which browser  #Chrome(executable_path="path")

driver.get("https://terralogic.paxanimi.ai/ticket-management/detail/66ec53ebad3f0a7db776c3d1")   #to launch browser
print(driver.title)    # prints browser title
driver.maximize_window() # enlarge window size
time.sleep(8)
driver.close()
#OR

'''from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())'''




