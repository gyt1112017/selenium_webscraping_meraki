from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common import action_chains, keys
import time

# login meraki by using selenium
browser = webdriver.Chrome('C:/Program Files (x86)/Google/Chrome/Application/chromedriver.exe')
# navigate the broswer to event log
browser.get('https://n210.meraki.com/London-ChinaTown/n/kHeSwdsd/manage/dashboard/event_log')
action = webdriver.ActionChains(browser)
emailElem = browser.find_element_by_id('email')
emailElem.send_keys('your email')
PasswdElem = browser.find_element_by_id('password')
PasswdElem.send_keys('your password')
loginButton = browser.find_element_by_id('commit')
loginButton.click()
select = browser.find_element_by_id('event_type_include_chosen')
select.click()

# choose the event type is Splash authentication
Splash = browser.find_element_by_xpath("//li[@class='active-result group-option'][21]")
Splash.click()
SearchBotton = browser.find_element_by_xpath("//input[@type='submit']")
SearchBotton.click()
time.sleep(5)

# download the event log which type is Splash authentication as CSV file
DownloadButton = browser.find_element_by_xpath("//div[@class='btn-group']")
CSV = browser.find_element_by_xpath("//ul[@class='dropdown-menu pull-left']//li//a")
DownloadButton.click()
CSV.click()

#  press the old button which is one the top right
OlderButton = browser.find_element_by_xpath("//a[@class='older_link']")

# continuly download
count = 0
while (count < 10000):     
    count = count + 1
    OlderButton.click()
    time.sleep(5)
    DownloadButton.click()
    CSV.click()
