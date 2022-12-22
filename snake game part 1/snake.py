from turtle import Turtle
FORWARD_DISTANCE = 20


class Snake:
    turtles = []

    def __init__(self):
        positions = [(0, 0), (-20, 0), (-40, 0)]
        for position in positions:
            t = Turtle("square")
            t.color("white")
            t.penup()
            t.goto(position)
            self.turtles.append(t)
        self.head = self.turtles[0]

    def move(self):
        for t in range(len(self.turtles) - 1, 0, -1):
            x_position = self.turtles[t - 1].xcor()
            y_position = self.turtles[t - 1].ycor()
            self.turtles[t].goto((x_position, y_position))
        self.turtles[0].forward(FORWARD_DISTANCE)

    def up(self):
        self.turtles[0].setheading(90)

    def down(self):
        self.turtles[0].setheading(270)

    def left(self):
        self.turtles[0].setheading(180)

    def right(self):
        self.turtles[0].setheading(0)

    def add(self):
        t = Turtle("square")
        t.color("white")
        t.penup()
        x_position = self.turtles[len(self.turtles)-1].xcor()
        y_position = self.turtles[len(self.turtles) - 1].ycor()
        t.goto(x_position, y_position)
        self.turtles.append(t)

    def check(self):
        for i in range(1, len(self.turtles)-1):
            if self.turtles[0].distance(self.turtles[i]) == 0:
                return False

        return True


