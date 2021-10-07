import time
from datetime import datetime

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(r'C:\Users\Posma Panggabean\PycharmProjects\chromedriver', options=chrome_options)
driver.implicitly_wait(30)

# test scenario
driver.get(
    "http://automationpractice.com/index.php?controller=authentication&back=my-account")
email = driver.find_element_by_id("email_create")
email.send_keys("dwightks@mailinator.com")
# klik tombol create account
driver.find_element_by_xpath(
    "//button[@id='SubmitCreate']/span").click()
driver.find_element_by_id("customer_firstname").send_keys("Dwight")
driver.find_element_by_id("customer_lastname").send_keys("Schrute")
driver.find_element_by_id("passwd").send_keys("asdasd123")
Select(driver.find_element_by_id("days")).select_by_visible_text("regexp:1\\s+")
Select(driver.find_element_by_id("months")).select_by_visible_text("regexp:January\\s")
Select(driver.find_element_by_id("years")).select_by_visible_text("regexp:2005\\s+")
driver.find_element_by_id("newsletter").click()
driver.find_element_by_id("optin").click()
driver.find_element_by_id("company").send_keys("dunder mifflin")
river.find_element_by_id("address1").send_keys("Scranton, Pennsylvania")
driver.find_element_by_id("city").send_keys("Scranton")
Select(driver.find_element_by_id("id_state")).select_by_visible_text("Pennsylvania")
driver.find_element_by_id("postcode").send_keys("12520")
driver.find_element_by_id("other").send_keys("Near Vance refrigeration")
driver.find_element_by_id("phone_mobile").send_keys("02178832788")
driver.find_element_by_xpath("//button[@id='submitAccount']/span").click()
driver.find_element_by_xpath("//div[@id='center_column']/p").click()

# close browser
driver.quit()