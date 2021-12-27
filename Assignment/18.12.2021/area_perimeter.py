shape = input("Which shape do you want area & perimeter of? ")

if shape.casefold() == "square".casefold():
    side = float(input("Length of the side = "))

    print("The perimeter of the square is " + str(side*4))
    print("The area of the square is " + str(side**2))

elif shape.casefold() == "circle".casefold():
    radius = float(input("Radius of the side = "))

    print("The circumference of the circle is " + str(2 * 3.14 * radius))
    print("The area of the circle is " + str(3.14 * radius**2))

elif shape.casefold() == "rectangle".casefold():
    length = float(input("Length = "))
    breadth = float(input("Breadth = "))

    print("The perimeter of the rectangle is " + str(2*(length + breadth)))
    print("The area of the rectangle is " + str(length * breadth))
else:
    print("Either the shape you have chosen is not supported or the you have done any spelling mistake.")
