# Feladatod, hogy leteszteld, hogy az alábbi sorrendben jelennek-e meg az elemek a weblapon:
# (az alábbi tartalmat írd ki kézzel egy data.txt nevű fileba és onnan olvassa fel a kódod a tesztadatot)


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
    driver.get("https://witty-hill-0acfceb03.azurestaticapps.net/periodic_table.html")
    time.sleep(2)

    # List the elements of the periodic table and make a :
    periodic_list=[]
    periodic_elements= driver.find_elements_by_xpath('/html/body/div/ul/li/span')
    for e in periodic_elements:
        periodic_list.append(e.text)

    print(periodic_list)

    # Read the rows from the data.txt (dictionaryban lett volna érdemes kigyűjteni, de erre már nem volt időm)
    txt_list=[]
    with open('data.txt', 'r') as f:
        contents = f.readlines()
        for i in f:
            txt_list.append(i)
    print(txt_list)

    # Compare the lists:
    assert periodic_list == txt_list


finally:
    pass
    # driver.close()