arr = [2, 7, 4, 1, 5, 3]
sorted_arr = []

for i in range(len(arr)):
    min_e = arr[0]
    for j in range(len(arr)):
        if arr[j] < min_e:
            min_e = arr[j]
    sorted_arr.append(min_e)
    arr.remove(min_e)

print(sorted_arr)
