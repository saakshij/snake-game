from random import randint
from food import Food

class Map:

  def __init__(self, screen_size, object_radius):
    self.screen_size = screen_size
    self.object_radius = object_radius
    self.map_size = screen_size // (2*object_radius)

  def get_map_size(self):
    return self.map_size

  def map_to_screen(self, x, y):
    return (self.object_radius + ((x-1)*self.object_radius*2), self.object_radius + ((y-1)*self.object_radius*2))

  #make the food and check if snake intersects with food
  #if snake is initially on that spot - then cannot make food there
  def make_ball(self, snake):
    unavailable_spots = snake.get_body()
    #assign random x and y coordinates within the range of the map
    x = randint(0, self.map_size)
    y = randint(0, self.map_size)
    #flag variable to check for a valid spot
    valid_spot = False
    while not valid_spot:
      valid_spot = True
      #go through snake's body to check if body intersects with food
      for spot in unavailable_spots:
        if (x, y) == spot:
          valid_spot = False
      #if we find out there is not valid spot - must get new coordinates
      if not valid_spot:
        x = randint(0, self.map_size)
        y = randint(0, self.map_size)
    #can return food at those coordinates
    return Food(x, y)
