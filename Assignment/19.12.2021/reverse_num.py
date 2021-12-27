num = int(input("Number: "))

reverse = 0


while num > 0:
    reminder = num % 10
    reverse = reverse * 10 + reminder
    num = int(num / 10)  # Also I can use // instead of /

print(f"The reverse of the number is {reverse}")
