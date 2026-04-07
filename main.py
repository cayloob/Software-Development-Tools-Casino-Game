import pygame

pygame.init()

'''AU_logo = pygame.image.load("AU_logo.png")
logo_rect = AU_logo.get_rect()'''


screen_width, screen_height = pygame.display.get_desktop_sizes()[0]
screen = pygame.display.set_mode((screen_width, screen_height - 60))

screen.fill("antiquewhite3")

font = pygame.font.SysFont('roboto', 60)

pygame.display.set_caption('The Alfred Casino')

running = True
clock = pygame.time.Clock()


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    text = font.render("Welcome to the Alfred Casino", True, "white")
    textrect = text.get_rect()
    textrect.center = (screen_width/2, screen_height/6)

    screen.blit(text, textrect)
    pygame.display.flip()  # refresh screen display
    #clock.tick(60) # wait until next frame (runs 60FPS)

pygame.quit()
