#implement re module in python

import re

data = input("Enter email or mobile number: ")

email_pattern = r'^[a-zA-Z0-9.%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
mobile_pattern = r'^[0-9]{10}$'

if re.fullmatch(email_pattern, data):
    print("Valid email id")
elif re.fullmatch(mobile_pattern, data):
    print("Valid mobile number")
else:
    print("Invalid email or mobile number")
    
