# Combained conditions

age = int(input("Enter your age: "))

# first firm
''' 
if age>0:
    if age >= 18 and age <= 110:
        print("You are over age")
    else:
        print("You are a minor")
else:
    print("Wrong age")
'''

# correct shape
if age>0:
    if 18<=age<= 110:
        print("You are over age")
    else:
        print("You are a minor")
else:
    print("Wrong age")
