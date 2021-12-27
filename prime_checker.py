num = int(input("Number = "))

counter = 0

for i in range(2, num):
    if num % i == 0:
        counter += 1

if num == 1:
    print("The number is neither prime nor consonant.")
elif counter == 0:
    print("The number is prime.")

else:
    print("The number is not prime.")
