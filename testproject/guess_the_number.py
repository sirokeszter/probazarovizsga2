# #Egy tesztet kell írnod ami addig találgat a megadott intervallumon belül amíg ki nem találja a helyes számot. Nem jár plusz pont azért ha úgy automatizálsz, hogy minnél optimálisabban és gyosabban találja ki a helyes számot a program
# Amikor megvan a helyes szám, ellenőrizd le, hogy a szükséges lépések száma mit az aplikáció kijelez egyezik-e a saját belső számlálóddal.
# Teszteld le, hogy az applikáció helyesen kezeli az intervallumon kívüli találgatásokat. Az applikéció -19 vagy 255 értéknél nem szabad, hogy összeomoljon. Azt kell kiírnia, hogy alá vagy fölé találtál-e.
#
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

options = Options()
# options.add_argument('--headless')
options.add_argument('--disable-gpu')
driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)

try:
    driver.get("https://witty-hill-0acfceb03.azurestaticapps.net/guess_the_number.html")
    time.sleep(2)

    # Select the locators:
    guess_input = driver.find_element_by_xpath('/html/body/div/div[2]/input')
    guess_btn = driver.find_element_by_xpath('/html/body/div/div[2]/span/button')
    restart_btn = driver.find_element_by_xpath('/html/body/div/div[1]/div[2]/button')
    good_alert = driver.find_element_by_xpath('/html/body/div/p[5]')
    bad_alert1 = driver.find_element_by_xpath('/html/body/div/p[3]')
    bad_alert2 = driver.find_element_by_xpath('/html/body/div/p[4]')

    for number in range(1, 100):
        guess_input.send_keys(number)
        guess_btn.click()
        if good_alert.text == 'Yes! That is it.':
            break
        else:
            guess_input.clear()
            number += 1

    # Check the number of guessing (it must be equal with the guessed number)
    number_of_guess = driver.find_element_by_xpath('/html/body/div/div[3]/p/span')
    assert number_of_guess == number

    # Check data under the period:
    time.sleep(1)
    restart_btn.click()
    time.sleep(2)
    for number in range(-19, 0):
        guess_input.send_keys(number)
        guess_btn.click()
        if bad_alert1.text != 'Guess higher.':
            break
        else:
            guess_input.clear()
            number += 1

    # Check data over the period:
    time.sleep(1)
    restart_btn.click()
    time.sleep(2)
    for number in range(100, 255):
        guess_input.send_keys(number)
        guess_btn.click()
        if bad_alert1.text != 'Guess lower.':
            break
        else:
            guess_input.clear()
            number += 1

finally:
    pass
    # driver.close()
