from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get("https://demoqa.com/alerts")
time.sleep(2)

#HandleAlertPertama
#driver.find_element_by_id("alertButton").click()
#time.sleep(2)
#driver.switch_to.alert.accept()


#HandleAlertKedua
#driver.find_element_by_id("confirmButton").click()
#time.sleep(2)
#buttonya kalau klik OK
#driver.switch_to.alert.accept()
#buttonnya kalau klik Batal
#driver.switch_to.alert.dismiss()

#HandleAlertKetiga
time.sleep(2)
driver.find_element_by_xpath('//*[@id="promtButton"]').click()

time.sleep(2)
driver.switch_to.alert.send_keys("saya sedang test")

time.sleep(2)
driver.switch_to.alert.accept()
