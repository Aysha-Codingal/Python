import pygame
import random

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Add Sprites - Movement Control")

clock = pygame.time.Clock()
FPS = 60


PLAYER_SIZE = 50
player_x = 100
player_y = SCREEN_HEIGHT // 2 - PLAYER_SIZE // 2
player_rect = pygame.Rect(player_x, player_y, PLAYER_SIZE, PLAYER_SIZE)
PLAYER_SPEED = 5

STATIC_SIZE = 75
static_x = SCREEN_WIDTH - 150
static_y = SCREEN_HEIGHT // 2 - STATIC_SIZE // 2
static_rect = pygame.Rect(static_x, static_y, STATIC_SIZE, STATIC_SIZE)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT]:
        # Move the rectangle horizontally, checking boundaries
        player_rect.x -= PLAYER_SPEED
    if keys[pygame.K_RIGHT]:
        player_rect.x += PLAYER_SPEED
    if keys[pygame.K_UP]:
        player_rect.y -= PLAYER_SPEED
    if keys[pygame.K_DOWN]:
        player_rect.y += PLAYER_SPEED
        
    player_rect.left = max(0, player_rect.left)
    player_rect.right = min(SCREEN_WIDTH, player_rect.right)
    player_rect.top = max(0, player_rect.top)
    player_rect.bottom = min(SCREEN_HEIGHT, player_rect.bottom)


    
    screen.fill(WHITE) 

    pygame.draw.rect(screen, RED, player_rect)

    pygame.draw.rect(screen, BLUE, static_rect)

    pygame.display.flip()
    clock.tick() 


pygame.quit()
random.exit()