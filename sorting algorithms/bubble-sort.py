arr = [2, 7, 4, 1, 5, 3]


#     [2, 6, 1, 2, 6, 0, 1, 9]
def bubble_sort(t_list):
    for i in range(len(t_list)-1):
        k = i-1
        for j in range(len(t_list)-2-k):
            if t_list[j] > t_list[j+1]:
                swap = t_list[j]
                t_list[j] = t_list[j+1]
                t_list[j+1] = swap
    return t_list


print(bubble_sort(arr))
