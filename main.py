import turtle
from turtle import Screen
from snake import Snake
from Food import Food
from scoreboard import Scoreboard
import  time
screen=Screen()
screen.bgcolor("black")
screen.screensize(600,600)
screen.title("snake GAME")
screen.tracer(0)
screen.listen()

snake=Snake()
food=Food()
scoreboard=Scoreboard()
screen.onkey(snake.up,"Up")
screen.onkey(snake.right,"Right")
screen.onkey(snake.left,"Left")
screen.onkey(snake.down,"Down")




#todo Move snake
isGameOn=True
while isGameOn:
    #todo join object pieces of snake
    screen.update()
    time.sleep(0.2)
    snake.moveForward()

    #TODO collision with food
    if snake.head.distance(food)<15:
       food.randLocation()
       scoreboard.increase_Score()
       snake.extend()


    #TODO detect snake collision with wall
    if snake.head.xcor()> 300 or snake.head.xcor() <-300 or snake.head.ycor()>300 or snake.head.ycor() <-300:
        scoreboard.gameOver()
        isGameOn=False
        # # TODO popUp:Is user want to continue this game
        # wantToContinue = turtle.textinput("Want to continue this game", "Type YES")
        # if wantToContinue == "yes":
        #     isGameOn = True
    #todo if head of snake collides with any segment
    for segment in snake.snakePeices:
        if segment==snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            scoreboard.gameOver()
            isGameOn = False
            turtle.reset()
            # # TODO popUp:Is user want to continue this game
            # wantToContinue = turtle.textinput("Want to continue this game", "Type YES")
            # if wantToContinue == "yes":
            #     isGameOn = True
            #     turtle.reset()
            break

screen.exitonclick()