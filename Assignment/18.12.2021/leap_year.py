counter = 0

for i in range(2001, 2101):
    if i % 400 == 0:
        counter += 1
    elif i % 100 != 0 and i % 4 == 0:
        counter += 1

print(counter)
