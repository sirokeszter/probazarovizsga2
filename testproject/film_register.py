from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

options = Options()
# options.add_argument('--headless')
options.add_argument('--disable-gpu')
driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)

try:
    driver.get("https://witty-hill-0acfceb03.azurestaticapps.net/film_register.html")
    time.sleep(2)

    # Teszteld le, hogy betöltés után megjelennek filmek az alkalmazásban, méghozzá 24 db.
    # Make a list from films by xpath and check the length of the list
    films = driver.find_elements_by_xpath('/html/body/div[2]/div[3]/a')
    assert len(films) == 24

    # Teszteld le, hogy fel lehet-e venni az alábbi adatokkal egy új filmet:
    # #     * Film title: Black widow
    # #     * Release year: 2021
    # #     * Chronological year of events: 2020
    # #     * Trailer url: https://www.youtube.com/watch?v=Fp9pNPdNwjI
    # #     * Image url: https://m.media-amazon.com/images/I/914MHuDfMSL._AC_UY327_FMwebp_QL65_.jpg
    # #     * Film summary: https://www.imdb.com/title/tt3480822/

    # Fulfill input fields:
    register_btn = driver.find_element_by_xpath('/html/body/div[2]/div[1]/button').click()
    time.sleep(1)
    title = driver.find_element_by_id('nomeFilme').send_keys('Black widow')
    release_year = driver.find_element_by_id('anoLancamentoFilme').send_keys('2021')
    cron_year = driver.find_element_by_id('anoCronologiaFilme').send_keys('2020')
    trailer = driver.find_element_by_id('linkTrailerFilme').send_keys('https://www.youtube.com/watch?v=Fp9pNPdNwjI')
    image = driver.find_element_by_id('linkImagemFilme').send_keys(
        'https://m.media-amazon.com/images/I/914MHuDfMSL._AC_UY327_FMwebp_QL65_.jpg')
    sum_url = driver.find_element_by_id('linkImdbFilme').send_keys('https://www.imdb.com/title/tt3480822/')
    save_btn = driver.find_element_by_xpath('/html/body//fieldset/button[1]').click()
    time.sleep(2)

    # Check again the length of the list:
    films = driver.find_elements_by_xpath('/html/body/div[2]/div[3]/a')
    assert len(films) == 25

finally:
    pass
    # driver.close()
