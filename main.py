#Importation:
from turtle import Screen
from helper import randcolor, randcolorwall, randbackground
from keyboardturtle import KeyboardTurtle
from gem import Gem
from wall import Wall
from random import randint, choice

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
starting_wall = Wall(randint(250, 300), 180, 1, 5)
SW_x = randint(250, 300)
SW_y = 180


#Vairaibles:
last_x = starting_wall.xcor()
last_y = starting_wall.ycor()
last_width = starting_wall.x_size
last_height = starting_wall.y_size
color = randcolorwall()
starting_wall.color(color)

''' This no work IDK how to make work
if randbackground("z_floor1.gif"):
  color = "red"
'''

def callibration():
  notch = [-10, 1, 10]
  return choice(notch)

def random():
  rando = [1, 2, 3, 4, 5, 6]
  return choice(rando)

#Creation of the first wall:
wall_list.append(starting_wall)

#I wanna add a penup type command as to create gaps in the walls

#Loop for amount of whole walls:
for i in range(4):


#Doing this to create blank
  for i in range(2):


  #Loop for amount of walls:
    for i in range(2):

    # Horrizontal Wall
      my_width = randint(3, 6)
      my_height = 1
      current_callibration = callibration()
      last_x = last_x + (my_width * current_callibration) - current_callibration #I want it to minus callibration
      last_y = last_y - (last_height) * 10
      last_width = my_width
      last_height = my_height
      wall_list.append(Wall(last_x, last_y, my_width, my_height))
      wall_list[len(wall_list)-1].color(color)

      #wall_list.color("clear") this no work

      current_callibration = callibration()
      # Vertical Wall
      my_width = 1
      my_height = randint(3, 6)
      last_x = last_x + (last_width * current_callibration) - current_callibration
      last_y = last_y - (my_height) * 10
      last_width = my_width
      last_height = my_height
      wall_list.append(Wall(last_x, last_y, my_width, my_height))
      wall_list[len(wall_list)-1].color(color)
    
    randturtle = len(wall_list)-random()
    wall_list[randturtle].hideturtle()
    wall_list.remove(wall_list[randturtle])


    # Making another beggining notch
  starting_wall = Wall(SW_x-200, 180, 1, 5)
  SW_x = SW_x - 200
  last_x = SW_x
  last_y = 180
  starting_wall.color(color)



#Score Board:
wall_list.append(Wall(256, 190, 4, 4))


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

