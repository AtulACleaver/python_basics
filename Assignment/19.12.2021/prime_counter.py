num = int(input("Number= "))

counter = 0
total_primes = 0

# This will go from 2 to input number
for j in range(2, num):
    # This is a checker for prime number
    for i in range(2, j):
        if j % i == 0:
            counter += 1
    if counter == 0:
        total_primes += 1
    counter = 0

print(f"Total primes between 1 and {num} = {total_primes}")
