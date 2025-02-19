from turtle import Turtle, Screen
import random

# Create a screen object and set color mode to 255
screen = Screen()
screen.colormode(255)  # Ensures (R, G, B) values are in 0-255 range

chima = Turtle()
chima.shape("arrow")
chima.speed(100)


# Perform the random walk
for i in range(130):  # 200 steps
    # Generate random color
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    chima.color(r, g, b)
    
    chima.pd()
    chima.circle(100)
    chima.pu()
    chima.right(3)
    

 

screen.exitonclick()
