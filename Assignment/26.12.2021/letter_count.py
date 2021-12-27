name = input("Name: ")

letter = []

for i in range(len(name)):
    if name[i] not in letter:
        letter.append(name[i])

for i in range(len(letter)):
    letter_count = f"{letter[i]} - "
    counter = 0
    for j in range(len(name)):
        if letter[i] == name[j]:
            counter += 1
    letter_count += str(counter)
    print(letter_count)

