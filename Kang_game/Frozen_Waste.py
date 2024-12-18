import sys
import pygame

class Game:
    def __init__(self):
        pygame.init()

        pygame.display.set_caption("My game")
        self.screen = pygame.display.set_mode((800,800))
        self.clock = pygame.time.Clock()

    def main_menu(self):
        self.background_image = pygame.image.load("Imgs/main_menu.png")

        self.start_button_image = pygame.image.load("Imgs/start_button.png")
        self.start_button_image = pygame.transform.scale(self.start_button_image, (300, 300))
        self.start_button_rect = self.start_button_image.get_rect(center = (400, 325))

        self.tutorial_button_image = pygame.image.load("Imgs/tutorial_button.png")
        self.tutorial_button_image = pygame.transform.scale(self.tutorial_button_image, (300, 300))
        self.tutorial_button_rect = self.tutorial_button_image.get_rect(center = (400, 500))

        self.quit_button_image = pygame.image.load("Imgs/quit_button.png")
        self.quit_button_image = pygame.transform.scale(self.quit_button_image, (300, 300))
        self.quit_button_rect = self.quit_button_image.get_rect(center = (400, 675))

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.start_button_rect.collidepoint(event.pos):
                        self.starting_screen()
                    elif self.quit_button_rect.collidepoint(event.pos):
                        pygame.quit()
                        sys.exit()

            self.screen.blit(self.background_image, (0,0))
            self.screen.blit(self.start_button_image, self.start_button_rect)
            self.screen.blit(self.tutorial_button_image, self.tutorial_button_rect)
            self.screen.blit(self.quit_button_image, self.quit_button_rect)
            pygame.display.update()
            self.clock.tick(60)
    
    def starting_screen(self):
        self.background_image = pygame.image.load("Imgs/background.png")

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self.screen.blit(self.background_image, (0,0))
            pygame.display.update()
            self.clock.tick(60)

Game().main_menu()

