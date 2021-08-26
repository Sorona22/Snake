from turtle import Turtle
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
starting_positions = [(0,0), (-20, 0), (40, 0)]

class Snake:
    def __init__(self):
        self.boxes = []
        self.create_snake()
        self.head = self.boxes[0]

    def add_segment(self, position):
        box = Turtle(shape="square")
        box.penup()
        box.color("white")
        box.goto(position)
        self.boxes.append(box)

    def extend(self):
        self.add_segment(self.boxes[-1].position())

    def create_snake(self):
        for box in starting_positions:
            self.add_segment(box)

    def move(self):
        for box in range(len(self.boxes)-1,  0, -1):
            new_x = self.boxes[box - 1].xcor()
            new_y = self.boxes[box - 1].ycor()
            self.boxes[box].goto(new_x, new_y)
        self.boxes[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.boxes[0].setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.boxes[0].setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.boxes[0].setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.boxes[0].setheading(RIGHT)

