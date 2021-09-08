import time
from pyautogui import press
from selenium import webdriver
from webdriver_manager import driver
from webdriver_manager.chrome import ChromeDriverManager

import keyboard
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

#simulating the mobile agents

opts= Options()
opts.add_argument("--user-agent=Mozilla/5.0 (Linux; Android 7.0; SM-G930V Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36")
driver = webdriver.Chrome(ChromeDriverManager().install(), options=opts)

email="emailid@gmail.com"
pas="password_for_the_email"

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

opts.add_experimental_option("excludeSwitches", ["disable-popup-blocking"])

press('esc')

time.sleep(2)

press('esc')

diss_btn = driver.find_element_by_xpath("/html/body/div/div[3]/div/div[2]/div[3]/div/span/span")
diss_btn.click()
#count=0
#while (count<3):
#    count+=1
#    press('esc')

time.sleep(2)

asktojoin=driver.find_element_by_xpath("/html/body/div[1]/c-wiz/div/div/div[9]/div[3]/div/div/div[4]/div/div/div[2]/div/div[2]/div/div[1]/div[1]/span")
asktojoin.send_keys(Keys.ENTER)