from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 15, "normal")

with open("data.txt") as data:
    the_data = int(data.read())


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = the_data
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} | HighScore: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset_board(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as the_data2:
                the_data2.write(f"{self.high_score}")
            self.score = 0
            self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset_score(self):
        self.score = 0
        self.update_scoreboard()
