# Python datetime

import datetime

print(dir(datetime))

# Getting datetime Information

from datetime import datetime

now = datetime.now()
print(now)
day = now.day
month = now.month
year = now.year
hour = now.hour
minute = now.minute
second = now.second
timestamp = now.timestamp()
print(day, month, year, hour, minute, second, timestamp)
print('timestamp', timestamp)
print(f'{day}/{month}/{year}, {hour}:{minute}')

# Formatting Date Output Using strftime

from datetime import datetime

new_year = datetime(2024, 8, 7)
print(new_year)
day = new_year.day
month = new_year.month
year = new_year.year
hour = new_year.hour
minute = new_year.minute
second = new_year.second
print(day, month, year, hour, minute)
print(f'{day}/{month}/{year}, {hour}:{minute}')

from datetime import datetime

now = datetime.now()
t = now.strftime("%H:%M:%S")
print("time:", t)
time_one = now.strftime("%m/%d/%Y, %H:%M:%S")
print("time one:", time_one)
time_two = now.strftime("%d/%m/%Y, %H:%M:%S")
print("time two:", time_two)

# String to Time Using strptime


# Using date from datetime

from datetime import date

today = date.today()
print(today)
print("current Year :  ", today.year)
print("current Month :  ", today.month)
print("current Day :  ", today.day)

# Time Objects to Represent Time

from datetime import time

a = time()
print("a =", a)
b = time(10, 30, 50)
print("b =", b)
c = time(hour=10, minute=30, second=50)
print("c =", c)
d = time(10, 30, 50, 200555)
print("d =", d)

# Difference Between Two Points in Time Using

today = date(year=2019, month=12, day=5)
new_year = date(year=2020, month=1, day=1)
time_left_for_newyear = new_year - today

print('Time left for new year: ', time_left_for_newyear)

t1 = datetime(year=2019, month=12, day=5, hour=0, minute=59, second=0)
t2 = datetime(year=2020, month=1, day=1, hour=0, minute=0, second=0)
diff = t2 - t1
print('Time left for new year:', diff)

# Difference Between Two Points in Time Using timedelta

from datetime import timedelta

t1 = timedelta(weeks=12, days=10, hours=4, seconds=20)
t2 = timedelta(days=7, hours=5, minutes=3, seconds=30)
t3 = t1 - t2
print("t3 =", t3)

# Exercises: Day 16

# Get the current day, month, year, hour, minute and timestamp from datetime module

from datetime import datetime

now = datetime.now()
print(now)
day = now.day
month = now.month
year = now.year
hour = now.hour
minute = now.minute
second = now.second
timestamp = now.timestamp()
print(day, month, year, hour, minute, second, timestamp)

# Format the current date using this format: "%m/%d/%Y, %H:%M:%S")

from datetime import datetime

now = datetime.now()
t = now.strftime("%m/%d/%Y, %H:%M:%S")
print("time:", t)

# Today is 5 December 2019. Change this time string to time.

from datetime import datetime

date_string = "5 December 2019"
date_object = datetime.strptime(date_string, "%d %B %Y")
print(date_object)

# Calculate the time difference between now and new year.

from datetime import datetime

now = datetime.now()
new_year = datetime(now.year + 1, 1, 1)
time_difference = new_year - now
print(f"Time until New Year: {time_difference}")

# Calculate the time difference between 1 January 1970 and now.

from datetime import datetime

epoch = datetime(1970, 1, 1)
now = datetime.now()
time_difference = now - epoch
print("Diffrence is : ", time_difference)

# Think, what can you use the datetime module for? Examples:

# Time series analysis

from datetime import datetime, timedelta

start_date = datetime(2023, 1, 1)
dates = [start_date + timedelta(days=i) for i in range(10)]  # 10 days of data
values = range(10)

for date, value in zip(dates, values):
    print(f"Date: {date.strftime('%Y-%m-%d')}, Value: {value}")


# To get a timestamp of any activities in an application


# Record an activity with a timestamp
def log_activity(description):
    timestamp = datetime.now()
    print(f"Activity: {description}, Timestamp: {timestamp.strftime('%Y-%m-%d %H:%M:%S')}")


log_activity("User logged in")
log_activity("File uploaded")

# Adding posts on a blog

from datetime import datetime

post_date = datetime(2024, 8, 7)
print(f"Blog post scheduled for: {post_date.strftime('%Y-%m-%d')}")
