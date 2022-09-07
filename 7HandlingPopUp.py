from lib2to3.pgen2.driver import Driver
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
import time

for i in range (2):
    driver.get("https://tees.co.id")
    try:
        WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]')))
        print("Muncul pak")
        driver.find_element_by_class_name("btn-modal-close").click()
        print("pop up diclose")
    except TimeoutException:
        print("pop up tidak muncul pak")
        pass

    time.sleep(3)