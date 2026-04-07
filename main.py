import pygame
from cards import Card
pygame.init()

screen = pygame.display.set_mode((1280,720))

clock= pygame.time.Clock()
c1 = Card(1,1)
while True:
    # reads user input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit

    #logic updates (to do later)
    
    
    screen.fill("green")
    screen.blit(c1.image, c1.rect.center)
    #Graphics render (to do)

    pygame.display.flip() # refresh screen display
    clock.tick(60) # wait until next frame (runs 60FPS)
