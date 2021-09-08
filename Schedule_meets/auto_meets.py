# importing all the libraries required 

import selenium
import keyboard
from pyautogui import press
import time
import os

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


#installing webdrivers of chrome

driver_path = "/Users/pushpesh/auto_mac/chromedriver"
driver = webdriver.Chrome(driver_path)

#loading the data reuired as the credentials

email="pls load your email id out here"
pas="pls load your pssword over here"

#disabling notifications, alers by using experimental features

opt = Options()
opt.add_argument("--disable-infobars")
opt.add_argument("start-maximized")
opt.add_argument("--disable-extensions")
opt.add_argument("--start-maximized")
# Pass the argument 1 to allow and 2 to block
opt.add_experimental_option("prefs", { \
    "profile.default_content_setting_values.media_stream_mic": 1
    , 
    "profile.default_content_setting_values.media_stream_camera": 1,
    "profile.default_content_setting_values.geolocation": 1, 
    "profile.default_content_setting_values.notifications": 1 
  })

driver = webdriver.Chrome(options= opt , executable_path='/Users/pushpesh/auto_mac/chromedriver')


#login URL

driver.get("https://accounts.google.com/signin/v2/identifier?ltmpl=meet&continue=https%3A%2F%2Fmeet.google.com%3Fhs%3D193&&o_ref=https%3A%2F%2Fmeet.google.com%2F_meet%2Fwhoops%3Fsc%3D232%26alias%3Dmymeetingraheel&_ga=2.262670348.1240836039.1604695943-1869502693.1604695943&flowName=GlifWebSignIn&flowEntry=ServiceLogin")

email_input =driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input")
email_input.send_keys(email)
press('enter')
time.sleep(2)

pas_input = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input")
pas_input.send_keys(pas)
press('enter')
time.sleep(2)

#scheduled meets 

link = open("meetlink.txt","r").read()#pls do write down the meeting link out here
#print(link)


driver.get(link) #or just put your meet link out here

#link_input = driver.find_element_by_xpath("/html/body/c-wiz/div/div[2]/div/div[1]/div[3]/div/div[2]/div[1]/label/input")
#link_input.send_keys("fnq-orad-fwv")
#time.sleep(2)
press('enter')
time.sleep(2)

# for muting mic
# for mac users pls use system preferces configured for vscode and google chrome to access
press('tab')
press('tab')
press('tab')
press('tab')
press('enter')

#alternative for mic off
#micoff= driver.find_element_by_xpath("/html/body/div/c-wiz/div/div/div[9]/div[3]/div/div/div[4]/div/div/div[1]/div[1]/div/div[4]/div[1]/div/div/div/span/span/div/div[1]/div/svg")
#micoff().click()
time.sleep(2)

#for pausing video (as of for other than mac) 
#for macs by default system prefernce blocks it up
#press('tab')
#press('tab')
#press('tab')
#press('tab')
#press('enter')

#alternative for mic off
#micoff= driver.find_element_by_xpath("/html/body/div/c-wiz/div/div/div[9]/div[3]/div/div/div[4]/div/div/div[1]/div[1]/div/div[4]/div[1]/div/div/div/span/span/div/div[1]/div/svg")
#micoff().click()
#time.sleep(2)

#join now / ask to join 
press('tab')
press('tab')
press('tab')
press('tab')
press('tab')
press('enter')

#alternative for join now or ask to join button
#joinnow = driver.find_element_by_xpath("/html/body/div[1]/c-wiz/div/div/div[9]/div[3]/div/div/div[4]/div/div/div[2]/div/div[2]/div/div[1]/div[1]/span/span")
#joinnow.click()
time.sleep(2)

