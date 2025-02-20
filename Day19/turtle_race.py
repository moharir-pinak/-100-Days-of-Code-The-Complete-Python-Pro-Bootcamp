from turtle import  Turtle , Screen
import random

from colorama.ansi import clear_screen

is_race = False
screen = Screen()
# Define the width and height of the screen
screen.setup(width=500,height=400)


#  User input for the bet
user_input = screen.textinput(title="Who Will Win ?", prompt="Which turtle will win the race")
# print(user_input)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_pos = [-70,-40,-10,20,50,80]
all_turtle = []

# Turtles positioning
for i in range (0,6):
    new_turtle = Turtle()
    new_turtle.color(colors[i])
    new_turtle.shape("turtle")
    new_turtle.pu()
    new_turtle.goto(x=-240, y=y_pos[i])
    all_turtle.append(new_turtle)

if user_input:
    
    is_race = True
    
    
winners = []

while is_race:
    for turtle in all_turtle:

        if turtle.xcor() > 230:
            is_race =  False
            winners.append(turtle.pencolor())
        turtle.fd(random.randint(1,10))

if winners[0] == user_input :
    print(f"The winner is {winners[0]} .Your Player Won ")
else :
    print(f"The winner is {winners[0]} . Unfortunately your turtle lose.")


screen.exitonclick()