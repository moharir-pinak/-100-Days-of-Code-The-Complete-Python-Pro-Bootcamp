from turtle import Turtle, Screen
import random

# Create a screen object and set color mode to 255
screen = Screen()
screen.colormode(255)  # Ensures (R, G, B) values are in 0-255 range

chima = Turtle()
chima.shape("arrow")
chima.speed(10)
chima.pensize(5)


# Full Random Lines gengrator 

# paths = 0
# while paths < 200:
    
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
    
#     distance = random.randint(50,100)
#     angle = random.randint(20,360)

    
#     chima.color((r, g, b))  # Now it will work correctly
#     chima.forward(distance)
    
#     if random.choice(["left", "right"]) == "left":
#         chima.left(angle)
#     else:
#         chima.right(angle)
#     paths += 1

# Code for random Walk

# Directions (angles)
directions = [0, 90, 180, 270]  # Move in 4 possible directions

# Perform the random walk
for _ in range(200):  # 200 steps
    # Generate random color
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    chima.color(r, g, b)

    # Move forward and turn randomly
    chima.forward(30)
    chima.setheading(random.choice(directions))  # Face a random direction


screen.exitonclick()
