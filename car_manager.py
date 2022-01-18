from turtle import Turtle
import random
# initalizes constants such as colors for cars, starting speed, and incremental speed when user levels up
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 7


class CarManager:
    def __init__(self):
        """creates empty list for all cars. List is useful because in main,
         I can check if any car in the list has collided. Car speed variable
          is used to increment when player levels up"""
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        """creates a car and adds it to the list"""
        random_chance = random.randint(1, 5)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(1, 2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.goto(300, random.randint(-250, 250))
            self.all_cars.append(new_car)

    def move_cars(self):
        """moves all the cars in the lsit by current speed"""
        for car in self.all_cars:
            car.backward(self.car_speed)

    def increase_speed(self):
        """increments the speed. called when player completes level"""
        self.car_speed += MOVE_INCREMENT
