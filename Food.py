from  turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("Blue")
        self.shapesize(0.5,0.5)
        self.speed("fastest")
        self.penup()
        self.randLocation()

    def randLocation(self):
            rand_X=random.randint(-280,280)
            rand_Y=random.randint(-280,280)
            self.goto(rand_X, rand_Y)




