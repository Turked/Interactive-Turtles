from turtle import Turtle, Screen
from helper import randcolorwall, randcolor, randbackground
from keyboardturtle import KeyboardTurtle
from gem import Gem
from wall import Wall
from random import randint
from time import time


#Setup:
class WallRandom(Turtle):
  def __init__(self, 
               window,  
               space = "restart"):
    Turtle.__init__(self)

    # Sets up incoming variables:
    self.space = space


    # Sets up keyboard command examples:
    self.window.onkey(self.re_start, self.space)

# The whole stuff
  def re_start(self):
    #List setup:
    wall_list = []
    w1 = Wall(256, 190, 4, 4)
    wall_list.append(w1)

    #Vertical walls:
    color = randcolorwall() #Maroon shouldn't exist as a color but it does
    for wall in range (10):
      wall_list.append(Wall(randint(-300, 300), randint(-200, 200), .5, randint(5, 10)))
      wall_list[len(wall_list)-1].color(color)


    #Horizontal walls:
    for wall in range (10):
      wall_list.append(Wall(randint(-300, 300), randint(-200, 200), randint(5, 10), .5))
      wall_list[len(wall_list)-1].color(color)
