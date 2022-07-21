from turtle import Screen, Turtle
import time
from snake import Snake
from FOOD import Food
from Score_Board import Scoreboard

screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("My Snake game")
screen.tracer(0)

snake = Snake()
screen.listen()
food = Food()
score_board = Scoreboard()



screen.onkey(snake.up, "Up")
screen.onkey(snake.left, "Left")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")

game_is_on = True
score = 0

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.segments[0].distance(food) < 15:
        food.random_position()
        snake.extend()
        score_board.add_score()
    if snake.segments[0].xcor() > 280:
        game_is_on = False
        score_board.game_over()
    if snake.segments[0].ycor() > 280:
        game_is_on = False
        score_board.game_over()

    for segments in snake.segments[1:]:
        if snake.segments[0].distance(segments) < 10:
            game_is_on = False
            score_board.game_over()

































screen.exitonclick()




