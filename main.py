import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

SDAROT_URL = "https://www.sdarot.tw/watch/8249-%D7%90%D7%99%D7%A0%D7%A4%D7%99%D7%A0%D7%99%D7%98%D7%99-infiniti/season/1/episode/14"
DNS_URL = "chrome://settings/security?search=dns"

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(DNS_URL)
driver.maximize_window()
#driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
driver.execute_script("window.scrollTo(0, 500)")

done = False



driver.get(SDAROT_URL)
while not done:
    html_source = driver.page_source
    if "Not Available" in html_source:
        print('Not Available this time, f5 + sleeping 30 seconds.')
        driver.get(SDAROT_URL)  # refresh
        time.sleep(31)
    else:
        print('found!!')
        done = True

