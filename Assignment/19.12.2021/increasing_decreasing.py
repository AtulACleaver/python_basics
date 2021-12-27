# With Stars
star = "* "

for i in range(1, 6):
    print(star * i)

for i in reversed(range(1, 6)):
    print(star * i)

# With Numbers

# To get:
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3
# 1 2
# 1

for i in range(2, 7):
    line = ""
    for j in range(1, i):
        line += str(j) + " "
    print(line)

for i in reversed(range(2, 7)):
    line = ""
    for j in range(1, i):
        line += str(j) + " "
    print(line)
