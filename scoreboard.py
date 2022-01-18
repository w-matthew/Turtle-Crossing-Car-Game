from turtle import Turtle
# Different font sizes for level and end game
FONT1 = ("Courier", 15, "normal")
FONT2 = ("Courier", 28, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        # set inital level, color, and modes so turtle and trail line do not show up
        self.level = 1
        self.color("black")
        self.penup()
        self.hideturtle()

    def write_board(self):
        """displays the "level: x" text and sets position"""
        self.clear()
        self.goto(-230, 255)
        self.write(f"Level: {self.level}", align="center", font=FONT1)

    def increment_level(self):
        """increment level. called when turtle reaches end on current level"""
        self.level += 1

    def end_game_print(self):
        """display the end game text. called when user collides with car"""
        self.goto(0, 0)
        self.write("GAME OVER.", align="center", font=FONT2)
