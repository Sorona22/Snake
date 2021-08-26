from turtle import Turtle




class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.ht()
        self.color("white")
        self.Score = 0
        self.goto(0, 280)
        self.starting_board()

    def starting_board(self):
        self.write(f"Score: {self.Score}", align="center", font=(20))

    def score(self):
        self.clear()
        self.Score += 1
        self.write(f"Score: {self.Score}", align="center", font=(20))

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", font = (20))