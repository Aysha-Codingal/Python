import pygame

pygame.init()

SWIDTH = 500 
SHIEGHT = 400
screen = pygame.display.set_mode((SWIDTH, SHIEGHT))
pygame.display.set_caption("Add Sprites and Movement")
mspeed = 3

class Sprite(pygame.sprite.Sprite):
    def __init__(self, color, h, w, x, y):
        super().__init__()
        self.image = pygame.Surface([w, h])
        self.image.fill(color)

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.w = w
        self.h = h

    def move(self, xchange, ychange):
        new_x = self.rect.x + xchange
        new_y = self.rect.y + ychange

        self.rect.x = max(0, min(new_x, SWIDTH - self.w))
        self.rect.y = max(0, min(new_y, SHIEGHT - self.h))

clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group() 

sprite1 = Sprite("green", 30, 30, 235, 300)
all_sprites.add(sprite1)

sprite2 = Sprite("red", 50, 50, 100, 100)
all_sprites.add(sprite2)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    xchange = (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * mspeed
    ychange = (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * mspeed

    sprite1.move(xchange, ychange)

    screen.fill("black") 
    all_sprites.draw(screen)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()