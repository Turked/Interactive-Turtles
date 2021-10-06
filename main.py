#Importation:
from turtle import Screen
from random import randint
from helper import randcolor
from keyboardturtle import KeyboardTurtle
from clickableturtle import ClickableTurtle
#from movingturtle import MovingTurtle


# Setting up the screen:
window = Screen()
screen_width = 400
screen_height = 400
window.setup(screen_width, screen_height)


# set up clickable button:
button = ClickableTurtle()



#Setting up game and overall setting:


#Game setup:
# randbackground()
print("Here's the deal.")
print("Your a turtle and a theif.")
print("Now go get that gem!")


#Player setup:
player_2 = KeyboardTurtle(window, "w", "s", "a", "d")
player_2.color(randcolor())
gem = KeyboardTurtle(window)
x_location = randint(screen_width/4*-1, screen_width/4)
y_location = randint(screen_height/4*-1, screen_width/4)
gem.speed(0)
gem.goto(x_location, y_location)
gem.left(45)
gem.shape("square")
gem.shapesize(1, 1)
gem.color("Lime")
gem.speed(6)


#Setting setup:


# Setting up collision check:
gem.other_player = player_2
player_2.other_player = gem

# This is needed to listen for inputs
window.listen()
window.mainloop()