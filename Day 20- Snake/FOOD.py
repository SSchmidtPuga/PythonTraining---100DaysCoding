from typing import Any

from turtle import Screen, Turtle,listen
import random
from snake import Snake


class Food(Turtle,Snake):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.penup()
        self.speed("fastest")
        self.shapesize(0.5,0.5)
        self.random_position()

#primero tengo que guardar las cordenadas actuales en la que estoy(o,o), despues modificarlas de manera random entre numero del 1 al 600
    def random_position(self):
        new_x = random.randint(-200, 200)
        new_y = random.randint(-200, 200)
        self.goto(new_x, new_y)














