from selenium import webdriver
from selenium.webdriver.support.ui import Select
import pyautogui

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get('https://demoqa.com/select-menu')

# #old style selection
# pilih = Select(driver.find_element_by_id('oldSelectMenu'))
# bytext
# pilih.select_by_visible_text('Yellow')
# by value
# pilih.select_by_value('10')


# #select one with typing
# driver.find_element_by_id('selectOne').click()
# pyautogui.typewrite('Prof.')
# pyautogui.press('enter')

#multi select
driver.find_element_by_css_selector("#selectMenuContainer > div:nth-child(7) > div > div > div > div.css-1hwfws3 > div.css-1wa3eu0-placeholder").click()
pyautogui.typewrite('Green')
pyautogui.press('enter')
driver.find_element_by_css_selector("#selectMenuContainer > div:nth-child(7) > div > div > div > div.css-1hwfws3 > div.css-1wa3eu0-placeholder").click()
pyautogui.typewrite('Black')
pyautogui.press('enter')

