# degree f to degree c
def degftoc(f):
    c = 5 / 9 * (f - 32)
    return round(c, 2)


# get the table of any number
def get_table(n):
    for i in range(1, 11):
        result = n * i
        return str(n) + " x " + str(i) + " = " + str(result)


# Leap year checker
def leap_check(year):

    if year % 400 == 0:
        return "The number is a leap year."
    elif year % 100 != 0 and year % 4 == 0:
        return "The number is a leap year."
    else:
        return "The number is not a leap year."


# Even Odd
def evod(num):
    if num % 2 == 0:
        return "The number is even."
    else:
        return "The number is odd."


# positive negative
def pos_neg(num):
    if num > 0:
        return "The number " + str(num) + " is positive."
    elif num < 0:
        return "The number " + str(num) + " is negative."
