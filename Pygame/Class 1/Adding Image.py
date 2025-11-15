# pygame window
import pygame 
pygame.init()

window = pygame.display.set_mode((300,400))
window.fill("cyan")
bg = pygame.transform.scale(pygame.image.load("RedSelector.png").convert(),(300,400))

done = False
while not done:
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            pygame.quit()
        window.blit(bg,(0,0))            
        

    pygame.display.flip()      

