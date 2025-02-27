# from turtle import Screen
# from paddel import Paddel
# from ball import Ball
# import time

# screen = Screen()
# screen.bgcolor("black")
# screen.setup(width=800,height=600)
# screen.title("Pong Game")

# p1 = Paddel()
# p2 = Paddel()
# p1.right_side_paddel()
# p2.left_side_paddel()

# ball = Ball()

# screen.listen()

# # Right Side Paddel
# screen.onkey(p1.right_up,"w")
# screen.onkey(p1.right_down,"s")
# # Left Side Paddel
# screen.onkey(p2.left_up,"Up")
# screen.onkey(p2.left_down,"Down")


# game_is_on = True

# while game_is_on:
#     time.sleep(0.1)
#     screen.update()
#     ball.move()
    
#     # Detect the collision between the ball and the walls
#     if ball.ycor()> 280 or ball.ycor() < -280:
#         # Need to bounce
#         ball.bounce()

# screen.exitonclick()

from turtle import Screen, Turtle
from paddel import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(0.02)
    screen.update()
    ball.move()

    #Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    #Detect R paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    #Detect L paddle misses:
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()