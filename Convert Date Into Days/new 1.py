import datetime
import time

#Setting the date format
ud = input("Enter a date: ")
print("The day of the selcted date is:")
print(datetime.datetime.strptime(ud, '%d/%m/%Y').strftime('%A'))

time.sleep (3)