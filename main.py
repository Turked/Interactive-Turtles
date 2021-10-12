#Importation:
from turtle import Screen
from helper import randcolor, randcolorwall, randbackground
from keyboardturtle import KeyboardTurtle
from gem import Gem
from wall import Wall
from random import randint
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




#Text
print("Here's the deal.")
print("Your a turtle and a theif.")
print("Now go get that gem!")
print(" ")


#Player setup:
player_2 = KeyboardTurtle(window, "w", "s", "a", "d", walls = wall_list)
player_2.color(randcolor())

gem = Gem(screen_width, screen_height)




#Setting setup:


# Setting up collision check:
player_2.other_player = gem

# This is needed to listen for inputs
window.listen()
window.mainloop()

