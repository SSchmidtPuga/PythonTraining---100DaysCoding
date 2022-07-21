from turtle import Screen, Turtle
import time
from snake import Snake
from FOOD import Food

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.goto(0,270)
        self.write(f"Your score is {self.score}: ", False, align="center", font=("Arial", 24,"normal"))
        self.hideturtle()


    def add_score(self):
        self.score +=1
        self.clear()
        self.write(f"Your score is {self.score}: ", False, align="center", font=("Arial", 24,"normal"))

    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over", False, align="center", font=("Arial", 24, "normal"))






