import pygame
from cards import Card
pygame.init()

'''AU_logo = pygame.image.load("AU_logo.png")
logo_rect = AU_logo.get_rect()'''


screen_width, screen_height = pygame.display.get_desktop_sizes()[0]
screen = pygame.display.set_mode((screen_width, screen_height - 60))

screen.fill("antiquewhite3")

font = pygame.font.SysFont('roboto', 60)

pygame.display.set_caption('The Alfred Casino')

clock= pygame.time.Clock()
c1 = Card(1,1)
c1.create()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    
    screen.fill("green")
    screen.blit(c1.image,c1.rect.center)

    pygame.display.flip() # refresh screen display
    clock.tick(60) # wait until next frame (runs 60FPS)
