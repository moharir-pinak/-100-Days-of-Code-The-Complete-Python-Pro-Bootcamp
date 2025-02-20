from turtle import  Turtle , Screen

from colorama.ansi import clear_screen

chima = Turtle()
chima.shape("arrow")
screen = Screen()

def m_forward():
    chima.fd(15)

def m_backward():
    chima.fd(-15)

def l_angle():
    chima.left(10)

def r_angle():
    chima.right(10)

def t_clr_scn():
    chima.reset()

screen.listen()
screen.onkey(key="w",fun=m_forward)
screen.onkey(key="a",fun=l_angle)
screen.onkey(key="s",fun=m_backward)
screen.onkey(key="d",fun=r_angle)
screen.onkey(key="c",fun=t_clr_scn)

screen.exitonclick()