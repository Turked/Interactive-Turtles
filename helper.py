# Importation
from random import choice
import os

# Helpful stuff:
def randcolor():
  colors = ["red", "gold", "orange", "MediumBlue", "magenta", "purple"]
  return choice(colors)

def randbackground():
  option = ["z_floor1.gif", "z_floor2.gif", "z_floor3.gif", "z_floor5.gif", "z_floor4.gif"]
  return choice(option)

def randcolorwall():
  alternative = ["grey", "black", "light green"]
  return choice(alternative)

def updatescore(player_2):
  #High Score:
  changing_file = False
  # Read the current file
  file = open("highscore.txt", "r")

  score = player_2.amount
  if int(score) > int(file.read()):
    changing_file = True


  file.close()


  # DELETE OLD FILE
  if changing_file:
    os.remove("highscore.txt")

    # RECREATE THE FILE
    file = open("highscore.txt", "w")
    file.write(str(score))
    file.close()
