from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.score = 0
        with open("savefile.txt") as save:
            self.high_score = int(save.read())
        self.goto(-270,270)
        self.update()
        self.hideturtle()

    def update(self):
        self.clear()
        self.write(f"Score: {self.score} | High Score: {self.high_score}")

    def refresh(self):
        self.score = 0
        self.update()

    def new_score(self):
        self.score += 1
        if self.score > self.high_score:
            self.high_score = self.score
        self.update()

    def save(self):
        with open("savefile.txt",mode="w") as save:
            save.write(f"{self.high_score}")