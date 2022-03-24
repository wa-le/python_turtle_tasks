from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.pu()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for tart in all_turtles:
        if tart.xcor() > 230:
            is_race_on = False
            winner = tart.pencolor()
            if winner == user_bet:
                print(f"You win the bet")
                print(f"{winner} won while your bet was on {user_bet}")
            else:
                print("you lost the bet")
                print(f"{winner} won while your bet was on {user_bet}")
        rand_distance = random.randint(0, 10)
        tart.forward(rand_distance)

screen.exitonclick()
