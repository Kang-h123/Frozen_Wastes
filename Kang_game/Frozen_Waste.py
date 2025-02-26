import sys
import pygame
import time

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
                    elif self.tutorial_button_rect.collidepoint(event.pos):
                        self.tutorial_screen()
                    elif self.quit_button_rect.collidepoint(event.pos):
                        pygame.quit()
                        sys.exit()

            self.screen.blit(self.background_image, (0,0))
            self.screen.blit(self.start_button_image, self.start_button_rect)
            self.screen.blit(self.tutorial_button_image, self.tutorial_button_rect)
            self.screen.blit(self.quit_button_image, self.quit_button_rect)
            pygame.display.update()
            self.clock.tick(60)

    def tutorial_screen(self):

        self.background_image = pygame.image.load("Imgs/tutorial_screen.png")
        self.button_image = pygame.image.load("Imgs/tutorial_close.png")
        self.button_image =  pygame.transform.scale(self.button_image, (300, 75))
        self.tutorial_close_rect = self.button_image.get_rect(center = (250, 675))

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.tutorial_close_rect.collidepoint(event.pos):
                        self.main_menu()

            self.screen.blit(self.background_image, (0, 0))
            self.screen.blit(self.button_image, self.tutorial_close_rect.center)
            pygame.display.update()
            self.clock.tick(60)

    
    def starting_screen(self):

        self.background_image = pygame.image.load("Imgs/background.png")
        self.character_image = pygame.image.load("Imgs/character.png")
        self.character_image = pygame.transform.scale(self.character_image, (30, 80)) 
        self.floor_image = pygame.image.load("Imgs/ground.png")
        self.enemy_image = pygame.image.load("Imgs/ice_enemy.png")
        self.health_image = pygame.image.load("Imgs/full_health.png")
        

        enemy_size_x = 40
        enemy_size_y = 70
        self.enemy_image = pygame.transform.scale(self.enemy_image, (enemy_size_x, enemy_size_y))

        self.all_rect = {"rect1": [200, 700, 200, 50], "rect2": [550, 700, 400, 50], "rect3": [1050, 700, 500, 50]}
        self.all_enemy = {
            "enemy1": [600, 625], "enemy2": [1200, 625]
        }

        for k, v in self.all_enemy.items():
            setattr(self, k, self.enemy_image.get_rect(topleft = (v[0], v[1])))

        for k, v in self.all_rect.items():
            a = k + "_image"
            setattr(self, a, pygame.transform.scale(self.floor_image, (v[-2], v[-1])))
            setattr(self, k, self.floor_image.get_rect(topleft=(v[0], v[1])))
        
        # self.floor_image = pygame.transform.scale(self.floor_image, (200, 50))  

        # rect_x, rect_y = 200, 700
        # rect1_x, rect1_y = 550, 700
        # rect2_x, rect2_y = 800, 700
        # rect3_x, rect3_y = 1000, 700
        
        # self.floor_rect = self.floor_image.get_rect(topleft=(0, 750))  

        # self.floor_rect1 = self.floor_image.get_rect(topleft=(350, 750))

        # self.floor_rect2 =self.floor_image.get_rect(topleft=(700, 750))

        # self.floor_rect3 =self.floor_image.get_rect(topleft=(1050, 750))

        # Character properties
        char_x, char_y = 50, 400 
        char_velocity_x = 0
        char_velocity_y = 0
        gravity = 1
        jump_power = -15
        on_floor = False
        
        health = 3
        self.start = time.time()



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
            for k, v in self.all_rect.items():
                v[0] -= char_velocity_x 
            for k, v in self.all_enemy.items():
                v[0] -= char_velocity_x
            char_y += char_velocity_y



            on_floor = False
            for k, v in self.all_rect.items():
                char_y, char_velocity_y, a = self.check_collision(char_x, char_y, char_velocity_y, v[0],v[1], v[2],v[3])
                on_floor = on_floor or a


            char_x = max(200, min(char_x, 650))  


            if self.touched_enemy(char_x, char_y, self.all_enemy, enemy_size_x, enemy_size_y):
                self.end = time.time()
                if (self.end - self.start) > 0.8:
                    health -= 1
                    self.start = time.time()
                
                

            if health == 3:
                self.health_image = pygame.image.load("Imgs/full_health.png")
            elif health == 2:
                self.health_image = pygame.image.load("Imgs/half_health.png")
            elif health == 1:
                self.health_image = pygame.image.load("Imgs/low_health.png")
            else:
                self.GameOver()

            # Draw background, floor, and character
            self.screen.blit(self.background_image, (0, 0))
            for k, v in self.all_rect.items():
                a = k + "_image"
                self.screen.blit(getattr(self, a), (v[0], v[1]))
            for k, v in self.all_enemy.items():
                self.screen.blit(self.enemy_image, (v[0], v[1]))
            self.screen.blit(self.character_image, (char_x, char_y))
            self.screen.blit(self.health_image, (20, 50))

            pygame.display.update()
            self.clock.tick(60)
            # print(char_x, char_y, self.all_enemy)

    def GameOver(self):
        self.background_image = pygame.image.load("Imgs/game_over.png")

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()



            self.screen.blit(self.background_image, (0, 0))



            pygame.display.update()
            self.clock.tick(60)


    def check_collision(self, char_x, char_y, char_velocity_y, rectx, recty, sizex, sizey):
        on_floor = False
        
        if recty < char_y + 80 < recty + 20:
            if rectx <= char_x <= rectx + sizex or \
               rectx <= char_x + 30 <= rectx + sizex:
                char_y = recty - 80
                char_velocity_y = 0
                on_floor = True
            else:
                on_floor = False
        elif recty + 20 < char_y + 80 < recty + sizey:
            if rectx < char_x + 30 < rectx + (sizex / 2):
                char_x  = rectx - 30
            else:
                char_x = rectx + sizex
            on_floor = False
        
        return char_y, char_velocity_y, on_floor

    def touched_enemy(self, char_x, char_y, enemy_list, enemy_sizex, enemy_sizey):
        touched = False
        for k, v in enemy_list.items():
            if v[0] <= char_x <= v[0] + enemy_sizex or \
                v[0] + enemy_sizex >= char_x + 30 >= v[0]:
                if char_y <= v[1] <= char_y + 80 or \
                    char_y + 80 >= v[1] + enemy_sizey >= char_y:
                        touched = True

        return touched

        


Game().main_menu()

