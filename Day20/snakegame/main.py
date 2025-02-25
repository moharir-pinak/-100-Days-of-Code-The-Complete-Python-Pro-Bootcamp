from turtle import Turtle , Screen
from snake import Snake
from food import Food 
from scoreboard import Scoreboard
# importing this so that we can check the animations by slowing down the animtions
import time

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Game")
# to Change the default animations we are changing the tracer value of the screen to 0
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snake.up , "w")
screen.onkey(snake.left,"a")
screen.onkey(snake.down,"s")
screen.onkey(snake.right,"d")

game_is_on = True
while game_is_on :
    screen.update()
    time.sleep(0.1)
    snake.move()
    
    # Collision Detection with food
    
    if snake.head.distance(food) < 15:
        food.refresh()  
        snake.extend()
        score.increase()
    # Collision detection with Wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_is_on = False
        score.game_over()
        
        
screen.exitonclick()
