import pygame

pygame.init()

screen = pygame.display.set_mode((1280,720))

clock= pygame.time.Clock()

while True:
    # reads user input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit

    #logic updates (to do later)
    

    screen.fill("green")

    #Graphics render (to do)

    pygame.display.flip() # refresh screen display
    clock.tick(60) # wait until next frame (runs 60FPS)
