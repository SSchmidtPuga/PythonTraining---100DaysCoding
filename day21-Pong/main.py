from turtle import Turtle,Screen, listen
from Paddle import paddle
import time
from BALL import ball
import random


screen = Screen()
screen.setup(width=800,height=500)
screen.bgcolor("black")
screen.tracer(0)

STARTING_POSITIONS = [(350,0), (350,-20), (350,20)]

ball = ball()
paddle2 = paddle(2)
paddle1 = paddle(1)

screen.listen()
screen.onkey(paddle1.down, "Down")
screen.onkey(paddle1.up, "Up")

game_is_on = True
score = 0
ball.move()



while game_is_on:
    screen.update()
    time.sleep(0.1)
    ball.move()
    if ball.xcor() > 200:
        ball.bouncing()











    #     paddle1.segments[0].backward(20)
    # if paddle1.segments[0].ycor() <= -225:
    #     paddle1.segments[0].backward(20)
    # if paddle2.segments[0].distance(ball) < 15:
    #     ball.movebackwards()
    # elif paddle1.segments[0].distance(ball) < 10:
    #     ball.movebackwards()
















screen.exitonclick()
