import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

URL = "https://www.sdarot.tw/watch/8249-%D7%90%D7%99%D7%A0%D7%A4%D7%99%D7%A0%D7%99%D7%98%D7%99-infiniti/season/1/episode/14"

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(URL)
done = False

while not done:
    html_source = driver.page_source
    if "סדרות" not in html_source:
        print("Selenium didnt get reach the correct page. exit!")
        exit(-1)

    if "Not Available" in html_source:
        print('Not Available this time, f5 + sleeping 30 seconds.')
        driver.get(URL)  # refresh
        time.sleep(31)
    else:
        print('found!!')
        done = True

