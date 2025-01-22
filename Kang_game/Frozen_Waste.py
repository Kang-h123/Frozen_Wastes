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
        self.character_image = pygame.image.load("Imgs/character.png")
        self.character_image = pygame.transform.scale(self.character_image, (30, 80)) 
        self.floor_image = pygame.image.load("Imgs/ground.png")
        self.floor_image = pygame.transform.scale(self.floor_image, (200, 50))  

        rect_x, rect_y = 200, 700
        rect1_x, rect1_y = 550, 700
        
        self.floor_rect = self.floor_image.get_rect(topleft=(0, 750))  

        self.floor_rect1 = self.floor_image.get_rect(topleft=(350, 750))

        # Character properties
        char_x, char_y = 50, 600 
        char_velocity_x = 0
        char_velocity_y = 0
        gravity = 1
        jump_power = -15
        on_floor = False

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        char_velocity_x = 5  
                    if event.key == pygame.K_LEFT:
                        char_velocity_x = -5  
                    if event.key == pygame.K_SPACE and on_floor:  
                        char_velocity_y = jump_power

                if event.type == pygame.KEYUP:
                    if event.key in [pygame.K_RIGHT, pygame.K_LEFT]:
                        char_velocity_x = 0  

            
            char_velocity_y += gravity

            
            char_x -= char_velocity_x
            rect_x -= char_velocity_x
            rect1_x -= char_velocity_x
            char_y += char_velocity_y

            char_y, char_velocity_y, a = self.check_collision(char_x, char_y, char_velocity_y, rect_x, rect_y)
            char_y, char_velocity_y, b = self.check_collision(char_x, char_y, char_velocity_y, rect1_x, rect1_y)


            on_floor = a or b


            char_x = max(200, min(char_x, 650))  

            # Draw background, floor, and character
            self.screen.blit(self.background_image, (0, 0))
            self.screen.blit(self.floor_image, (rect_x, rect_y))
            self.screen.blit(self.floor_image, (rect1_x, rect1_y ))
            self.screen.blit(self.character_image, (char_x, char_y))

            pygame.display.update()
            self.clock.tick(60)

    def check_collision(self, char_x, char_y, char_velocity_y, rectx, recty):
        on_floor = False
        
        if char_y + 80 > recty:  
            if rectx <= char_x <= rectx + 200 or \
                rectx <= char_x + 30 <= rectx + 200:
                char_y = recty - 80 
                char_velocity_y = 0  
                on_floor = True
            else:
                on_floor = False
        else:
            on_floor = False
            
        return char_y, char_velocity_y, on_floor

Game().main_menu()

