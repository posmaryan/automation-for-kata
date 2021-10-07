import time
from datetime import datetime

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select

chrome_options = Options()
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(r'C:\Users\Posma Panggabean\PycharmProjects\chromedriver', options=chrome_options)
driver.implicitly_wait(30)

# test scenario
driver.get(
    "http://automationpractice.com/index.php?controller=authentication&back=my-account")
# input email
driver.find_element_by_id(
    "email_create").send_keys("ryanhoward@mailinator.com")
# klik tombol create account
driver.find_element_by_xpath(
    "//button[@id='SubmitCreate']/span").click()
# mengisi first name dan last name
driver.find_element_by_id(
    "customer_firstname").send_keys("Ryan")
driver.find_element_by_id(
    "customer_lastname").send_keys("Howard")
# membuat password
driver.find_element_by_id(
    "passwd").send_keys("asdasd123")
# memilih tanggal - bulan - tahun lahir
SelectDate = Select(driver.find_element_by_id(
    "days"))
SelectDate.select_by_index(6)
SelectMonth = Select(driver.find_element_by_id(
    "months"))
SelectMonth.select_by_index(6)
SelectYear = Select(driver.find_element_by_id(
    "years"))
SelectYear.select_by_index(6)
# memilih checkbox newsletter dan special offers
driver.find_element_by_id(
    "newsletter").click()
driver.find_element_by_id(
    "optin").click()
driver.find_element_by_id(
    "company").send_keys("dunder mifflin")
driver.find_element_by_id(
    "address1").send_keys("Scranton, Pennsylvania")
driver.find_element_by_id(
    "city").send_keys("Scranton")
SelectState = Select(driver.find_element_by_id(
    "id_state"))
SelectState.select_by_index(6)
driver.find_element_by_id(
    "postcode").send_keys("12520")
driver.find_element_by_id(
    "other").send_keys("Near Vance refrigeration")
driver.find_element_by_id(
    "phone_mobile").send_keys("02178832788")
# submit pembuatan akun
driver.find_element_by_xpath(
    "//button[@id='submitAccount']/span").click()
# verifikasi apakah sudah berhasil automatic login atau belum, dengan men-specify konten "Welcome to ..."
driver.find_element_by_xpath(
    "//div[@id='center_column']/p").click()
# close browser
driver.quit()