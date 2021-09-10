#import pandas as pd
#
#column_names = ["timer", "day1", "day2", "day3", "day4", "day5"]
#df = pd.read_csv("batch2tt.csv", names=column_names)
#print(df)
#
#letters = df.day2.to_list()
#print(letters[3])
##
#
from datetime import datetime
#import time
#
now = datetime.now()
current_time = now.strftime('%H:%M')
current = now.__format__("%H:%M")
class1 = datetime.strptime('09:00','%H:%M')
time1=class1.__format__("%H:%M")
class2 = datetime.strptime('08:30','%H:%M')
time2=class2.__format__("%H:%M")
class3 = datetime.strptime('09:00','%H:%M')
time3=class3.__format__("%H:%M")
class4 = datetime.strptime('09:00','%H:%M')
time4=class4.__format__("%H:%M")
class5 = datetime.strptime('09:00','%H:%M')
time5=class5.__format__("%H:%M")
print(current)

now = datetime.now()
current_time = now.strftime(' %H:%M ')
print(current_time)

print(now.strftime("%H:%M"))   # 2018/09/09
print(now.__format__("%H:%M")) 
current = now.__format__("%H:%M")
#time1 = datetime.time("09:00" )
class1 = datetime.strptime('09:00','%H:%M')
print(class1.__format__("%H:%M"))
time1=class1.__format__("%H:%M")

if (current > time1) & (current < datetime.strptime('')):
    print("hallayuh")




#from collections import UserDict, UserList
#import pandas 
#from datetime import datetime
#import time
#
#now = datetime.now()
#current_time = now.strftime("%H:%M")
#print(current_time)
#pandas_data = pd.read_csv('timetable.csv',usecols = ["2"])
#listdata = list(pandas_data)
#
#print(pandas_data)
#print(listdata)
#
#import csv
#with open('timetable.csv', 'r') as file:
#    csv_reader = csv.reader(file)
#    for l in csv_reader:
#        print(l[1])
#    print(list(csv.reader(file)))
#

## Read the csv file
#data = pd.read_csv('timetable(1).csv')
#
## Print it out if you want
#print(data)
#
#for row in data:
#  print(row[1])
#
##data = list(pd.read_csv('timetable(1).csv'))
##print(data[0])
#
#def select_index(index):
#    csv_file = open('timetable(1).csv', 'r')
#    csv_reader = csv.DictReader(csv_file)
#
#    for line in csv_reader:
#        l = line['Index']
#        if l == index:
#            print(line[' "Name"'])
#
#select_index('11')
#
#
##def read_cell(x, y):
##    with open('timetable(1).csv', 'r') as f:
##        reader = pd.read_csv(f)
##        y_count = 0
##        for n in reader:
##            if y_count == y:
##                cell = n[x]
##                return cell
##            y_count += 1
##
##print(read_cell(4,0))