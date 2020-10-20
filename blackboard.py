from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import urllib.request
import requests

driver = webdriver.Chrome(executable_path='/usr/bin/chromedriver') # Add chromedriver.exe to your path
options = Options() # Adds additional options such as cookies
driver = webdriver.Chrome(options=options)


driver.get('https://suagm.blackboard.com/webapps/login/') # Reach the login page
cookies = driver.find_element_by_xpath('//*[@id="agree_button"]')
cookies.click()

username = driver.find_element_by_id('user_id') # Username for login
password = driver.find_element_by_id('password') # Password

username.send_keys('YOUR_USERNAME') # Send Keys
password.send_keys('YOUR_PASSWORD')

login = driver.find_element_by_xpath('//*[@id="entry-login"]') # Login
login.click()

#driver.get('https://suagm.blackboard.com/webapps/bb-social-learning-BBLEARN/execute/mybb?cmd=display&toolId=AlertsOnMyBb_____AlertsTool') # Notifications page




if __name__ == "__main__":
    pass
