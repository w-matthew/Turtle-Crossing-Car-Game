from turtle import Turtle
# constants for inital position, move units, and finish line
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        """initalizes default settings for turtle to start at bottom"""
        super().__init__()
        self.MOVE_INCREMENT = 0.1
        self.penup()
        self.shape("turtle")
        self.left(90)
        self.go_to_start()

    def go_up(self):
        """Moves turtle up 10 spaces"""
        self.forward(MOVE_DISTANCE)

    def check_end(self):
        """returns if the turtle has crossed the finish line"""
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False

    def go_to_start(self):
        """sets the turtle back to the start(bottom, middle)"""
        self.goto(STARTING_POSITION)

