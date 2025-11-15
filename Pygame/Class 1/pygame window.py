# pygame window
import Pygame 
Pygame.init()

window = Pygame.display.set_model(300,400)
window.fill("cycan")

done = False
while not done:
    for event in Pygame.event.get():
        if event.type ==Pygame.QUIT:
            Pygame.quit()

    Pygame.display.flip()      

