# Using date time module

from datetime import datetime

# Input date string
date_string = "14/09/2024 15:45:30"

# Format string matching the input
format_string = "%d/%m/%Y %H:%M:%S"

# Convert the string to a datetime object
datetime_object = datetime.strptime(date_string, format_string)

print("Datetime object:", datetime_object)
print("Type of datetime_object:", type(datetime_object))


import datetime

now = datetime.datetime.now()
print(now)

# Format the datetime object into a string
formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")

print(formatted_date)

# Using dateutil module

from dateutil import parser

date_time=parser.parse("Oct 13 1997 7:15 AM")
print(date_time)
print(type(date_time))