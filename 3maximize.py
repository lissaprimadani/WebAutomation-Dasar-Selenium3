from selenium import webdriver

driver = webdriver.Chrome()

driver.get("http://the-internet.herokuapp.com/login")
#driver.maximize_window()
driver.minimize_window()