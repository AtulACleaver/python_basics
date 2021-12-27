string = input("String: ")

rev = ""

for i in range(len(string)-1, -1, -1):
    rev += string[i]

if rev == string:
    print("The string is palindrome.")
else:
    print("The string is not palindrome.")
