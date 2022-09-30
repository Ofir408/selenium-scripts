import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

SDAROT_URL = "https://www.sdarot.tw/watch/8249-%D7%90%D7%99%D7%A0%D7%A4%D7%99%D7%A0%D7%99%D7%98%D7%99-infiniti/season/1/episode/14"
DNS_URL = "chrome://settings/security?search=dns"

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(DNS_URL)
driver.maximize_window()
#driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#driver.execute_script("window.scrollTo(0, 500)")

driver.execute_script("alert('set dns to CleanBrowsing (Family Filter)');")
time.sleep(15)

driver.execute_script("window.scrollTo(0, 500)")
driver.implicitly_wait(2)
time.sleep(1)
#link = driver.find_element_by_link_text("Custom")
#link.click()
done = False

driver.get(SDAROT_URL)

while "ברוך שובך" not in driver.page_source:
    print('waiting to ברוך שובך...')
    time.sleep(5)

while not done:
    time.sleep(36)
    html_source = driver.page_source
    if "כל שרתי הצפייה שלנו עמוסים" in html_source:
        print('Not Available this time, f5 + sleeping 30 seconds.')
        driver.get(SDAROT_URL)  # refresh

    elif "נגן את הפרק" in html_source:
        print('found!!')
        done = True
        time.sleep(60 * 3 * 60)  # you can watch the for 3 hours.
