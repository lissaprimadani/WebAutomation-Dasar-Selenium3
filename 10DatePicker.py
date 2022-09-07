from lib2to3.pgen2 import driver
from time import time
from selenium import webdriver
import time
import pyautogui

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()

#alamat1
# driver.get('https://jqueryui.com/datepicker/')
#cara1
#driver.switch_to.frame(driver.find_element_by_xpath('//*[@id="content"]/iframe'))
#driver.find_element_by_id("datepicker").click()
#driver.find_element_by_xpath('//*[@id="ui-datepicker-div"]/table/tbody/tr[2]/td[6]/a').click()

# cara2 dengan send key
# driver.switch_to.frame(driver.find_element_by_xpath('//*[@id="content"]/iframe'))
# driver.find_element_by_id("datepicker").send_keys('02/01/2022')
# time.sleep(3)
# driver.find_element_by_id("datepicker").clear()


#alamat2 pakek gui
driver.get('https://demoqa.com/date-picker/')
driver.find_element_by_id('datePickerMonthYearInput').click()
pyautogui.press('backspace',presses=10)
time.sleep(3)
driver.find_element_by_id('datePickerMonthYearInput').send_keys('02/021/2022')
