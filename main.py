#Importation:
from turtle import Screen
from helper import randcolor, randcolorwall, randbackground
from keyboardturtle import KeyboardTurtle
from wall_random import WallRandom
from gem import Gem
from wall import Wall
from random import randint, choice
from time import time


# Setting up the screen:
window = Screen()
window.bgpic(randbackground())
screen_width = 600
screen_height = 400
window.setup(screen_width, screen_height)


#Setting up game and overall setting:


#Game setup:

#Screen:




#Mega Walls:________________________________________

#Setup:
wall_list = []


#Vairaibles:
starting_wall = Wall(-50, 180, 1, 5)
last_x = starting_wall.xcor()
last_y = starting_wall.ycor()
last_width = starting_wall.x_size
last_height = starting_wall.y_size

def callibration():
  notch = [-10, 1, 10]
  return choice(notch)


#Creation of the first wall:
wall_list.append(starting_wall)

#Loop for amount of walls:
for i in range(5):

# Horrizontal Wall
  my_width = randint(3, 6)
  my_height = 1
  last_x = last_x + (my_width * callibration()) - 10
  last_y = last_y - (last_height) * 10
  last_width = my_width
  last_height = my_height
  wall_list.append(Wall(last_x, last_y, my_width, my_height))

# Vertical Wall
  my_width = 1
  my_height = randint(3, 6)
  last_x = last_x + (last_width * 10) - 10
  last_y = last_y - (my_height) * 10
  last_width = my_width
  last_height = my_height
  wall_list.append(Wall(last_x, last_y, my_width, my_height))

#Score Board:
wall_list.append(Wall(256, 190, 4, 4))


'''
#Vertical walls:
color = randcolorwall() #Maroon shouldn't exist as a color but it does
for wall in range (12):
  wall_list.append(Wall((wall*55)-300+randint(-10, 10), randint(-200, 200), .5, randint(5, 10)))
  wall_list[len(wall_list)-1].color(color)

#Horizontal walls:
for wall in range (12):
  wall_list.append(Wall(randint(-300, 300), (wall*50)-200+randint(-10, 10), randint(5, 10), .5))
  wall_list[len(wall_list)-1].color(color)

wall_list.append(Wall(256, 190, 4, 4))
'''

#Text
print("Here's the deal.")
print("Your a turtle and a theif.")
print("Now go get that gem!")
print(" ")


#Player setup:
player_2 = KeyboardTurtle(window, "w", "s", "a", "d", walls = wall_list)
player_2.color(randcolor())

gem = Gem(screen_width, screen_height)

#restart = WallRandom()


#Setting setup:


# Setting up collision check:
player_2.other_player = gem

# This is needed to listen for inputs
window.listen()
window.mainloop()

