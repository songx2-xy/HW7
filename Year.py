def Year(y):
    if y%4==0 and y%100==0 and y%400==0:
        return "Leap Year"
    else:
        return "Not Leap Year"
print(Year(2001))
print(Year(2000))