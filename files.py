import os


changing_file = False
# Read the current file
file = open("highscore.txt", "r")

score = input ("Enter username and highscore")
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
