from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.maximize_window()

driver.get("https://the-internet.herokuapp.com/")
time.sleep(1)

#scroll by pixel
driver.execute_script("window.scrollBy(0,110)"," ")
time.sleep(2)

