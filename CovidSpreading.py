import pygame
from pygame.locals import *
from random import randint

# constants
SIZE = 640, 640
WIDTH, HEIGHT = SIZE
CELLSIZE = 40
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
RUNNING = True
N = 10  # number of people
X = 0
Y = 0
SURFACE = pygame.Surface((CELLSIZE, CELLSIZE))
COORDS = SURFACE.fill(BLUE)

# game
pygame.init()
board = pygame.display.set_mode(SIZE)
crowd_surfaces = []
crowd_coords = []
for i in range(N):
    crowd_surfaces.append(SURFACE)
    crowd_coords.append(COORDS.move([randint(0, WIDTH/CELLSIZE)*CELLSIZE,
                                     randint(0, HEIGHT/CELLSIZE)*CELLSIZE]))  # start from random position

while RUNNING:
    board.fill(BLACK)
    for event in pygame.event.get():
        if event.type == QUIT:
            RUNNING = False

    for i in range(N):   # every person
        pygame.time.delay(100)  # every 100 ms
        X = randint(-1, 1)
        Y = randint(-1, 1)
        crowd_coords[i] = crowd_coords[i].move([CELLSIZE * X, CELLSIZE * Y])  # moves a step in a random direction
        pygame.draw.rect(board, BLUE, crowd_coords[i], 1)
        board.blit(crowd_surfaces[i], crowd_coords[i])
    pygame.display.update()
    print(crowd_coords)
pygame.quit()


# if it would hit a wall
# instead it stays still
# if it would hit a person
# instead it changes color (blue to green to red)
# if it was already red
# it leaves the board
# if there is only one person
# close the game

