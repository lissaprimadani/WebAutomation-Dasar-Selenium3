from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()

#driver.get("http://the-internet.herokuapp.com/login")
#driver.find_element_by_name("username").send_keys("Kadekc")
#driver.find_element_by_partial_link_text("Elemental").click()
#driver.find_element_by_class_name("radius").click()
#time.sleep(2)
#driver.find_element_by_css_selector("button.radius").click()
#time.sleep(3)
#driver.find_element_by_css_selector("#login > button").click()

driver.get("http://the-internet.herokuapp.com/add_remove_elements/")
#driver.find_element_by_css_selector("#content > div > button").click()
#driver.find_element_by_xpath('//*[@id="content"]/div/button').click()
driver.find_element(By.XPATH, '//*[@id="content"]/div/button').click()