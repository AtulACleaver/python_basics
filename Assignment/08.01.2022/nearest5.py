num = int(input("Num = "))

if num % 10 == 5:
    print("The last digit of the number is already 5.")
elif num % 10 < 5:
    l_nearest_5 = num + (5-(num % 10))
    print(f"{l_nearest_5} is the nearest number with last digit as 5.")
elif num % 10 > 5:
    s_nearest_5 = num - ((num % 10) - 5)
    print(f"{s_nearest_5} is the nearest number with last digit as 5.")

