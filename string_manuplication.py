# a = "Shubham"
#
# # for i in range(len(a)):
# #     print(a[i])
#
# reverse = ""
# for i in range(len(a)-1, -1, -1):
#     # reverse += a[i]
#     print(i)
#
# print(reverse)

# for i in range(len(a)):
#     print(a[len(a)-1-i])

name = input("Name= ")

for i in reversed(range(len(name)+1)):
    line = ""
    for j in range(i):
        line += name[j]
    print(line)

for i in range(len(name), 0, -1):
    print(name[0:i])
