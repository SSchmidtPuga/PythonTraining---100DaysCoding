import turtle
from turtle import Turtle
screen = turtle.Screen()
screen.title(("U.S. State Games"))
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

answer_state = screen.textinput(title="Guess the state", prompt = "Whats another states name")

import pandas as pd

df_us_state = pd.read_csv("50_states.csv")

print(df_us_state)

turtle.goto(0,0)
list_us_states = df_us_state["state"].tolist()

State_serie = df_us_state[df_us_state.state == "Alabama"]
xcor = int(State_serie.x)
print(xcor)

Titles = []
Title = Turtle()
Title.penup()
Title.hideturtle()
print(list_us_states)


while len(Titles) < 50:
    answer_state = screen.textinput(title=f"{len(Titles)}/50 state Guessed", prompt="Whats another states name").title()
    if answer_state == "exit":
        break
    if answer_state in list_us_states:
        State_serie = df_us_state[df_us_state.state == answer_state]
        xcor = int(State_serie.x)
        State_serie = df_us_state[df_us_state.state == answer_state]
        ycor = int(State_serie.y)
        Title.goto(xcor,ycor)
        Title.write(f"{answer_state}", align="left", font=("Arial", 10, "normal"))
        Titles.append(Title)












screen.exitonclick()

#