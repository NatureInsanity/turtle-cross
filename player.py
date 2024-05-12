from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.y = -280
        self.goto(0,self.y)

    def reset(self):
        self.goto(0,self.y)
    def up(self):
        self.forward(20)

    def down(self):
        self.backward(20)

