n = int(input("Number: "))


def factorial(num):
    f = 1
    for i in range(1, num + 1):
        f = f * i
    return f


combination = factorial(n)
print(f"So, number of combination that can be formed = {combination}")
