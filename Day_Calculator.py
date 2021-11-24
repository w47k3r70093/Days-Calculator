def MONTHTODAYS():
    month = float(input("Enter the number of months you want to convert them into days : "))
    days = month * 30
    print(days)


def YEARSTODAY():
    year = float(input("Enter the number of years you want to convert them into days : "))
    days = year * 365
    print(days)

def HOURTODAYS():
    hour = float(input("Enter the number of hours you want to convert them into days : "))
    days = hour / 24
    print(days)

def WEEKTODAYS():
    week = float(input("Enter the number of weeks you want to convert them into days : "))
    days = week * 7
    print(days)

print("Please enter your choice from the following options : (1/2/3/4)")
print("1. Convert Month to Days")
print("2. Convert Years to Days")
print("3. Convert Hours to Days")
print("4. Convert Weeks to Days")

a = int(input("Please enter your choice ---->  "))
print(a)

if a == 1:
    MONTHTODAYS()
elif a == 2:
    YEARSTODAY()
elif a == 3:
    HOURTODAYS()
else:
    WEEKTODAYS()
