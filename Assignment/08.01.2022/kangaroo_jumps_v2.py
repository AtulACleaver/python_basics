pos_1 = int(input("Position of 1st kangaroo: "))
pos_2 = int(input("Position of 2nd kangaroo: "))

if pos_1 == pos_2:
    print("Stop wasting my time! The other kangaroo is right here!")
else:
    speed_1 = int(input("Speed of 1st kangaroo: "))
    speed_2 = int(input("Speed of 2nd kangaroo: "))

    # In this model, kangaroos can chase each other in any direction.
    r_s = abs(pos_2 - pos_1)
    if speed_1 > speed_2:
        r_v = speed_1 - speed_2
        hops = r_s / r_v
        if hops == int(hops):
            print(f"Number of hops needed for them to get together is {int(hops)}. Finally 🙂")
        else:
            print("No luck today! Numbers are not matching. They can never get together 😢.")
    else:
        r_v = speed_2 - speed_1
        hops = r_s / r_v
        if hops == int(hops):
            print(f"Number of hops needed for them to get together is {int(hops)}. Finally 🙂")
        else:
            print("No luck today! Numbers are not matching. They can never get together 😢.")

    # if pos_1 == pos_2:
    #     print("Both kangaroos are at the same position. So, no hops needed.")
    # elif pos_1 > pos_2:
    #     r_s = pos_2 - pos_1
    #     if speed_1 > speed_2:
    #         r_v = speed_2 - speed_1
    #         hops = r_s / r_v
    #         if hops == int(hops):
    #             print(f"No. of hops needed = {int(hops)}")
    #         else:
    #             print("No number of hops can let kangaroo 1 catch kangaroos 2.")
    #     else:
    #         print("No luck today! kangaroo 1 just went head of kangaroo 2.")
    # elif pos_2 > pos_1:
    #     r_s = pos_2 - pos_1
    #     if speed_1 > speed_2:
    #         r_v = speed_1 - speed_2
    #         hops = r_s / r_v
    #         if hops == int(hops):
    #             print(f"No. of hops needed = {int(hops)}")
    #         else:
    #             print("No luck today! kangaroo 1 just went head of kangaroo 2.")
    #     else:
    #         print("No number of hops can let kangaroo 1 catch kangaroos 2.")

    # elif speed_1 > speed_2:
    #     relative_speed = speed_1 - speed_2
    #     distance = pos_2 - pos_1
    #     print(f"Number of hops: " + str(distance/relative_speed))
    # else:
    #     relative_speed = speed_2 - speed_1
    #     distance = abs(pos_2 - pos_1)
    #     print(f"Number of hops: " + str(distance / relative_speed))
