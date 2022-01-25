n = int(input("Number of people: "))


# Same person cannot handshake again

# def handshake(people):
#     r = 2
#     f_people = 1
#     # people factorial
#     for i in range(1, people + 1):
#         f_people = f_people * i
#     f_people_r = 1
#     for i in range(1, people-r+1):
#         f_people_r = f_people_r * i
#     # create the formula now
#     return f_people/(r * f_people_r)
#
#
#
# print(handshake(n))

def factorial(num):
    f = 1
    for i in range(1, num + 1):
        f = f * i
    return f


handshakes = factorial(n)/(factorial(2) * (factorial(n-2)))

print(f"No. of handshakes: {handshakes}")
