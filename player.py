import pygame
from manage_sound import SoundManager

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, width):
        pygame.sprite.Sprite.__init__(self)
        self.images_right = []
        self.images_left = []
        self.index = 0
        self.counter = 0
        for num in range(0,5):            
            img_right = pygame.image.load(f"./src/assets/images/player/play{num}.png").convert_alpha()
            img_right = pygame.transform.scale(img_right, (50,100))
            img_left = pygame.transform.flip(img_right, True, False)
            self.images_right.append(img_right)
            self.images_left.append(img_left)
        self.image = self.images_right[self.index]
        self.img_rect = self.image.get_rect()
        self.img_rect.x = x
        self.img_rect.y = y
        self.img_rect.width = self.image.get_width()
        self.img_rect.height = self.image.get_height()
        self.vel_y = 0  #Velocidad en y
        self.jumped = False  #Controla el salto del jugador
        self.direction = 0

        self.rect = self.img_rect

        self.sound = SoundManager()

        #cargar imagen donde salta
        img_jump = pygame.image.load("./src/assets/images/jump.png").convert_alpha()
        img_jump = pygame.transform.scale(img_jump, (50, 100))
        self.images_jump = [img_jump]      

       
        self.screen_width = width  # Ancho de la pantalla, reemplaza WIDTH con tu valor real
        self.sprite_width = 45
        self.shoot = False

          #cargar imagen del shield
        self.shield_img = pygame.image.load("./src/assets/images/shield.png").convert_alpha()
        self.shield_img = pygame.transform.scale(self.shield_img, (150,150))              


        self.shield_active = False
        self.shield_timer = pygame.time.get_ticks()
        self.shield_duration = 18000


    def activate_shield(self):
        self.shield_active = True
        self.shield_timer = pygame.time.get_ticks()
        # print("Shield activated at:", self.shield_timer)

    def deactivate_shield(self):
        # Lógica para desactivar el escudo
        self.shield_active = False

    def update_shield(self):
        if self.shield_active:
            current_time = pygame.time.get_ticks()
            # print("Current time:", current_time)
            if current_time - self.shield_timer >= self.shield_duration:  # Convierte segundos a milisegundos
                self.shield_active = False 
                # print("Shield deactivated at:", current_time)

    def update_shield1(self, screen, list):
        shield_collision = pygame.sprite.spritecollideany(self, list)
        if shield_collision:
            self.shield_active = True
            
        if self.shield_active:
            screen.blit(self.shield_img, (self.img_rect.x - 50, self.img_rect.y - 30))  # Dibuja el escudo en la posición del jugador       
          
    def update(self, screen, height, list):
        dx = 0
        dy = 0
        walk_cooldown = 5

        #obtener keypresses
        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE] and self.jumped == False:
            self.vel_y = -20
            self.sound.play_jump_sound()
            self.jumped = True
        if key[pygame.K_SPACE] == False:
            self.jumped = False
        if key[pygame.K_LEFT]:
            dx -= 5
            self.counter += 1
            self.direction = -1
        if key[pygame.K_RIGHT]:
            dx += 5
            self.counter += 1
            self.direction = 1
        if key[pygame.K_LEFT] == False and key[pygame.K_RIGHT] == False:
            self.counter = 0
            self.index = 0
            if self.direction == 1:                
                self.image = self.images_right[self.index]
            if self.direction == -1:                
                self.image = self.images_left[self.index]
        if key[pygame.K_s]:
            self.shoot = True
            self.sound.play_shot_sound()
        if key[pygame.K_s] == False:
            self.shoot = False
        
        if self.jumped:
            if self.direction == 1:  # Si el jugador se mueve hacia la derecha
                self.image = self.images_jump[0]  # Usar la imagen de salto cuando se mueve hacia la derecha
            elif self.direction == -1:  # Si el jugador se mueve hacia la izquierda
                # Voltear la imagen de salto horizontalmente para que coincida con el movimiento hacia la izquierda
                self.image = pygame.transform.flip(self.images_jump[0], True, False)

        if self.img_rect.left < 0:  # No permitir que el jugador se salga por la izquierda
            self.img_rect.left = 0
        elif self.img_rect.right > self.screen_width:  # No permitir que el jugador se salga por la derecha
            self.img_rect.right = self.screen_width
        
        #animaciones:
        #self.counter += 1
        if self.counter > walk_cooldown:
            self.counter = 0
            self.index += 1
            if self.index >= len(self.images_right):
                self.index = 0
            if self.direction == 1:                
                self.image = self.images_right[self.index]
            if self.direction == -1:                
                self.image = self.images_left[self.index]

        #gravedad
        self.vel_y += 1
        if self.vel_y > 10:
            self.vel_y = 10
        dy += self.vel_y

        #chequear por colisiones
        for tile in list:
            if tile[1].colliderect(self.img_rect.x + dx, self.img_rect.y, self.img_rect.width, self.img_rect.height):
                dx = 0
            if tile[1].colliderect(self.img_rect.x, self.img_rect.y + dy, self.img_rect.width, self.img_rect.height):
                if self.vel_y < 0:
                    dy = tile[1].bottom - self.img_rect.top
                    self.vel_y = 0
                elif self.vel_y >= 0:
                    dy = tile[1].top - self.img_rect.bottom
                    self.vel_y = 0
        
        #actualizar player 
        self.img_rect.x += dx
        self.img_rect.y += dy

        if self.img_rect.bottom > height:
            self.img_rect.bottom = height
            dy = 0
        
        if self.img_rect.top < 0:  # Evita que el jugador pase por encima del borde superior de la pantalla
            self.img_rect.top = 0
            dy = 0  # Detiene el movimiento vertical

            
        screen.blit(self.image, self.img_rect)

        

    
   