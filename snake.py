from turtle import Turtle
class Snake:
    def __init__(self):
        self.position=0
        self.snakePeices=[]
        self.createSnake()
        self.move=20
        self.head=self.snakePeices[0]

    # todo Create snake
    def createSnake(self):
           for pos in range(3):
               self.add_segment(pos)
    def add_segment(self,position):
        new_segment = Turtle(shape="circle")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(self.position, 0)
        self.position += -20
        self.snakePeices.append(new_segment)

    def extend(self):
        self.add_segment(self.snakePeices[-1].position())
    #todo for follwed each segment/peices
    def moveForward(self):
          for seg in range(len(self.snakePeices)-1,0,-1):
            new_x=self.snakePeices[seg-1].xcor()
            new_y=self.snakePeices[seg-1].ycor()
            self.snakePeices[seg].goto(new_x,new_y)
          self.snakePeices[0].forward(self.move)

    def up(self):
        if  self.snakePeices[0].heading()!=270:
            self.snakePeices[0].setheading(90)

    def down(self):
        if self.snakePeices[0].heading() != 90:
         self.snakePeices[0].setheading(270)
    def right(self):
        if self.snakePeices[0].heading() != 180:
         self.snakePeices[0].setheading(0)
    def left(self):
        if self.snakePeices[0].heading() != 0:
         self.snakePeices[0].setheading(180)