lists = [1, 12, 2, 9, 4, 3, 13, 14, 22, 0]

max_num = 0

for i in range(0, len(lists)):
    if lists[i] > max_num:
        max_num = lists[i]

print(f"The maximum number from this list is {max_num}")
