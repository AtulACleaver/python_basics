total_numbers = int(input("Input the last number you want: "))

odd_counter = 0
even_counter = 0

smallest_odd = 1
smallest_even = 0
largest_odd = 1
largest_even = 0


while total_numbers >= 0:
    if total_numbers % 2 == 0:
        even_counter += 1
        if smallest_even > total_numbers:
            smallest_even = total_numbers
        if largest_even < total_numbers:
            largest_even = total_numbers
    else:
        odd_counter += 1
        if smallest_odd > total_numbers:
            smallest_odd = total_numbers
        if largest_odd < total_numbers:
            largest_odd = total_numbers

    total_numbers -= 1

n_even = (largest_even - smallest_even) / 2 + 1
if n_even == even_counter:
    print("Even loop is correct.")
else:
    print("Even loop is not correct.")

n_odd = (largest_odd - smallest_odd)/2 + 1
if n_odd == odd_counter:
    print("Odd loop is correct.")
else:
    print("Odd loop is not correct.")

print("Total odd numbers are: " + str(odd_counter))
print("Smallest odd number is: " + str(smallest_odd))
print("Largest odd number is: " + str(largest_odd))
print("Total even numbers are: " + str(even_counter))
print("Largest even number is: " + str(largest_even))
print("Smallest even number is: " + str(smallest_even))
