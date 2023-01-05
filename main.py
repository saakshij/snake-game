import pygame
from snake import Snake
from food import Food
from map import Map

# Initializing Pygame
pygame.init()

# Game parameters
WIDTH = 400
OBJECT_RADIUS = 10
TICK = 100

# Screen
screen = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("Snake Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Fonts
END_FONT = pygame.font.SysFont('courier', 40)


# Helpers
def draw_object(game_map, color, x, y):
  pygame.draw.circle(screen, color, game_map.map_to_screen(x, y), OBJECT_RADIUS)

def handle_action(direction, snake, food, game_map):
  #handle each direction, left, right, up, down
  if direction == pygame.K_RIGHT:
    tail = snake.move_right()
  if direction == pygame.K_LEFT:
    tail = snake.move_left()
  if direction == pygame.K_UP:
    tail = snake.move_up()
  if direction == pygame.K_DOWN:
    tail = snake.move_down()
  
  #check if the snake intersects with food right after direction change
  #if food is there, body part gets added
  #if food is not there, tail turns black
  #return a food object
  if snake.is_alive():
    #if snake intersects with food, then eat, make new food
    if (snake.get_x() == food.get_x()) and (snake.get_y() == food.get_y()):
      snake.eat()
      new_food = game_map.make_ball(snake)
      draw_object(game_map, BLUE, snake.get_x(), snake.get_y())
      draw_object(game_map, RED, new_food.get_x(), new_food.get_y())
      return new_food
    else:
      #draw snake
      draw_object(game_map, BLUE, snake.get_x(), snake.get_y())
      #get rid of tail to make it look like its moving
      draw_object(game_map, BLACK, tail[0], tail[1])
      return food


if __name__ == '__main__':
  #add a delay - more user friendly
  pygame.time.delay(200)

  game_map = Map(WIDTH, OBJECT_RADIUS)
  #create a snake at a random point
  snake = Snake(1, 5, 5, game_map.get_map_size())
  #make food
  food = game_map.make_ball(snake)

  #draw the snake and food
  draw_object(game_map, BLUE, snake.get_x(), snake.get_y())
  draw_object(game_map, RED, food.get_x(), food.get_y())

  #previous direction matters because if you are moving left, you cannot move right - so initally set the direction of the snake to move right at the beginning of the game
  previously_moved = pygame.K_RIGHT

  while snake.is_alive():
    pygame.time.delay(TICK)

    for event in pygame.event.get():
      #quit the game
      if event.type == pygame.QUIT:
        pygame.quit()
      elif event.type == pygame.KEYDOWN:
        #pause the game
        if event.key == pygame.K_p:
          paused = True
          #how do we use a loop to pause the game?
          while paused:
            for pause_event in pygame.event.get():
              if (pause_event.type == pygame.KEYDOWN) and (pause_event.key == pygame.K_p):
                paused = False
        elif (event.key == pygame.K_RIGHT) and (previously_moved != pygame.K_LEFT):
          previously_moved = pygame.K_RIGHT
        elif (event.key == pygame.K_LEFT) and (previously_moved != pygame.K_RIGHT):
          previously_moved = pygame.K_LEFT
        elif (event.key == pygame.K_UP) and (previously_moved != pygame.K_DOWN):
          previously_moved = pygame.K_UP
        elif (event.key == pygame.K_DOWN) and (previously_moved != pygame.K_UP):
          previously_moved = pygame.K_DOWN

    food = handle_action(previously_moved, snake, food, game_map)

    pygame.display.update()

  pygame.time.delay(500)
  pygame.quit()
