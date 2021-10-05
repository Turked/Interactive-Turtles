from turtle import Screen
from keyboardturtle import KeyboardTurtle
#from clickableturtle import ClickableTurtle
#from movingturtle import MovingTurtle
from random import randint
# set up instance of the screen
window = Screen()
screen_width = 600
screen_height = 400
window.setup(screen_width, screen_height)

# set up clickable instance
#button = ClickableTurtle()

#set up players:
player_2 = KeyboardTurtle(window, "w", "s", "a", "d")
player_2.color("MediumBlue")
gem = KeyboardTurtle(window)
x_location = randint(-180, 180)
y_location = randint(-180, 180)
gem.goto(x_location, y_location)
gem.left(45)
gem.shape("square")
gem.shapesize(1, 1)
gem.color("Lime")

# set target of other player(our collison check) to the opposite player
gem.other_player = player_2
player_2.other_player = gem


#moveT = MovingTurtle(screen_width)

# This is needed to listen for inputs
window.listen()
window.mainloop()


# be CAREFUL. We aren't controlling the screen draws in this program, so NO while True loops

#TODO:  Check the classes and complete TODOs
#push to github repo.
#link repo to assignment