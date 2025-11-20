import pygame
pygame.init()


screen = pygame.display.set_mode((400,500))
pygame.display.set_caption("Rectangle")
screen.fill("black")
x = 100
y = 100
pygame.draw.rect(screen,'pink',pygame.Rect(x,y,30,30))


while True:
    screen.fill("black")
    for event in pygame.event.get():
        if event.type == pygame. QUIT:
            quit()
        pressed = pygame.key.get_pressed    
        if pressed[pygame.K_UP]:
            y = y - 5
        if pressed[pygame.K_DOWN]:
            y = y + 5
        if pressed[pygame.K_LEFT]:
            y = x - 5
        if pressed[pygame.K_RIGHT]:
            x = y + 5
    pygame.draw.rect(screen,'pink',pygame.Rect(x,y,30,30))


    


    pygame.display.flip()