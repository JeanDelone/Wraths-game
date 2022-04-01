def main():

    import pygame
    from sys import exit

    pygame.init()


    WIDTH = 1600
    HEIGHT = 900
    WIN = pygame.display.set_mode((WIDTH, HEIGHT))
    FPS = 60

    default_hit_cooldown = 60
    default_hit_points = 100
    default_hits_power = 3

    first_player_starting_position = (300,500)
    second_player_starting_position = (WIDTH - 300,500)

    clock = pygame.time.Clock()

    background = pygame.image.load('Images/Others/background-game.png').convert_alpha()
    background_2 = pygame.image.load('Images/Others/background-game-2.png').convert_alpha()
    background_menu = pygame.image.load('Images/Others/background-menu.png').convert_alpha()
    start_text = pygame.image.load('Images/Others/start-text.png').convert_alpha()
    start_text_rect = start_text.get_rect(midbottom = (800, 750))

    sword_attack_1 = pygame.image.load('Images/Swords/attack_1.png').convert_alpha()
    sword_attack_2 = pygame.image.load('Images/Swords/attack_2.png').convert_alpha()
    sword_attack_3 = pygame.image.load('Images/Swords/attack_3.png').convert_alpha()
    sword_attack_4 = pygame.image.load('Images/Swords/attack_4.png').convert_alpha()
    sword_attack_5 = pygame.image.load('Images/Swords/attack_5.png').convert_alpha()
    sword_attack_6 = pygame.image.load('Images/Swords/attack_6.png').convert_alpha()
    sword_attack_7 = pygame.image.load('Images/Swords/attack_7.png').convert_alpha()
    sword_attack_8 = pygame.image.load('Images/Swords/attack_8.png').convert_alpha()
    sword_attack_9 = pygame.image.load('Images/Swords/attack_9.png').convert_alpha()
    sword_attack_10 = pygame.image.load('Images/Swords/attack_10.png').convert_alpha()
    sword_attack_11 = pygame.image.load('Images/Swords/attack_11.png').convert_alpha()
    sword_attack_12 = pygame.image.load('Images/Swords/attack_12.png').convert_alpha()
    sword_attack_13 = pygame.image.load('Images/Swords/attack_13.png').convert_alpha()
    sword_attack_14 = pygame.image.load('Images/Swords/attack_14.png').convert_alpha()
    sword_attack_15 = pygame.image.load('Images/Swords/attack_15.png').convert_alpha()

    flipped_sword_1 = pygame.transform.flip(sword_attack_1, True, False)
    flipped_sword_2 = pygame.transform.flip(sword_attack_2, True, False)
    flipped_sword_3 = pygame.transform.flip(sword_attack_3, True, False)
    flipped_sword_4 = pygame.transform.flip(sword_attack_4, True, False)
    flipped_sword_5 = pygame.transform.flip(sword_attack_5, True, False)
    flipped_sword_6 = pygame.transform.flip(sword_attack_6, True, False)
    flipped_sword_7 = pygame.transform.flip(sword_attack_7, True, False)
    flipped_sword_8 = pygame.transform.flip(sword_attack_8, True, False)
    flipped_sword_9 = pygame.transform.flip(sword_attack_9, True, False)
    flipped_sword_10 = pygame.transform.flip(sword_attack_10, True, False)
    flipped_sword_11 = pygame.transform.flip(sword_attack_11, True, False)
    flipped_sword_12 = pygame.transform.flip(sword_attack_12, True, False)
    flipped_sword_13 = pygame.transform.flip(sword_attack_13, True, False)
    flipped_sword_14 = pygame.transform.flip(sword_attack_14, True, False)
    flipped_sword_15 = pygame.transform.flip(sword_attack_15, True, False)

    sword_attacks = [sword_attack_15, sword_attack_14, sword_attack_13, sword_attack_12, sword_attack_11, sword_attack_10, sword_attack_9, sword_attack_8, sword_attack_7, sword_attack_6, sword_attack_5, sword_attack_4, sword_attack_3, sword_attack_2, sword_attack_1]
    sword_attacks_flipped = [flipped_sword_15, flipped_sword_14, flipped_sword_13, flipped_sword_12, flipped_sword_11, flipped_sword_10, flipped_sword_9, flipped_sword_8, flipped_sword_7, flipped_sword_6, flipped_sword_5, flipped_sword_4, flipped_sword_3, flipped_sword_2, flipped_sword_1]

    blue_wrath = pygame.image.load('Images/Wraths/blue-wrath-2.png').convert_alpha()
    green_wrath = pygame.image.load('Images/Wraths/green-wrath-2.png').convert_alpha()
    pink_wrath = pygame.image.load('Images/Wraths/pink-wrath-2.png').convert_alpha()
    red_wrath = pygame.image.load('Images/Wraths/red-wrath-2.png').convert_alpha()


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


    # In this list there will be dynamically added and removed Sword objects that both players can generate, in main game loop each time player will check for collision from every item in this list
    current_sword_list = []

    class Sword:

        def __init__(self, x, y, image, owner, is_flipped=False):
            self.x = x
            self.y = y
            self.image = image
            self.owner = owner
            self.is_flipped = is_flipped
            self.rectangle = self.image.get_rect(topleft = (self.x, self.y))

    class Wrath:

        # x and y are starting positions for the player, image is image that is supposed to be loaded and pressed_keys is key preset declared before
        # 
        def __init__(self, name, x, y, image, pressed_keys):
            self.name = name
            self.x = x
            self.y = y
            self.image = image
            self.pressed_keys = pressed_keys
            self.x_default_speed = 10
            self.x_velocity = 0
            self.y_velocity = 0
            self.jumps_left = 3
            self.image_flipped = pygame.transform.flip(self.image, True, False)
            self.is_flipped = False
            self.attacked = False
            self.cooldown = 15
            self.rectangle = self.image.get_rect(center = (self.x, self.y))
            self.is_hit = False
            self.hit_cooldown = default_hit_cooldown
            self.hp = default_hit_points


        def jump(self):
            if self.jumps_left > 0:
                self.jumps_left -= 1
                self.y_velocity = -20


    #   natural_move() implicates gravity, makes sure that player won't go outside map, and resets jumps when player hits ground
        def natural_move(self):
            # Checks if player is hit, if so, it applies cooldown to prevent hitting player multiple times in few frames
            if self.is_hit:
                self.hit_cooldown -= 1
                if self.hit_cooldown == 1:
                    self.is_hit = False
                    self.hit_cooldown = default_hit_cooldown
            # Player after getting hit, has applies big x_velocity, this if statement reduces it every frame
            if self.x_velocity != 0:
                if self.x_velocity < 0.1 and self.x_velocity > -0.1:
                    self.x_velocity = 0
                self.x_velocity = self.x_velocity / 1.1
            else:
                self.rectangle.x += self.x_velocity

            # Gravity and moving player
            self.y_velocity += 1.2
            self.rectangle.x += self.x_velocity
            self.rectangle.y += self.y_velocity
            # This makes sure that player is always above 700 lvl, which is floor lvl
            if self.rectangle.y >= HEIGHT - 200:
                self.rectangle.y = HEIGHT - 200
                self.jumps_left = 3
            # This make sure that player doesn't go beyond walls and takes hp when standing too close to it
            if self.rectangle.left <= 30:
                self.hp -= 0.25
                if self.rectangle.left <= 0:
                    self.rectangle.left = 0
                    self.x_velocity = - self.x_velocity
            elif self.rectangle.right >= WIDTH - 30:
                self.hp -= 0.25
                if self.rectangle.right >= WIDTH:
                    self.rectangle.right = WIDTH
                    self.x_velocity = - self.x_velocity


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
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_a:
                        self.pressed_keys["a"] = False
                    if event.key == pygame.K_d:
                        self.pressed_keys["d"] = False
                    if event.key == pygame.K_s:
                        self.pressed_keys["s"] = False
                    if event.key == pygame.K_SPACE:
                        self.attacked = True
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
                    if event.key == pygame.K_RCTRL:
                        self.attacked = True

        def move(self):
            if self.pressed_keys == key_presses_1:
                if self.pressed_keys["a"] == True:
                    self.rectangle.x -= self.x_default_speed
                if self.pressed_keys["d"] == True:
                    self.rectangle.x += self.x_default_speed
                if self.pressed_keys["s"] == True:
                    self.rectangle.y += 5
            else:
                if self.pressed_keys["left"] == True:
                    self.rectangle.x -= self.x_default_speed
                if self.pressed_keys["right"] == True:
                    self.rectangle.x += self.x_default_speed
                if self.pressed_keys["down"] == True:
                    self.rectangle.y += 5

        def attack(self):
            if self.attacked:
                self.cooldown -= 1

                if self.cooldown <= 0:
                    self.attacked = False
                    self.cooldown = 15
                

                elif self.is_flipped:
                    # Numbers that are added to rectangle.x and y are here to initiate sword at exactly middle of the player
                    current_sword = Sword(self.rectangle.x -68, self.rectangle.y +49, sword_attacks_flipped[self.cooldown - 1], self.name, is_flipped=True)
                    current_sword_list.append(current_sword)
                    # print(f"F Sword topright: {current_sword_list[0].rectangle.topright}, {self.name}'s center:{self.rectangle.center}")
                    WIN.blit(current_sword.image, (current_sword.x, current_sword.y))
                else: 
                    current_sword = Sword(self.rectangle.x +34, self.rectangle.y +50, sword_attacks[self.cooldown - 1], self.name)
                    current_sword_list.append(current_sword)
                    # print(f"NF Sword topleft: {current_sword_list[0].rectangle.topleft}, {self.name}'s center:{self.rectangle.center}")
                    WIN.blit(current_sword.image, (self.rectangle.center))

        def sword_collision(self):
            for sword in current_sword_list:
                if self.is_hit == False:
                    if self.rectangle.colliderect(sword.rectangle) and sword.owner != self.name:
                        self.is_hit = True
                        if sword.is_flipped:
                            self.y_velocity = -((101 - self.hp) * default_hits_power) / 6
                            self.x_velocity -= ((101 - self.hp) * default_hits_power) / 1.3
                            print(f"FLIPPED COLLISION! {self.name} collided with {sword.owner}'s sword")
                        else:
                            self.y_velocity = -((101 - self.hp) * default_hits_power) / 6
                            self.x_velocity += ((101 - self.hp) * default_hits_power) / 1.3
                            print(f"NON FLIPPED COLLISION! {self.name} collided with {sword.owner}'s sword")
                        self.hp -= 10

        def draw_image(self):
            self.sword_collision()
            if self.is_flipped:
                WIN.blit(self.image_flipped, self.rectangle)
            else:
                WIN.blit(self.image, self.rectangle)
            self.attack()
            print(f"{self.name}'hp is: {self.hp}")





    # Place to inicialize players
    green_wrath_1 = Wrath("green", first_player_starting_position[0], first_player_starting_position[1], green_wrath, key_presses_2)
    blue_wrath_1 = Wrath("blue", second_player_starting_position[0], second_player_starting_position[1], blue_wrath, key_presses_1)

    # Game active state determines if player is in the menu or in the game
    game_active = False

    run = True
    while run:

        if game_active:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                green_wrath_1.move_switch()
                blue_wrath_1.move_switch()
                
            green_wrath_1.move()
            blue_wrath_1.move()

            WIN.blit(background_2, (0,0))

            # There is a bug exactly in the 3 lines below that i cannot detect. Basically, there should be only 2 lines, when there is 2, second lane does'nt work. Only if I duplicate 1st line and copy it to 3rd line, code works properly. Without it, whatever character is in 2nd line, he is immune to sword.
            blue_wrath_1.draw_image()
            green_wrath_1.draw_image()
            blue_wrath_1.draw_image()

            green_wrath_1.natural_move()
            blue_wrath_1.natural_move()
            
            current_sword_list.clear()
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