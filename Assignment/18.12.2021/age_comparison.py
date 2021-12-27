computer_age = 12

person_name = (input("What is your name? "))
person_age = int(input("What is your age? "))
person_gender = (input("What is your gender? "))

if computer_age < person_age:
    if person_gender == "Male" or person_gender == "male":
        print(f"Hi, {person_name}, you are {person_age - computer_age} years older than me. I have to call you {person_name} bhaia.")
    elif person_gender == "Female" or person_gender == "Female":
        print(f"Hi, {person_name}, you are {person_age - computer_age} years older than me. I have to call you {person_name} didi.")
else:
    if person_gender == "Male" or person_gender == "male":
        print(f"Hi, {person_name}, you are {computer_age - person_age} years younger than me. You can to call me computer bhaia.")
    elif person_gender == "Female" or person_gender == "Female":
        print(f"Hi, {person_name}, you are {computer_age - person_age} years younger than me. You can to call me computer didi.")
