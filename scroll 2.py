from selenium import webdriver
import time

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.maximize_window()

driver.get("https://the-internet.herokuapp.com/")
time.sleep(1)

#scroll by element
element = driver.find_element(By.LINK_TEXT, "Form Authentication")
time.sleep(1)
driver.execute_script("arguments[0].scrollIntoView()", element)
time.sleep(1)

#scroll till end of the page
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
time.sleep(3)