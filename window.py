import pygame
# pygame.init()
# screen = pygame.display.set_mode((1280,720))
# clock = pygame.time.Clock()
# running = True

# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#     screen.fill("purple")

#     pygame.display.flip()
#     clock.tick(60)

# pygame.quit()


class Window():
    def __init__(self, height, width):
        self.rect = pygame.Rect(0, 0, width, height)
        self.width = width
        self.height = height
        pygame.init()

        # most users and tutorials call it "screen"
        self.screen = pygame.display.set_mode(self.rect.size)

        # self.Player_Hand = Player_Hand()
        # se

        self.sprites_list = []

        # self.add_sprite(Card("Image", 100, 400))

        # self.remove_last_sprite()
    def add_card(self, card_sprite):
        self.sprites_list.append(card_sprite)

    def run():
        clock = pygame.tick.Clock()
        RUNNING = True
        PAUSED = False
