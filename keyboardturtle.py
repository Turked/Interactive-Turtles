from turtle import Turtle
from random import randint


class KeyboardTurtle(Turtle):
  # our 'wrapper' class of the Turtle class
  def __init__(self, 
               window,  
               straight = "Up", 
               backward = "Down",
               turn_left = "Left",
               turn_right = "Right", 
               other_player = None):
    # Runs Keyboard Turtle Constructor as well as the Turtle Constructor
    Turtle.__init__(self)
    
    # Sets up incoming variables
    self.window = window
    self.straight = straight
    self.backward = backward
    self.turn_right = turn_right
    self.turn_left = turn_left
    self.other_player = other_player

    #set turtle starting states
    self.shape("turtle")
    self.color("green")
    self.penup()

    # Sets up keyboard command examples
    self.window.onkey(self.go_right, self.turn_right)
    self.window.onkey(self.go_left, self.turn_left)
    self.window.onkey(self.go_nstraight, self.backward)
    self.window.onkey(self.go_forward, self.straight)

    #sets up controlling variables (y not implemented)
    self.movement_speed = 5
    self.turn_speed = 45
    self.collision_distance = 20
    self.amount = 0


  # Movement Methods
  def go_forward(self):
    self.forward(self.movement_speed)
    if self.check_collision(self.other_player):
      print("gem collected")
      self.amount += 1
      print(self.amount)
      x_location = randint(-180, 180)
      y_location = randint(-180, 180)
      self.other_player.speed(0)
      self.other_player.goto(x_location, y_location)
      self.other_player.speed(6)

      
  def go_nstraight(self):
    self.forward(-self.movement_speed)
    if self.check_collision(self.other_player):
      print("gem collected")
      self.amount += 1
      print(self.amount)
      x_location = randint(-180, 180)
      y_location = randint(-180, 180)
      self.other_player.speed(0)
      self.other_player.goto(x_location, y_location)
      slef.other_player.speed(6)




  def go_right(self):
    self.right(self.turn_speed)

  def go_left(self):
    self.left(self.turn_speed)


  # Useful Methods

  # This checks if object collides with another object.  
  # Right now it checks against the other player, but 
  # it doesn't NEED to.  It can check against any
  # other turtle object

  def check_collision(self, obj_to_check):
    distance_x = obj_to_check.xcor() - self.xcor()
    distance_x = abs(distance_x)

    distance_y = obj_to_check.ycor() - self.ycor()
    distance_y = abs(distance_y)

    if distance_x < self.collision_distance and distance_y < self.collision_distance:
      return True
    else:
      return False


    # TODO: finish setting up the inputs (left and down)
    
