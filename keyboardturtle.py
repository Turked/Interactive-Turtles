#Importation
from turtle import Turtle
from random import randint
from clickableturtle import Text
from time import time

#Setup:
class KeyboardTurtle(Turtle):
  def __init__(self, 
               window,  
               straight = "Up", 
               backward = "Down",
               turn_left = "Left",
               turn_right = "Right", 
               other_player = None,
               walls = None):
    Turtle.__init__(self)
    
    # Sets up incoming variables:
    self.window = window
    self.straight = straight
    self.backward = backward
    self.turn_right = turn_right
    self.turn_left = turn_left
    self.other_player = other_player
    self.text = Text()
    self.walls = walls

    #set turtle starting states:
    self.shape("turtle")
    self.color("green")
    self.penup()

    # Sets up keyboard command examples:
    self.window.onkey(self.go_right, self.turn_right)
    self.window.onkey(self.go_left, self.turn_left)
    self.window.onkey(self.go_nstraight, self.backward)
    self.window.onkey(self.go_forward, self.straight)

    #sets up controlling variables (y not implemented):
    self.movement_speed = 5
    self.turn_speed = 45
    self.collision_distance = 20

    self.amount = 0
    self.canCollect = True


  # Movement Methods/defining above Keyboard Commands:
  def go_forward(self):
    #Move forward
    last_position = (self.xcor(), self.ycore())
    collided = False
    self.forward(self.movement_speed)
    #Check for collision with gem
    if self.check_collision(self.other_player):
      if self.canCollect:
        self.canCollect = False
        self.amount += 1
        self.text.draw_title(str(self.amount))
        print("gem collected (" + str(self.amount) + ")")
        x_location = randint(-180, 180)
        y_location = randint(-180, 180)
        self.other_player.speed(0)
        self.other_player.goto(x_location, y_location)
        self.other_player.speed(6)
        self.wait(.5)

    #Check for collision with walls
    if self.walls !=None:
      for wall in self.walls:
        if self.check_wall_collision(wall):
          collided = True
          break
      if collided:
        self.goto(last_position)

  def go_nstraight(self):
    #Move forward
    last_position = (self.xcor(), self.ycore())
    collided = False
    self.forward(-self.movement_speed)
    #Check for collision with gem
    if self.check_collision(self.other_player):
      if self.canCollect:
        self.canCollect = False
        self.amount += 1
        print("gem collected (" + str(self.amount) + ")")
        x_location = randint(-180, 180)
        y_location = randint(-180, 180)
        self.other_player.speed(0)
        self.other_player.goto(x_location, y_location)
        self.other_player.speed(6)
        self.wait(.5)

    #Check for collision with walls
    if self.walls !=None:
      for wall in self.walls:
        if self.check_wall_collision(wall):
          collided = True
          break
      if collided:
        self.goto(last_position)

  def go_right(self):
    self.right(self.turn_speed)

  def go_left(self):
    self.left(self.turn_speed)

  def wait(self, seconds):
    start_time = time()
    end_time = start_time + seconds
    while time() < end_time:
      pass
    self.canCollect = True

  # Useful Methods:

  # This checks if object collides with another object:
  def check_wall_collision(self, obj_to_check):
    turtle_rad = 10
    wall_rad = 10
    distance_x = obj_to_check.xcor() - self.xcor()
    distance_x = abs(distance_x)
    
    distance_y = obj_to_check.ycor() - self.ycor()
    distance_y = abs(distance_y)
    if distance_x < turtle_rad + (wall_rad * obj_to_check.x_size) and distance_y < turtle_rad + (wall_rad * obj_to_check.y_size):
      return True
    else:
      return False    