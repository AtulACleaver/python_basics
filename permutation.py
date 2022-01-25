# Find the number of combination if the number is given but the spaces are less than the number
num = int(input("Number = "))
spaces = int(input("Spaces = "))

permutation = 1

for i in range(spaces):
    permutation = permutation * (num-i)

print(f"Permutation = {permutation}")
