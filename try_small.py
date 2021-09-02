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
email="pk1459@srmist.edu.in"
pas="Rasu@2001"

#installing webdrivers of chrome
driver_path = "/Users/pushpesh/auto_mac/chromedriver"
driver = webdriver.Chrome(driver_path)

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("disable-popup-blocking")
webdriver.Chrome(os.path.join(driver_path, 'chromedriver'),  chrome_options=chrome_options)

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

diss_btn = driver.find_element_by_xpath("/html/body/div/div[3]/div/div[2]/div[3]/div/span/span")
diss_btn.click()
#count=0
#while (count<3):
#    count+=1
#    press('esc')

time.sleep(2)

asktojoin=driver.find_element_by_xpath("/html/body/div[1]/c-wiz/div/div/div[9]/div[3]/div/div/div[4]/div/div/div[2]/div/div[2]/div/div[1]/div[1]/span")
asktojoin.send_keys(Keys.ENTER)
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