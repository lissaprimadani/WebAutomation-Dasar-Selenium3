from selenium import webdriver
import pyautogui
import time

driver = webdriver.Chrome()

#Alamat1
#driver.get("https://demoqa.com/upload-download")
#driver.find_element_by_id("uploadFile").send_keys("C:/Users/Lissa/Downloads/automasi/pdfdummy.pdf")

#Alamat2
driver.get("https://gofile.io/uploadFiles")
driver.find_element_by_xpath('//*[@id="rowUploadButton"]/div/div/div/div/div/div[1]/div/button').click()
time.sleep(3)
pyautogui.write(r"C:\UsersLissa\Downloads\automasi\pdfdummy.pdf")
pyautogui.press("enter")