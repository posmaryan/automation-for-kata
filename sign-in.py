import time
from datetime import datetime

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(r'C:\Users\Posma Panggabean\PycharmProjects\chromedriver', options=chrome_options)
driver.implicitly_wait(30)

# test scenario verify invalid credentials
# isi email dan password yang salah
driver.get(
    "http://automationpractice.com/index.php?controller=authentication&back=my-account")
email = driver.find_element_by_id("email")
email.send_keys("jimhalpert@mailnesia.com")
passw = driver.find_element_by_id("passwd")
passw.send_keys("asdasd123")
# klik tombol sign in
driver.find_element_by_xpath(
    "//button[@id='SubmitLogin']/span").click()
# verifikasi alert muncul
driver.find_element_by_xpath('//*[@id="center_column"]/div[1]')

# test scenario sign in
driver.get(
    "http://automationpractice.com/index.php?controller=authentication&back=my-account")
# isi email dan password
email = driver.find_element_by_id("email")
email.send_keys("jimhalpert@mailinator.com")
passw = driver.find_element_by_id("passwd")
passw.send_keys("asdasd123")
# klik tombol sign in
driver.find_element_by_xpath(
    "//button[@id='SubmitLogin']/span").click()
# verifikasi apakah sudah berhasil login atau belum, dengan men-specify konten "Welcome to ..."
driver.find_element_by_xpath(
    "//div[@id='center_column']/p")
# close browser
driver.quit()