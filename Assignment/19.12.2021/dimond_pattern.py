#      *
#     * *
#    * * *
#   * * * *
#  * * * * *
# * * * * * *
#  * * * * *
#   * * * *
#    * * *
#     * *
#       *

star = "* "
space = " "

for i in range(1, 6):
    line = ""
    line += (space * (5 - i)) + star * i
    print(line)
for i in reversed(range(1, 6)):
    line = ""
    line += (space * (5 - i)) + star * i
    print(line)

for i in range(2, 7):
    line = (space * (6 - i))
    for j in range(1, i):
        line += str(j) + " "
    print(line)
for i in reversed(range(2, 7)):
    line = (space * (6 - i))
    for j in range(1, i):
        line += str(j) + " "
    print(line)
