from turtle import Turtle
from Paddle import paddle
import random


class ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.heading()

    def move(self):
        new_x = self.xcor() + 10
        new_y = self.ycor() + 10
        self.goto(new_x, new_y)





    def movefoward(self):
       self.forward(20)

    def movebackwards(self):
        self.backward(20)

    def bouncing(self):
        new_x = self.xcor()
        new_y = self.ycor() -20
        self.goto(new_x, new_y)














