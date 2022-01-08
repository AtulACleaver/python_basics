x = float(input("Dividend: "))
y = float(input("Divisor: "))

# Checking if the number is divisible
if x % y == 0:
    print(f"The number {x} is completely divisible by {y}.")
else:
    print(f"The number {x} is not completely divisible by {y}. So, lets make {x} divisible.")
    if x > y:
        reminder = x % y
        print(f"The new number that will be divisible by {y} is {x-reminder}.")
    else:
        print(f"The new number that will be divisible by {y} is {x+(y-x)}.")

