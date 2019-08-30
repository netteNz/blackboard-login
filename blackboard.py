from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import urllib.request
import requests

driver = webdriver.Chrome(executable_path='C:/Windows/chromedriver.exe') # Add chromedriver.exe to your path

options = Options() # Adds additional options such as cookies
options.add_argument("user-data-dir=selenium") # Logs selenium output

driver = webdriver.Chrome(options=options)
driver.get('https://suagm.blackboard.com/webapps/login/') # Reach the login page


username = driver.find_element_by_id('user_id') # Username for login
password = driver.find_element_by_id('password') # Password

username.send_keys('YOURUSERNAME') # Send Keys
password.send_keys('YOURPASSWORD')

login = driver.find_element_by_xpath('//*[@id="entry-login"]') # Login
login.click()

#driver.get('https://suagm.blackboard.com/webapps/bb-social-learning-BBLEARN/execute/mybb?cmd=display&toolId=AlertsOnMyBb_____AlertsTool') # Notifications page




if __name__ == "__main__":
    pass