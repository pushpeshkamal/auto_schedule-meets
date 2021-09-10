# importing all the libraries required 

import selenium
import keyboard
from pyautogui import press
import time
import os
import schedule
import pandas as pd

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from datetime import datetime

#loading the data reuired as the credentials

email="use your email id"
pas="password"

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def login(email,pas):
  #login URL
  driver.get("https://accounts.google.com/signin/v2/identifier?service=classroom&passive=1209600&continue=https%3A%2F%2Fclassroom.google.com%2F%3Femr%3D0&followup=https%3A%2F%2Fclassroom.google.com%2F%3Femr%3D0&flowName=GlifWebSignIn&flowEntry=ServiceLogin")

  email_input =driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input")
  email_input.send_keys(email)
  press('enter')
  time.sleep(2)

  pas_input = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input")
  pas_input.send_keys(pas)
  press('enter')
  time.sleep(4)


def joinmeet():
    time.sleep(4)
    driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[5]/div[1]/div/div[2]/div[2]/div/span/a/div").click()
    time.sleep(2)

    #new tab after copying the URL
    driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 't') 
    time.sleep(3)

    #mic off
    press('tab')
    press('tab')
    press('tab')
    press('tab')
    press('tab')
    press('enter')

    #micoff= driver.find_element_by_xpath("/html/body/div/c-wiz/div/div/div[9]/div[3]/div/div/div[4]/div/div/div[1]/div[1]/div/div[4]/div[1]/div/div/div/span/span/div/div[1]/div/svg")
    #micoff().click()
    time.sleep(1)

    #join now / ask to join
    press('tab')
    press('tab')
    press('tab')
    press('tab')
    press('tab')
    press('enter')
    #joinnow = driver.find_element_by_xpath("/html/body/div[1]/c-wiz/div/div/div[9]/div[3]/div/div/div[4]/div/div/div[2]/div/div[2]/div/div[1]/div[1]/span/span")
    #joinnow.click()
    time.sleep(4)
    print('\x1b[6;30;46m'+" << succesfully meeting joined >>"+ '\x1b[0m')
    #driver.find_element_by_xpath("/html/body/div[1]/c-wiz/div/div/div[9]/div[3]/div/div/div[4]/div/div/div[2]/div/div[2]/div/div[1]/div[1]/span/span").click()
    #time.sleep(2)
    #driver.find_elements_by_class_name("l4V7wb Fxmcue").click()
    #time.sleep(2)
  

def classroom():
  driver.get("https://classroom.google.com/h")
  time.sleep(8)


# XPATHS for the classes according to inspect element (you can just accordingly)
def classli(argument):
    switch = {
      0: "/html/body/div[2]/div[1]/div[6]/div/ol/li[1]/div[1]/div[3]/h2/a[1]/div[1]" ,#AWS
      2: "/html/body/div[2]/div[1]/div[6]/div/ol/li[2]/div[1]/div[3]/h2/a[1]/div[1]" ,#FLAT
      3: "/html/body/div[2]/div[1]/div[6]/div/ol/li[3]/div[1]/div[3]/h2/a[1]/div[1]" ,#ANN
      4: "/html/body/div[2]/div[1]/div[6]/div/ol/li[4]/div[1]/div[3]/h2/a[1]/div[1]" ,#CV
      5: "/html/body/div[2]/div[1]/div[6]/div/ol/li[5]/div[1]/div[3]/h2/a[1]/div[1]" ,#ALTS
      6: "/html/body/div[2]/div[1]/div[6]/div/ol/li[6]/div[1]/div[3]/h2/a[1]/div[1]" ,#MATHS
      7: "/html/body/div[2]/div[1]/div[6]/div/ol/li[6]/div[1]/div[3]/h2/a[1]/div[1]" ,#CN_LAB
      8: "/html/body/div[2]/div[1]/div[6]/div/ol/li[8]/div[1]/div[3]/h2/a[1]/div[1]" ,#CN
      9: "/html/body/div[2]/div[1]/div[6]/div/ol/li[9]/div[1]/div[3]/h2/a[1]/div[1]" ,#CSP_II
      10: "/html/body/div[2]/div[1]/div[6]/div/ol/li[10]/div[1]/div[3]/h2/a[1]/div[1]", #INDIAN TRADITIONAL KNOWLEDGE
      11: "/html/body/div[2]/div[1]/div[6]/div/ol/li[11]/div[1]/div[3]/h2/a[1]/div[1]", #WASTE TO WEALTH TO WHEELS
      12: "/html/body/div[2]/div[1]/div[6]/div/ol/li[12]/div[1]/div[3]/h2/a[1]/div[1]", #INDUSTRIAL TRAINING
    }
    return switch.get(argument,"unknown")



def classmeet(x):  # sourcery no-metrics
 
  now = datetime.now()
  current_time = now.strftime('%H:%M')
  current = now.__format__("%H:%M")

  class1 = datetime.strptime('09:10','%H:%M')
  time1=class1.__format__("%H:%M")

  class2 = datetime.strptime('11:00','%H:%M')
  time2=class2.__format__("%H:%M")

  class3 = datetime.strptime('13:30','%H:%M')
  time3=class3.__format__("%H:%M")

  class4 = datetime.strptime('14:20','%H:%M')
  time4=class4.__format__("%H:%M")

  class5 = datetime.strptime('15:10','%H:%M')
  time5=class5.__format__("%H:%M")
  

  #excel timetable

  column_names = ["timer", "day1", "day2", "day3", "day4", "day5"]
  df = pd.read_csv("batch2tt.csv", names=column_names)

  dayorder1 = df.day1.to_list()
  dayorder2 = df.day2.to_list()
  dayorder3 = df.day3.to_list()
  dayorder4 = df.day4.to_list()
  dayorder5 = df.day5.to_list()
  

  # classroom operations
  #using time instead of schedule cuz its wasnt working as decided schedule comands listed in main fucntion can be checked out too
  if (x==1):
    if (current <= time1):
      classroom()
      driver.find_element_by_xpath(classli(dayorder1[0])).click()
      joinmeet()
      time.sleep(6600)

    if (current <= time2) & (current > time1):
      driver.execute_script('window.open("https://classroom.google.com/h","_blank")')
      time.sleep(4)
      window_after_class1 =  driver.window_handles[-2]
      driver.switch_to.window(window_after_class1)
      time.sleep(3)
      #classroom()
      driver.find_element_by_xpath(classli(dayorder1[1])).click()
      joinmeet()
      time.sleep(9000)

    if (current <= time3) & (current > time2):
      w_class2 = driver.window_handles[0]
      driver.switch_to.window(w_class2)
      time.sleep(3)
      classroom()
      driver.find_element_by_xpath(classli(dayorder1[2])).click()
      joinmeet()
      time.sleep(3000)

    if (current <= time4) & (current > time3):
      driver.execute_script('''window.open("https://classroom.google.com/h","_blank");''')
      win_3 = driver.window_handles[-2]
      driver.switch_to.window(win_3)
      time.sleep(3)
      #classroom()
      driver.find_element_by_xpath(classli(dayorder1[3])).click()
      joinmeet()
      time.sleep(3000)

    if (current <= time5) & (current >= time4):
      window_after_class4 = driver.window_handles[0]
      driver.switch_to.window(window_after_class4) 
      time.sleep(3)

      classroom()
      driver.find_element_by_xpath(classli(dayorder1[4])).click() 
      joinmeet()

    print("day 1 class ended")

  elif (x==2):
    if (current <= time1):
      classroom()
      driver.find_element_by_xpath(classli(dayorder2[0])).click()
      joinmeet()
      time.sleep(6600)

    if (current <= time2) & (current > time1):
      driver.execute_script('window.open("https://classroom.google.com/h","_blank")')
      time.sleep(4)
      window_after_class1 =  driver.window_handles[-2]
      driver.switch_to.window(window_after_class1)
      time.sleep(3)
      #classroom()
      driver.find_element_by_xpath(classli(dayorder2[1])).click()
      joinmeet()
      time.sleep(9000)

    if (current <= time3) & (current > time2):
      w_class2 = driver.window_handles[0]
      driver.switch_to.window(w_class2)
      time.sleep(3)
      classroom()
      driver.find_element_by_xpath(classli(dayorder2[2])).click()
      joinmeet()
      time.sleep(3000)

    if (current <= time4) & (current > time3):
      driver.execute_script('''window.open("https://classroom.google.com/h","_blank");''')
      win_3 = driver.window_handles[-2]
      driver.switch_to.window(win_3)
      time.sleep(3)
      #classroom()
      driver.find_element_by_xpath(classli(dayorder2[3])).click()
      joinmeet()
      time.sleep(3000)

    if (current <= time5) & (current >= time4):
      window_after_class4 = driver.window_handles[0]
      driver.switch_to.window(window_after_class4) 
      time.sleep(3)

      classroom()
      driver.find_element_by_xpath(classli(dayorder2[4])).click() 
      joinmeet()

    print("day 2 class ended")
  
  elif (x==3):
    if (current <= time1):
      classroom()
      driver.find_element_by_xpath(classli(dayorder3[0])).click()
      joinmeet()
      time.sleep(6600)

    if (current <= time2) & (current > time1):
      driver.execute_script('window.open("https://classroom.google.com/h","_blank")')
      time.sleep(4)
      window_after_class1 =  driver.window_handles[-2]
      driver.switch_to.window(window_after_class1)
      time.sleep(3)
      #classroom()
      driver.find_element_by_xpath(classli(dayorder3[1])).click()
      joinmeet()
      time.sleep(9000)

    if (current <= time3) & (current > time2):
      w_class2 = driver.window_handles[0]
      driver.switch_to.window(w_class2)
      time.sleep(3)
      classroom()
      driver.find_element_by_xpath(classli(dayorder3[2])).click()
      joinmeet()
      time.sleep(3000)

    if (current <= time4) & (current > time3):
      driver.execute_script('''window.open("https://classroom.google.com/h","_blank");''')
      win_3 = driver.window_handles[-2]
      driver.switch_to.window(win_3)
      time.sleep(3)
      #classroom()
      driver.find_element_by_xpath(classli(dayorder3[3])).click()
      joinmeet()
      time.sleep(3000)

    if (current <= time5) & (current >= time4):
      window_after_class4 = driver.window_handles[0]
      driver.switch_to.window(window_after_class4) 
      time.sleep(3)

      classroom()
      driver.find_element_by_xpath(classli(dayorder3[4])).click() 
      joinmeet()

    print("day 3 class ended")

  elif (x==4):
    if (current <= time1):
      classroom()
      driver.find_element_by_xpath(classli(dayorder4[0])).click()
      joinmeet()
      time.sleep(6600)

    if (current <= time2) & (current > time1):
      driver.execute_script('window.open("https://classroom.google.com/h","_blank")')
      time.sleep(4)
      window_after_class1 =  driver.window_handles[-2]
      driver.switch_to.window(window_after_class1)
      time.sleep(3)
      #classroom()
      driver.find_element_by_xpath(classli(dayorder4[1])).click()
      joinmeet()
      time.sleep(9000)

    if (current <= time3) & (current > time2):
      w_class2 = driver.window_handles[0]
      driver.switch_to.window(w_class2)
      time.sleep(3)
      classroom()
      driver.find_element_by_xpath(classli(dayorder4[2])).click()
      joinmeet()
      time.sleep(3000)

    if (current <= time4) & (current > time3):
      driver.execute_script('''window.open("https://classroom.google.com/h","_blank");''')
      win_3 = driver.window_handles[-2]
      driver.switch_to.window(win_3)
      time.sleep(3)
      #classroom()
      driver.find_element_by_xpath(classli(dayorder4[3])).click()
      joinmeet()
      time.sleep(3000)

    if (current <= time5) & (current >= time4):
      window_after_class4 = driver.window_handles[0]
      driver.switch_to.window(window_after_class4) 
      time.sleep(3)

      classroom()
      driver.find_element_by_xpath(classli(dayorder4[4])).click() 
      joinmeet()

    print("day 4 class ended")
  
  elif (x==5):
    if (current <= time1):
      classroom()
      driver.find_element_by_xpath(classli(dayorder5[0])).click()
      joinmeet()
      time.sleep(6600)

    if (current <= time2) & (current > time1):
      driver.execute_script('window.open("https://classroom.google.com/h","_blank")')
      time.sleep(4)
      window_after_class1 =  driver.window_handles[-2]
      driver.switch_to.window(window_after_class1)
      time.sleep(3)
      #classroom()
      driver.find_element_by_xpath(classli(dayorder5[1])).click()
      joinmeet()
      time.sleep(9000)

    if (current <= time3) & (current > time2):
      w_class2 = driver.window_handles[0]
      driver.switch_to.window(w_class2)
      time.sleep(3)
      classroom()
      driver.find_element_by_xpath(classli(dayorder5[2])).click()
      joinmeet()
      time.sleep(3000)

    if (current <= time4) & (current > time3):
      driver.execute_script('''window.open("https://classroom.google.com/h","_blank");''')
      win_3 = driver.window_handles[-2]
      driver.switch_to.window(win_3)
      time.sleep(3)
      #classroom()
      driver.find_element_by_xpath(classli(dayorder5[3])).click()
      joinmeet()
      time.sleep(3000)

    if (current <= time5) & (current >= time4):
      window_after_class4 = driver.window_handles[0]
      driver.switch_to.window(window_after_class4) 
      time.sleep(3)

      classroom()
      driver.find_element_by_xpath(classli(dayorder5[4])).click() 
      joinmeet()

    print("day 2 class ended")
 


if __name__=="__main__":
  # To prompt the user to input an integer we do the following:
  valid = False
  while not valid: #loop until the user enters a valid int
      try:
          x = int(input(bcolors.OKBLUE +'Enter TODAYs Day Order (1-5): '+ '\x1b[0m' + bcolors.ENDC))
          valid = True #if this point is reached, x is a valid int
      except ValueError:
          print(bcolors.OKCYAN+'Please only input digits'+bcolors.ENDC)
  


  #installing webdrivers of chrome
  # driver_path = "/Users/pushpesh/auto_mac/chromedriver"
  # driver = webdriver.Chrome(driver_path)

  #disabling notifications, alers by using experimental features

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
  
  #PLSSS input the locatin of chromedrivers in the execultable path directory
  driver = webdriver.Chrome(options= opt , executable_path='/Users/pushpesh/auto_mac/chromedriver')
  # to maximize the browser window
  #driver.maximize_window()
  



  #operations by calling functions
  #login( email,pas )

  if (x < 6):
    #operations by calling functions
    login( email,pas )
    classmeet(x)
  else:
    print('\x1b[6;30;41m'+" < Error 404 > Day-Order not found !"+'\x1b[0m')
  

  print('\x1b[6;30;42m'+" >>  succesfully completed >> "+'\x1b[0m')
  #schedule.every().day.at("09:03").do(classmeet,x)
  #schedule.every().day.at("10:53").do(classmeet(x))
  #schedule.every().day.at("13:23").do(classmeet(x))
  #schedule.every().day.at("14:13").do(classmeet(x))
  #schedule.every().day.at("15:03").do(classmeet(x))
  

  #endcall= driver.find_element_by_xpath("/html/body/div[1]/c-wiz/div[1]/div/div[9]/div[3]/div[10]/div[2]/div/div[7]/span/button")
  #endcall.click()
  time.sleep(10)
  driver.quit()




