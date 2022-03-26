from tkinter import W


def main():

    import pygame
    from sys import exit

    pygame.init()


    WIDTH = 1600
    HEIGHT = 900
    WIN = pygame.display.set_mode((WIDTH, HEIGHT))
    FPS = 60

    clock = pygame.time.Clock()

    background = pygame.image.load('Images/background-game.png').convert_alpha()
    background_menu = pygame.image.load('Images/background-menu.png').convert_alpha()
    start_text = pygame.image.load('Images/start-text.png').convert_alpha()
    start_text_rect = start_text.get_rect(midbottom = (800, 750))

    sword_attack_1 = pygame.image.load('Images/attack state 1.png').convert_alpha()
    sword_attack_2 = pygame.image.load('Images/attack state 2.png').convert_alpha()
    sword_attack_3 = pygame.image.load('Images/attack state 3.png').convert_alpha()
    sword_attack_4 = pygame.image.load('Images/attack state 4.png').convert_alpha()

    sword_attacks = [sword_attack_1, sword_attack_2, sword_attack_3, sword_attack_4]

    blue_wrath = pygame.image.load('Images/blue-wrath-1.png').convert_alpha()
    green_wrath = pygame.image.load('Images/green-wrath-1.png').convert_alpha()
    pink_wrath = pygame.image.load('Images/pink-wrath-1.png').convert_alpha()
    red_wrath = pygame.image.load('Images/red-wrath-1.png').convert_alpha()


    #   Pressed keys templates, each player will have assigned some keys to move with, and these are hard coded here
    #   I don't think that it's possible to have keys as variables since pygame has hard coded event listeners, for example:
    #
    #   if event.key == pygame.K_a:
    #       move_left()
    #   
    #   In this case, "a" is hard coded in pygame library, so it's almost impossible to have ur keys stored as variables inside constructor of the class
    key_presses_1 = {"w": False,
                    "s": False,
                    "a": False,
                    "d": False,
                    "spacebar": False}
    
    key_presses_2 = {"up": False,
                    "down": False,
                    "left": False,
                    "right": False,
                    "r_control": False}


    class Sword:

        def __init__(self, x, y, owner):
            self.x = x
            self.y = y
            self.owner = owner
            self.frames_left = 30
            self.image = sword_attacks[0]
            self.rectangle = self.image.get_rect(topleft = (self.x, self.y))

        def show(self):
            WIN.blit(self.image, self.rectangle(topleft = (self.x, self.y)))

    class Wrath:

        # x and y are starting positions for the player, image is image that is supposed to be loaded and pressed_keys is key preset declared before
        # 
        def __init__(self, x, y, image, pressed_keys):
            self.x = x
            self.y = y
            self.image = image
            self.pressed_keys = pressed_keys
            self.x_velocity = 10
            self.y_velocity = 0
            self.gravity = 0
            self.jumps_left = 3
            self.image_flipped = pygame.transform.flip(self.image, True, False)
            self.is_flipped = False
            self.is_hit = False
            self.attacked = False
            self.rectangle = self.image.get_rect(topleft = (self.x, self.y))

        def jump(self):
            if self.jumps_left > 0:
                self.jumps_left -= 1
                self.gravity = 0
                self.y_velocity = -20

        def attack(self):
            sword = Sword(self.x, self.y, self.image)
    #   natural_move() implicates gravity, makes sure that player won't go outside map, and resets jumps when player hits ground
        def natural_move(self):
            self.y_velocity += 1.2
            self.rectangle.y += self.y_velocity
            # This makes sure that player is always above 700 lvl, which is floor lvl
            if self.rectangle.y >= 700:
                self.rectangle.y = 700
                self.jumps_left = 3
            # This make sure that player doesn't go beyond walls
            if self.rectangle.left <= 20:
                self.rectangle.left = 20
            if self.rectangle.right >= 1580:
                self.rectangle.right = 1580


    #   There are 2 functions: move_swtich() and move(), each one of them serves purpose to move the player,
    #   move_switch() checks if button is pressed, and when it is, it changes key_pressed[i] boolean to True,
    #   move() checks if button is released, so it can change key_pressed[i] back to False, and player will no longer move
        def move_switch(self):
            if self.pressed_keys == key_presses_1:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        self.jump()
                    if event.key == pygame.K_a:
                        self.pressed_keys["a"] = True
                        self.is_flipped = True
                    if event.key == pygame.K_d:
                        self.pressed_keys["d"] = True
                        self.is_flipped = False
                    if event.key == pygame.K_s:
                        self.pressed_keys["s"] = True
                    if event.key == pygame.K_SPACE:
                        WIN.blit(sword_attacks[0], (200,200))
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_a:
                        self.pressed_keys["a"] = False
                    if event.key == pygame.K_d:
                        self.pressed_keys["d"] = False
                    if event.key == pygame.K_s:
                        self.pressed_keys["s"] = False
                    if event.key == pygame.K_SPACE:
                        WIN.blit(sword_attacks[0], (200,200))
            else:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.jump()
                    if event.key == pygame.K_DOWN:
                        self.pressed_keys["down"] = True
                    if event.key == pygame.K_LEFT:
                        self.pressed_keys["left"] = True
                        self.is_flipped = True
                    if event.key == pygame.K_RIGHT:
                        self.is_flipped = False
                        self.pressed_keys["right"] = True
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_DOWN:
                        self.pressed_keys["down"] = False
                    if event.key == pygame.K_LEFT:
                        self.pressed_keys["left"] = False
                    if event.key == pygame.K_RIGHT:
                        self.pressed_keys["right"] = False

        def move(self):
            if self.pressed_keys == key_presses_1:
                if self.pressed_keys["a"] == True:
                    self.rectangle.x -= self.x_velocity
                if self.pressed_keys["d"] == True:
                    self.rectangle.x += self.x_velocity
                if self.pressed_keys["s"] == True:
                    self.rectangle.y += 5
            else:
                if self.pressed_keys["left"] == True:
                    self.rectangle.x -= self.x_velocity
                if self.pressed_keys["right"] == True:
                    self.rectangle.x += self.x_velocity
                if self.pressed_keys["down"] == True:
                    self.rectangle.y += 5

        def draw_image(self):
            if self.is_flipped:
                WIN.blit(self.image_flipped, self.rectangle)
            else:
                WIN.blit(self.image, self.rectangle)




    # Place to inicialize players
    red_wrath_1 = Wrath(500,600, red_wrath, key_presses_1)
    pink_wrath_1 = Wrath(1100,600, pink_wrath, key_presses_2)

    # Game active state determines if player is in the menu or in the game
    game_active = False

    run = True
    while run:

        if game_active:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                red_wrath_1.move_switch()
                pink_wrath_1.move_switch()
                
            red_wrath_1.move()
            pink_wrath_1.move()

            WIN.blit(background, (0,0))

            red_wrath_1.draw_image()
            pink_wrath_1.draw_image()

            red_wrath_1.natural_move()
            pink_wrath_1.natural_move()
            # if red_wrath_1.rectangle.colliderect(pink_wrath_1.rectangle):
            #     if red_wrath_1.rectangle.right > pink_wrath_1.rectangle.left and red_wrath_1.rectangle.left < pink_wrath_1.rectangle.right:
            #         red_wrath_1.rectangle.right = pink_wrath_1.rectangle.left

        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if start_text_rect.collidepoint(pygame.mouse.get_pos()):
                        game_active = True

            WIN.blit(background_menu, (0,0))
            WIN.blit(start_text, start_text_rect)

            


        pygame.display.update()
        clock.tick(FPS)



if __name__ == '__main__':
    main()