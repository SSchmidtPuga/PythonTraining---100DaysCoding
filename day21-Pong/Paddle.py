from turtle import Turtle

STARTING_POSITIONS = [(350,0),(-350,0)]

MOVE_FORWARDS = 10

class paddle(Turtle):

    def __init__(self,player):
        super().__init__()
        self.paddle = Turtle(shape="square")
        self.paddle.penup()
        self.paddle.color("white")
        self.paddle.goto(STARTING_POSITIONS[player-1])
        self.paddle.shapesize(1, 5)
        self.paddle.setheading(90)

    def up(self):
        new_y = self.paddle.ycor() + 20
        self.paddle.goto(self.paddle.xcor(), new_y)


    def down(self):
        new_y = self.paddle.ycor() - 20
        self.paddle.goto(self.paddle.xcor(), new_y)




