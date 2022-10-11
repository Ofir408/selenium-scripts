import time
import smtplib
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from email.mime.multipart import MIMEMultipart

SERIES_REQUEST = 'Enter series name'
SERIES_INPUT = input(SERIES_REQUEST)
SEASON_MESSAGE = 'Insert season number: '
SEASON_INPUT = input(SEASON_MESSAGE)
EPISODE_REQUEST = 'Enter episode number: '
EPISODE_INPUT = input(EPISODE_REQUEST)
SDAROT_URL = "https://www.sdarot.tw/"
RECEIVER_ADDRESS = input('Enter mail address: ')
MAIL_CONTENT = "Enjoy! the episode is ready for you :)"
SENDER_Address = "cohen.alon213@gmail.com"
SENDER_PASS = "qgybdizygidotuhn"
SDAROT_USER = "loli213"
SDAROT_PASS = "loli213"
SEARCH_XPATH = '//*[@id="liveSearch"]'
SEARCH_BUTTON_XPATH = '//*[@id="mainSearch"]/div/span/button/span'
SERIES_XPATH = '//*[@id="seriesList"]/div[2]/div[1]/div[1]'
LOGIN_XPATH = '//*[@id="slideText"]/p/button'
USER_XPATH = '//*[@id="loginForm"]/form/div[1]/div/input'
PASS_XPATH = '//*[@id="loginForm"]/form/div[2]/div/input'
LOGIN_BUTTON_XPATH = '//*[@id="loginForm"]/form/div[4]/button'
WATCH_SHOW_XPATH = '//*[@id="seriesList"]/div[2]/div[1]/div[1]/div/a/span'
SEASON_XPATH = '//*[@id="season"]/li['+SEASON_INPUT+']'
EPISODE_MESSAGE = 'Insert episode number: '
EPISODE_XPATH = '//*[@id="episode"]/li['+ EPISODE_INPUT+']'
PASSWORD_XPATH = '//*[@id="loginForm"]/form/div[2]/div/input'


######################## Set driver ###########################################
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(SDAROT_URL)
driver.maximize_window()
#driver.execute_script("alert('set dns to CleanBrowsing (Family Filter)');")
#time.sleep(10)

########################## Login ##############################################
login = driver.find_element(By.XPATH, LOGIN_XPATH)
login.click()
driver.find_element(By.XPATH, USER_XPATH).send_keys(SDAROT_USER)
driver.find_element(By.XPATH, PASSWORD_XPATH).send_keys(SDAROT_PASS)
login_button = driver.find_element(By.XPATH, LOGIN_BUTTON_XPATH)
login_button.click()

########################## Search serirs ######################################

driver.find_element(By.XPATH, SEARCH_XPATH).send_keys(SERIES_INPUT)
search_button = driver.find_element(By.XPATH, SEARCH_BUTTON_XPATH)
search_button.click()

if "תוצאות חיפוש" in driver.page_source:
    action_chains = ActionChains(driver)
    series = driver.find_element(By.XPATH, SERIES_XPATH)
    action_chains.move_to_element(series).perform()
    driver.find_element(By.XPATH, WATCH_SHOW_XPATH).click()

######################## Search season & episode ##############################
season = driver.find_element(By.XPATH, SEASON_XPATH)
season.click()
episode = driver.find_element(By.XPATH, EPISODE_XPATH)
episode.click()

###################### Refresh until episode is ready #########################
done = False
while not done:
    time.sleep(36)
    html_source = driver.page_source
    if "כל שרתי הצפייה שלנו עמוסים" in html_source:
        print('Not Available this time, f5 + sleeping 30 seconds.')
        driver.refresh()

    elif "נגן את הפרק" in html_source:
        print('found!!')
        done = True

################################ Send email ###################################
message = MIMEMultipart()
message['From'] = SENDER_Address
message['To'] = RECEIVER_ADDRESS
message['Subject'] = MAIL_CONTENT
session = smtplib.SMTP('smtp.gmail.com', 587)  # use gmail with port
session.starttls()  # enable security
session.login(SENDER_Address, SENDER_PASS)  # login with mail_id and password
text = message.as_string()
session.sendmail(SENDER_Address, RECEIVER_ADDRESS, text)
session.quit()

time.sleep(60 * 3 * 60)  # you can watch the for 3 hours.
