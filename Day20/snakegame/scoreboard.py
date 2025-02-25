from turtle import Turtle

class Scoreboard(Turtle):
    
    def  __init__(self):
        super().__init__()
        self.score = 0
        self.goto(0,270)
        self.penup()
        self.color("white")
        self.hideturtle()
        
    def score_update(self):
        self.write(f"Score : {self.score}",align="center", font=("Times New Roman" , 24 , "bold"))
        
        
    def game_over(self):
        self.goto(0,0)
        self.write("Game Over" , align="center", font=("Times New Roman" , 30  , "bold"))
        
    def increase(self):
        self.score +=1
        self.clear()
        self.score_update()