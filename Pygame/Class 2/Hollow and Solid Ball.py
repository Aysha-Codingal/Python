import pygame
pygame.init()

screen = pygame.display.set_mode((400,500))
pygame.display.set_caption("Rectangle")
screen.fill("black")

pygame.draw.rect(screen,'pink',pygame.Rect(30,30,60,60))
pygame.draw.circle(screen,'deeppink',(200,100),30)
pygame.draw.circle(screen,'white',(100,200),30,3)
while True:
    for event in pygame.event.get():
        if event.type == pygame. QUIT:
            quit()
    pygame.display.flip()