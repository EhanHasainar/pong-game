from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape('square')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color('white')
        self.penup()
        self.goto(position, 0)

    def go_up(self):
        if self.ycor() < 250:  
            y_cord = self.ycor() + 20
            self.goto(self.xcor(), y_cord)

    def go_down(self):
        if self.ycor() > -240: 
            y_cord = self.ycor() - 20
            self.goto(self.xcor(), y_cord)

