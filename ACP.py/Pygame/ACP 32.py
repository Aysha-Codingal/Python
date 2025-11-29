import pygame
import math

pygame.init()

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 150, 0)
PURPLE = (150, 0, 150)

screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Assignment Screen: Rectangle and Text")

font = pygame.font.Font(None, 48)


rect_width = 250
rect_height = 150
rect_x = (SCREEN_WIDTH // 2) - (rect_width // 2)
rect_y = (SCREEN_HEIGHT // 2) - (rect_height // 2) + 50 
my_rectangle = pygame.Rect(rect_x, rect_y, rect_width, rect_height)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE) 

    pygame.draw.rect(screen, GREEN, my_rectangle)

    pygame.draw.rect(screen, BLACK, my_rectangle, 3) 
  

    pygame.display.flip()


pygame.quit()
math.exit()