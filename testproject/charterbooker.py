## 4 Feladat: charterbooker automatizálása
# * Teszteld le a többoldalas formanyomtatvány működését.
# * Ellenőrizd a helyes kitöltésre adott választ: "Your message was sent successfully. Thanks! We'll be in touch as soon as we can, which is usually like lightning (Unless we're sailing or eating tacos!)."
# * Készíts tesztesetet az e-mail cím validációjára.


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
import time

options = Options()
# options.add_argument('--headless')
options.add_argument('--disable-gpu')
driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)

try:
    driver.get("https://witty-hill-0acfceb03.azurestaticapps.net/charterbooker.html")
    time.sleep(2)

    # Locators:
    # 1. page
    select1 = Select(driver.find_element_by_xpath('//*[@id="step1"]/ul/li[1]/select'))
    next_btn1 = driver.find_element_by_xpath('//*[@id="step1"]/ul/li[2]/button')
    # 2. page
    datapicker = driver.find_element_by_xpath('//*[@id="step2"]/ul/li[1]/input')
    select2 = Select(driver.find_element_by_xpath('//*[@id="step2"]/ul/li[2]/select'))
    select3 = Select(driver.find_element_by_xpath('//*[@id="step2"]/ul/li[3]/select'))
    next_btn2 = driver.find_element_by_xpath('//*[@id="step2"]/ul/li[4]/button')
    # 3. page
    fullname = driver.find_element_by_xpath('//*[@id="step3"]/ul/li[1]/input')
    email = driver.find_element_by_xpath('//*[@id="step3"]/ul/li[2]/input')
    msg = driver.find_element_by_xpath('//*[@id="step3"]/ul/li[3]/textarea')
    request_btn3 = driver.find_element_by_xpath('//*[@id="step3"]/ul/li[4]/button')

    # Test the full form
    # 1. page
    select1.select_by_value('1')
    next_btn1.click()
    time.sleep(2)
    # 2. page
    datapicker.send_keys('2010')
    select2.select_by_value('Morning')
    select3.select_by_value('3')
    time.sleep(1)
    next_btn2.click()
    time.sleep(2)
    # 3. page
    fullname.send_keys('John Smith')
    email.send_keys('johnsmith@gmail.com')
    msg.send_keys('-')
    request_btn3.click()
    time.sleep(3)

    # Check the alert text:
    alert = driver.find_element_by_xpath('//*[@id="booking-form"]/h2')
    assert alert.text == "Your message was sent successfully. Thanks! We'll be in touch as soon as we can, which is usually like lightning (Unless we're sailing or eating tacos!)."

    # Check valid email address
    driver.get("https://witty-hill-0acfceb03.azurestaticapps.net/charterbooker.html")
    time.sleep(3)

    # 1. page
    select1.select_by_value('2')
    next_btn1.click()
    time.sleep(2)
    # 2. page
    datapicker.send_keys('2010')
    select2.select_by_value('Morning')
    select3.select_by_value('3')
    time.sleep(1)
    next_btn2.click()
    time.sleep(2)
    # 3. page
    fullname.send_keys('John Smith')
    email.send_keys('johnsmith@')
    msg.send_keys('-')
    request_btn3.click()
    time.sleep(3)

    assert driver.find_element_by_id('bf_email-error').text == "PLEASE ENTER A VALID EMAIL ADDRESS."
finally:
    pass
    # driver.close()
