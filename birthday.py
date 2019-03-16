
from datetime import *

#Get Today's Date
today = date.today()
print("Today: " +  today.strftime('%A %d, %b %Y'))

dob_str = input("What is your Date of Birth? dd/mm/yyyy ")
#Convert user input into a date
dob_data = dob_str.split("/")
dobDay = int(dob_data[0])
dobMonth = int(dob_data[1])
dobYear = int(dob_data[2])
dob = date(dobYear,dobMonth,dobDay)

numberOfDays = (today - dob).days 

age = numberOfDays // 365
print("You are " + str(age) + " years old.")
if age>100:
    print("Wow, you're old!")
elif age==0:
    print("Welcome to the world, kid!")

day = dob.strftime("%A")
print("You were born on a " + day + ".")

print("You have spent " + str(numberOfDays) + " days on Earth.")

thisYear = today.year

nextBirthday = date(thisYear,dobMonth,dobDay)
if today<nextBirthday:
  gap = (nextBirthday - today).days
  print("Your birhday is in " + str(gap) + " days.")
  print("Maybe you should try this again then?")
elif  today == nextBirthday:
  print("Today is your birthday! Happy Birthday, Sam!")
  import webbrowser
  webbrowser.open('https://www.youtube.com/watch?v=jc6VOnBYxDg')
else:
  nextBirthday = date(thisYear+1,dobMonth,dobDay)
  gap = (nextBirthday - today).days
  print("Your birthday is in " + str(gap) + " days.")
  print("Maybe you should try this again then?")
