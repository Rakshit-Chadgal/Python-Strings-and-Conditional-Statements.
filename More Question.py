#Q1: Accept gender from user and print a greeting message.
'''
gender = str(input("Enter your gender (M for Male, F for Female):"))
if gender == "M" or gender == "m":
    print("Good Morning Sir")
else:
    print("Good Morning Ma'am")
'''
#Q2: Accept a year and check if it is a leap year.
'''
year = int(input("Enter a year: "))
if year % 4 == 0:
    print(year,"is the leap year")
else:
    print(year,"is not a leap year")
'''
#Q3: Accept temperature in °C and print a description.
'''
Temp = int(input("Enter the temperature: "))
if Temp <= 5:
    print("It's Freezing Cold 🥶")
elif Temp in range(6, 17):
    print("It's Cold 🤒")
elif Temp in range(18,30):
    print("It's pleasant 😁🍄‍🟫")
elif Temp > 29:
    print("It's Hot 🔥🥵")
else:
    print("I dont know")
'''
#Q4: 