from turtle import Turtle
from random import randint

class Gem (Turtle):
    def __init__(self, screen_width, screen_height):
        Turtle.__init__(self)
        self.screen_width = screen_width
        self.screen_height = screen_height 
        
        self.penup()   
        x_location = randint(screen_width/4*-1, screen_width/4)
        y_location = randint(screen_height/4*-1, screen_width/4)
        # General setup
        self.speed(0)
        self.goto(x_location, y_location)
        self.left(45)
        self.shape("square")
        self.shapesize(1, 1)
        self.color("Lime")
        self.speed(6)
        # self.color("black")
        # 
        # self.shape("turtle")
        # self.goto(self.starting_x, self.starting_y)
        
    def method_example(self):
        pass
        ## change the name and make the method work