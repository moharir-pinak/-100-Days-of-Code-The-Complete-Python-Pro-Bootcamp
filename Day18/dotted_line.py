from turtle import Turtle , Screen

chima = Turtle()
chima.shape("arrow")

for _ in range(15):
    chima.pd()
    chima.fd(10)
    chima.pu()
    chima.fd(10)

screen =  Screen()

screen.exitonclick()