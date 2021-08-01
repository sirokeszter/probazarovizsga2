# Teszteld le, hogy a különböző szűrőfeltételek alapján megfelelő karaktereket mutatja az oldal.
# Tehát mondjuk `iceman` pontosan az `original` és a `factor` csapatban van benne és a `hellfire` illetve a `force` csapatokban nincs benne.
import pprint

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
import time

options = Options()
# options.add_argument('--headless')
options.add_argument('--disable-gpu')
driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)

try:
    driver.get("https://witty-hill-0acfceb03.azurestaticapps.net/mutant_teams.html")
    time.sleep(2)

    # Select team locators
    original_team = driver.find_element_by_id('original')
    force_team = driver.find_element_by_id('force')
    factor_team = driver.find_element_by_id('factor')
    hellfire_team = driver.find_element_by_id('hellfire')

    # Click origonal teams:
    original_team.click()
    time.sleep(1)

    # Select all the characters to a list and make an other from the teams membership (data-teams)
    data_list1 = []
    data_list2 = []
    characters = driver.find_elements_by_xpath('/html/body/div/ul/li')
    for data in characters:
        data_list1.append(data.get_attribute('data-teams'))
    characters_name = driver.find_elements_by_xpath('/html/body/div/ul/li/h2')
    for name in characters_name:
        data_list2.append(name.text)

    # Make a dictionary from the two lists, to check the membership
    marvel_dictionary = dict(zip(data_list2, data_list1))

    pprint.pprint(marvel_dictionary)

    # Check Iceman
    assert marvel_dictionary[3] == {'Iceman': 'original factor'}

finally:
    pass
    # driver.close()