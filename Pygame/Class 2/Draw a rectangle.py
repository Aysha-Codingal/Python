import pygame
pygame.init()

screen = pygame.display.set_mode((400,500))
pygame.display.set_caption("Rectangle")
screen.fill("teal")

pygame.draw.rect(screen,'tomato',pygame.Rect(30,30,60,60))

while True:
    for event in pygame.event.get():
        if event.type == pygame. QUIT:
            quit()
    pygame.display.flip()