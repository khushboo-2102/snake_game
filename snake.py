from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]    # create tuple # constant
MOVE_DISTANCE = 20                                   # create constant
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


# Create a Snake
class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        # add a new segment to the snake.
        self.add_segment(self.segments[-1].position())  # -1 is last segment and
        # position is from turtle to extract position of last segment and then add segment after it.

# Move a Snake
    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):    # start= 2, stop = 0, step = -1  ( 2 to 1 to 0)
            new_x = self.segments[seg_num - 1].xcor()           # last segment - 1 = 2nd last segment
            new_y = self.segments[seg_num - 1].ycor()           # (hold the position 2nd seg)
            self.segments[seg_num].goto(new_x, new_y)           # set last segment into the position of 2nd last segment

        self.head.forward(MOVE_DISTANCE)
        # segments[0].left(90)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
