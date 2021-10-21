import os

#3:38
# Read the current file
file = open("highscore.txt", "r")
score = file.read() + 100
print(score)
file.close()