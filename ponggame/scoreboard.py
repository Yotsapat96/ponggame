from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.right_player_score = 0
        self.left_player_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-150, 200)
        self.write(self.left_player_score, align="left", font=("Courier", 80, "bold"))
        self.goto(150, 200)
        self.write(self.right_player_score, align="right", font=("Courier", 80, "bold"))

    def left_scored(self):
        self.left_player_score += 1
        self.update_scoreboard()

    def right_scored(self):
        self.right_player_score += 1
        self.update_scoreboard()