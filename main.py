#Importation:
from turtle import Screen
from helper import randcolor
from keyboardturtle import KeyboardTurtle
from gem import Gem
from wall import Wall

# Setting up the screen:
window = Screen()
#2:51/8:17
#window.bgpic("bitfloor.png")
screen_width = 512
screen_height = 512
window.setup(screen_width, screen_height)


# set up clickable button:




#Setting up game and overall setting:


#Game setup:

#Screen:
# randbackground()

#List setup:
wall_list = []

w1 = Wall(100, 0, 1, 3)
wall_list.append(w1)
wall_list.append(Wall(0, 100, 5, 1))


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