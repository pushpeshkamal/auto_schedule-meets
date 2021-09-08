#Importing all the libraries 
import selenium
import keyboard
from pyautogui import press
import time
import os

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

#loading the data reuired as the credentials
email="email id"
pas="password"

#installing webdrivers of chrome
driver_path = "/Users/pushpesh/auto_mac/chromedriver"
driver = webdriver.Chrome(driver_path)

from selenium.webdriver.chrome.options import Options

#altenative methidds i searched from stackoverflow

#chrome_options = webdriver.ChromeOptions()
#chrome_options.add_argument("--disable-notifications")
#webdriver.Chrome(os.path.join(driver_path, '/Users/pushpesh/auto_mac/chromedriver'), chrome_options=chrome_options)

#option = Options()
#option.add_argument("--disable-notifications")
#
##option.add_argument("--disable-infobars")
##option.add_argument("start-maximized")
###option.add_argument("--disable-extensions")##

### Pass the argument 1 to allow and 2 to block
#option.add_experimental_option("prefs", {  "profile.default_content_setting_values.notifications": 1 })#

#driver = webdriver.Chrome(chrome_options=option, executable_path='/Users/pushpesh/auto_mac/chromedriver')
#driver.get('https://www.facebook.com')
#chrome_options = webdriver.ChromeOptions()
#chrome_options.add_argument("disable-popup-blocking")
#webdriver.Chrome(os.path.join(driver_path, 'chromedriver'),  chrome_options=chrome_options)

#chrome_options.add_argument("--disable-popup-blocking")
#chrome_prefs = {}
#chrome_options.add_argument("--disable-popup-blocking")
#chrome_prefs = {}
#chrome_options.experimental_options["prefs"] = chrome_prefs
#chrome_prefs["profile.default_content_settings"] = { "popups": 1 }
#chrome_options.add_experimental_option("excludeSwitches", ["--disable-popup-blocking"])
#chrome_options.experimental_options["prefs"] = chrome_prefs
#chrome_prefs["profile.default_content_settings"] = { "popups": 1 }
#chrome_options.add_experimental_option("excludeSwitches", ["--disable-popup-blocking"])
opt = Options()
opt.add_argument("--disable-infobars")
opt.add_argument("start-maximized")
opt.add_argument("--disable-extensions")
opt.add_argument("--start-maximized")
# Pass the argument 1 to allow and 2 to block
opt.add_experimental_option("prefs", { \
    "profile.default_content_setting_values.media_stream_mic": 1, 
    "profile.default_content_setting_values.media_stream_camera": 1,
    "profile.default_content_setting_values.geolocation": 1, 
    "profile.default_content_setting_values.notifications": 1 
  })

driver = webdriver.Chrome(chrome_options=opt , executable_path='/Users/pushpesh/auto_mac/chromedriver')

#driver.maximize_window()

driver.get("https://accounts.google.com/signin/v2/identifier?ltmpl=meet&continue=https%3A%2F%2Fmeet.google.com%3Fhs%3D193&&o_ref=https%3A%2F%2Fmeet.google.com%2F_meet%2Fwhoops%3Fsc%3D232%26alias%3Dmymeetingraheel&_ga=2.262670348.1240836039.1604695943-1869502693.1604695943&flowName=GlifWebSignIn&flowEntry=ServiceLogin")

email_input =driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input")
email_input.send_keys(email)

press('enter')
#keyboard.send("enter", do_press=True, do_release=True)
#next_btn = driver.find_element_by_link_text('Next') #_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/span")
#next_btn.send_keys(Keys.ENTER)

time.sleep(2)
pas_input = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input")
pas_input.send_keys(pas)

press('enter')
time.sleep(2)

link = open("schedule_meets.txt","r").read()
#print(link)

driver.get(link)
link_input = driver.find_element_by_xpath("/html/body/c-wiz/div/div[2]/div/div[1]/div[3]/div/div[2]/div[1]/label/input")
link_input.send_keys("fnq-orad-fwv")

time.sleep(2)

#press('esc')

time.sleep(2)

#press('esc')

driver.switch_to_frame(driver.find_element_by_xpath("/html/body/div/div[3]/div/div[2]/div[3]/div/span/span"))  
press('enter')
#diss_btn.click()
#count=0
#while (count<3):
#    count+=1
#    press('esc')

time.sleep(2)

#asktojoin=driver.find_element_by_xpath("/html/body/div[1]/c-wiz/div/div/div[9]/div[3]/div/div/div[4]/div/div/div[2]/div/div[2]/div/div[1]/div[1]/span")
#asktojoin.send_keys(Keys.ENTER)
#for i in range(2):
#    for i in range(3):
#        press('tab')
#    press('enter')
#



#class meet_bot:
#    def join(driver,meetlink):
#        driver.get(meetlink)
#        driver.bot.find_element_by_xpath("/html/body/div/div[3]/div/div[2]/div[3]/div/span/span")
#        keyboard.send("tab", do_press=True, do_release=True)

#
#obj =meet_bot()
#obj.join(link)