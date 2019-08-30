from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import urllib.request
import requests


driver = webdriver.Chrome('chromedriver.exe')
driver.get('https://www.educosoft.com/Home/US/es_u_default.aspx')

email_element = driver.find_element_by_id('ctl00_escontent_txtUserName')
password_element = driver.find_element_by_id('ctl00_escontent_txtPassword')

email_element.send_keys('elugo38@email.suagm.edu')
password_element.send_keys('March301994!')

# Button ID = ctl00_escontent_btnGo

#response = requests.post("https://www.educosoft.com/Home/US/es_u_default.aspx",
#                        {'email': "elugo38@email.suagm.edu", 'password': "March301994!", 'drpCountry': "US"},
#                        verify=False)


#soup = BeautifulSoup(response.text, "html.parser")

#print(soup.prettify().encode("utf-8"))

#response = requests.post( "https://suagm.blackboard.com/webapps/login/", # URL form_data = 
#                   {'user_id': "elugo38", 'password': "March_30_1994!!"}, # form-data 
#                headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"}, # headers 
#                verify=False) # this simply disables SSL security check ) 
#soup = BeautifulSoup(response.text, "html.parser")

#print(soup.prettify().encode('utf-8')) # pretty prints the response HTML