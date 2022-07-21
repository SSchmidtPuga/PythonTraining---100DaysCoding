from turtle import Screen, Turtle
import time
from snake import Snake
from FOOD import Food
from Score_Board import Scoreboard

class wall(Turtle):


# si es que la cabeza de la wea esta en la misma posicion que y = -300 o 300 o x=300 o -300 while off print(end fame)
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()

