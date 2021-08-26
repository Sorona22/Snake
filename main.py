from turtle import Screen
from oh import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.update()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.score()

    #Detect collision with wall.
    if snake.head.xcor() > 285 or snake.head.xcor() < -285 or snake.head.ycor() >285 or snake.head.ycor() < -285:
        game_is_on = False
        scoreboard.game_over()

    #Detect collision with tail
    #if head collides with any segment in the tail:
    #trigger game over
    for box in snake.boxes[1:]:
        if snake.head.distance(box) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
