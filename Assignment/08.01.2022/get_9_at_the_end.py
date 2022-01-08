num = float(input("num = "))

# We need to get:
# 4 = [4.9, 4.99, 4.999]
# 4.3 = [4.3, 4.39, 4.399]
# 4.34 = [4.34, 4.34, 4.349]

if num == int(num):
    res_1 = num + 0.9
    res_2 = res_1 + 0.09
    res_3 = res_2 + 0.009
    print(f"{res_1} \n{res_2}\n{res_3}")
elif num == round(num, 1):
    res_1 = num
    res_2 = res_1 + 0.09
    res_3 = res_2 + 0.009
    print(f"{res_1} \n{res_2}\n{res_3}")
elif num == round(num, 2):
    res_1 = num
    res_2 = num
    res_3 = res_2 + 0.009
    print(f"{res_1} \n{res_2}\n{res_3}")
else:
    print(f"{num} \n{num} \n{num}")
