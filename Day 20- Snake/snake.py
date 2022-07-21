from typing import Any

from turtle import Screen, Turtle,listen

STARTING_POSITIONS = [(0,0), (-20,0), (-40,0)]
MOVE_FORWARDS =20


class Snake():

    def __init__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)
    def add_segment(self,position):
        new_segments = Turtle(shape="square")
        new_segments.color("white")
        new_segments.penup()
        new_segments.goto(position)
        self.segments.append(new_segments)
    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_FORWARDS)

    def up(self):
        self.segments[0].setheading(90)
    def left(self):
        self.segments[0].setheading(180)
    def down(self):
        self.segments[0].setheading(270)
    def right(self):
        self.segments[0].setheading(0)













 

