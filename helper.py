# Importation
from keyboardturtle import KeyboardTurtle
from random import choice

# Helpful stuff:
def randcolor():
  colors = ["red", "gold", "orange", "MediumBlue", "magenta", "purple"]
  return choice(colors)

def randbackground():
  option = ["z_floor1.gif", "z_floor2.gif", "z_floor3.gif", "z_floor5.gif", "z_floor4.gif"]
  return choice(option)

def randcolorwall():
  alternative = ["brown", "grey", "black", "maroon", "blanched almond"]
  return choice(alternative)

'''
def randsizewall():
  alternative = ["brown", "grey", "black", "maroon", "blanched almond"]
  return choice(alternative)
'''