import time
import smtplib
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from email.mime.multipart import MIMEMultipart

EPISODE_REQEST = 'Enter episode number: '
EPISODE_INPUT = input(EPISODE_REQEST)
SDAROT_URL = "https://www.sdarot.tw/watch/8249-%D7%90%D7%99%D7%A0%D7%A4%D7%99%D7%A0%D7%99%D7%98%D7%99-infiniti/season/1/episode/"+ EPISODE_INPUT
RECEIVER_ADDRESS = input('Enter mail address: ')
MAIL_CONTENT = "Enjoy! the episode is ready for you :)"
SENDER_Address = "cohen.alon213@gmail.com"
SENDER_PASS = "qgybdizygidotuhn"
SDAROT_USER = "loli213"
SDAROT_PASS = "loli213"
LOGIN_XPATH = '//*[@id="slideText"]/p/button'
USER_XPATH = '//*[@id="loginForm"]/form/div[1]/div/input'
PASSWORD_XPATH = '//*[@id="loginForm"]/form/div[2]/div/input'
LOGIN_BUTTON_XPATH = '//*[@id="loginForm"]/form/div[4]/button'


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(SDAROT_URL)
driver.maximize_window()
#driver.execute_script("alert('set dns to CleanBrowsing (Family Filter)');")
#time.sleep(10)

login = driver.find_element(By.XPATH, LOGIN_XPATH)
login.click()
driver.find_element(By.XPATH, USER_XPATH).send_keys(SDAROT_USER)
driver.find_element(By.XPATH, PASSWORD_XPATH).send_keys(SDAROT_PASS)
login_button = driver.find_element(By.XPATH, LOGIN_BUTTON_XPATH)
time.sleep(1)
login_button.click()
time.sleep(15)
done = False

while not done:
   time.sleep(36)
   html_source = driver.page_source
   if "כל שרתי הצפייה שלנו עמוסים" in html_source:
       print('Not Available this time, f5 + sleeping 30 seconds.')
       driver.get(SDAROT_URL)  # refresh

   elif "נגן את הפרק" in html_source:
      print('found!!')
      done = True

message = MIMEMultipart()
message['From'] = SENDER_Address
message['To'] = RECEIVER_ADDRESS
message['Subject'] = MAIL_CONTENT

session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
session.starttls() #enable security
session.login(SENDER_Address, SENDER_PASS) #login with mail_id and password
text = message.as_string()
session.sendmail(SENDER_Address, RECEIVER_ADDRESS, text)
session.quit()

time.sleep(60 * 3 * 60)  # you can watch the for 3 hours.
