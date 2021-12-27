name = input("Name: ")

letter = []

# Converting name into letters
for i in range(len(name)):
    letter.append(name[i])

vowels = ['a', 'e', 'i', 'o', 'u']

vowels_counter = 0
consonant_counter = 0

for i in range(len(letter)):
    if letter[i] in vowels:
        vowels_counter += 1
    else:
        consonant_counter += 1

print(f"There are {vowels_counter} vowels in the word. \nThere are {consonant_counter} consonants in the word.")
