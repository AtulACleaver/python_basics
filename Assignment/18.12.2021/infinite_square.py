import turtle
draw = turtle.Turtle()
i = 40
while i > 0:
    draw.forward(120)
    draw.left(90)
    draw.forward(120)
    draw.left(90)
    draw.forward(120)
    draw.left(90)
    draw.forward(120)
    draw.left(90)
    draw.left(i)
    i += 10

turtle.done()
