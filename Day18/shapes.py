# from turtle import Turtle , Screen
# import random

# chima = Turtle()
# chima.shape("arrow")
# sides = 3

# while sides < 10:
    
#     angle = 360/sides
#     for _ in range(sides):
#         r = random.randint(0, 155)
#         g = random.randint(0, 155)
#         b = random.randint(0, 155)
#         chima.color((r, g, b))
#         chima.fd(200)
#         chima.right(angle)
#     sides +=1




# screen =  Screen()
# screen.colormode(255)
# screen.exitonclick()

from turtle import Turtle, Screen
import random

# Create a screen object and set color mode to 255
screen = Screen()
screen.colormode(255)  # Ensures (R, G, B) values are in 0-255 range

chima = Turtle()
chima.shape("arrow")

chima.pu()
chima.goto(0,0)
chima.pd()

sides = 3

while sides < 9:
    angle = 360 / sides
    r = random.randint(0, 155)
    g = random.randint(0, 155)
    b = random.randint(0, 155)

    chima.color((r, g, b))  # Now it will work correctly

    for _ in range(sides):
        chima.forward(100)
        chima.right(angle)
    sides += 1

screen.exitonclick()
