from turtle import Turtle
# import random

# STARTING_POS = [(350, 0), (-350, 0)]


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")

        self.turtlesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.speed("fastest")
        # self.refresh()
        self.pu()
        self.goto(position)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
