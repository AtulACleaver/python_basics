# # Decimal to binary
# for i in range(16):
#     binary = ""
# #   0000 0001 0010 0011 0100 0101 0110
#     while i > 0:
#         reminder = i % 2
#         binary = str(reminder) + binary
#         i = i//2
#     binary = ('0' * (4-len(binary))) + binary
#     print(binary)

# Decimal to any base
base_10 = int(input("Decimal: "))
base = int(input("Base: "))

ans = ""
while base_10 > 0:
    reminder = base_10 % base
    ans = str(reminder) + ans
    base_10 = base_10//base

if ans == '':
    print('0')

print(ans)
