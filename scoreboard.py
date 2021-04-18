from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        self.score = 0
        super().__init__()
        self.hideturtle()

    def increase_Score(self):
        self.penup()
        self.pencolor("white")
        self.goto(0, 250)

        self.score+=1
        self.clear()
        self.write(f"score: {self.score}", align="center", font=("arial", 20, "normal"))
    def gameOver(self):
           self.pencolor("white")
           self.goto(0,0)
           self.write("Game Over", align="center", font=("arial", 28, "normal"))
