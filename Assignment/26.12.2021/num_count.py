a = [0, 0, 0, 1, 1, 2]

b = []

for i in range(len(a)):
    if a[i] not in b:
      b.append(a[i])

print(b)
print(len(b))
