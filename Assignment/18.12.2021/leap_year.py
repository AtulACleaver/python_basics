num = int(input("Write a number: "))

if num % 400 == 0:
    print("The number is a leap year.")
elif num % 100 != 0 and num % 4 == 0:
    print("The number is a leap year.")
else:
    print("The number is not a leap year.")
