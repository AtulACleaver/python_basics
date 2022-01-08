pos_1 = int(input("Position of 1st kangaroo: "))
pos_2 = int(input("Position of 2nd kangaroo: "))

speed_1 = int(input("Speed of 1st kangaroo: "))
speed_2 = int(input("Speed of 2nd kangaroo: "))

# In this model, kangaroo 1 is always chasing kangaroo 2

if pos_1 == pos_2:
    print("Both kangaroos are at the same position. So, no hops needed.")
elif pos_1 > pos_2:
    r_s = pos_2 - pos_1
    if speed_1 > speed_2:
        r_v = speed_2 - speed_1
        hops = r_s / r_v
        if hops == int(hops):
            print(f"No. of hops needed = {int(hops)}")
        else:
            print("No luck today! kangaroo 1 just went head of kangaroo 2.")
    else:
        print("No number of hops can let kangaroo 1 catch kangaroos 2.")
elif pos_2 > pos_1:
    r_s = pos_2 - pos_1
    if speed_1 > speed_2:
        r_v = speed_1 - speed_2
        hops = r_s / r_v
        if hops == int(hops):
            print(f"No. of hops needed = {int(hops)}")
        else:
            print("No luck today! kangaroo 1 just went head of kangaroo 2.")
    else:
        print("No number of hops can let kangaroo 1 catch kangaroos 2.")
