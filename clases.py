from typing import Any
import pygame
from main import FinalGame


def draw_grid(screen, color, size, width, height):
    for line in range(0,20):
        pygame.draw.line(screen, color, (0, line * size), (width, line * size))
        pygame.draw.line(screen, color, (line * size, 0), (line * size, height))

# class Player():
#     def __init__(self, x, y, width):
#         self.images_right = []
#         self.images_left = []
#         self.index = 0
#         self.counter = 0
#         for num in range(0,5):            
#             img_right = pygame.image.load(f"./src/assets/images/play{num}.png").convert_alpha()
#             img_right = pygame.transform.scale(img_right, (50,100))
#             img_left = pygame.transform.flip(img_right, True, False)
#             self.images_right.append(img_right)
#             self.images_left.append(img_left)
#         self.image = self.images_right[self.index]
#         self.img_rect = self.image.get_rect()
#         self.img_rect.x = x
#         self.img_rect.y = y
#         self.img_width = self.image.get_width()
#         self.img_height = self.image.get_height()
#         self.vel_y = 0  #Velocidad en y
#         self.jumped = False  #Controla el salto del jugador
#         self.direction = 0

#         img_jump = pygame.image.load("./src/assets/images/jump.png").convert_alpha()
#         img_jump = pygame.transform.scale(img_jump, (50, 100))
#         self.images_jump = [img_jump]        

#         self.screen_width = width  # Ancho de la pantalla, reemplaza WIDTH con tu valor real
#         self.sprite_width = 45 

#     def update(self, screen, height, list):
#         dx = 0
#         dy = 0
#         walk_cooldown = 5

#         #obtener keypresses
#         key = pygame.key.get_pressed()
#         if key[pygame.K_SPACE] and self.jumped == False:
#             self.vel_y = -20
#             self.jumped = True
#         if key[pygame.K_SPACE] == False:
#             self.jumped = False
#         if key[pygame.K_LEFT]:
#             dx -= 5
#             self.counter += 1
#             self.direction = -1
#         if key[pygame.K_RIGHT]:
#             dx += 5
#             self.counter += 1
#             self.direction = 1
#         if key[pygame.K_LEFT] == False and key[pygame.K_RIGHT] == False:
#             self.counter = 0
#             self.index = 0
#             if self.direction == 1:                
#                 self.image = self.images_right[self.index]
#             if self.direction == -1:                
#                 self.image = self.images_left[self.index]
        
#         if self.jumped:
#             if self.direction == 1:  # Si el jugador se mueve hacia la derecha
#                 self.image = self.images_jump[0]  # Usar la imagen de salto cuando se mueve hacia la derecha
#             elif self.direction == -1:  # Si el jugador se mueve hacia la izquierda
#                 # Voltear la imagen de salto horizontalmente para que coincida con el movimiento hacia la izquierda
#                 self.image = pygame.transform.flip(self.images_jump[0], True, False)

#         if self.img_rect.left < 0:  # No permitir que el jugador se salga por la izquierda
#             self.img_rect.left = 0
#         elif self.img_rect.right > self.screen_width:  # No permitir que el jugador se salga por la derecha
#             self.img_rect.right = self.screen_width
        
#         #animaciones:
#         #self.counter += 1
#         if self.counter > walk_cooldown:
#             self.counter = 0
#             self.index += 1
#             if self.index >= len(self.images_right):
#                 self.index = 0
#             if self.direction == 1:                
#                 self.image = self.images_right[self.index]
#             if self.direction == -1:                
#                 self.image = self.images_left[self.index]

#         #gravedad
#         self.vel_y += 1
#         if self.vel_y > 10:
#             self.vel_y = 10
#         dy += self.vel_y

#         #chequear por colisiones
#         for tile in list:
#             if tile[1].colliderect(self.img_rect.x + dx, self.img_rect.y, self.img_width, self.img_height):
#                 dx = 0
#             if tile[1].colliderect(self.img_rect.x, self.img_rect.y + dy, self.img_width, self.img_height):
#                 if self.vel_y < 0:
#                     dy = tile[1].bottom - self.img_rect.top
#                 elif self.vel_y >= 0:
#                     dy = tile[1].top - self.img_rect.bottom

#         #actualizar player 
#         self.img_rect.x += dx
#         self.img_rect.y += dy

#         if self.img_rect.bottom > height:
#             self.img_rect.bottom = height
#             dy = 0
        
#         if self.img_rect.top < 0:  # Evita que el jugador pase por encima del borde superior de la pantalla
#             self.img_rect.top = 0
#             dy = 0  # Detiene el movimiento vertical

#         screen.blit(self.image, self.img_rect)        

        
# class World():
#     def __init__(self, data, size):    
#         self.tile_list = []
#         self.enemy_rect = None
#         self.enemy_speed = 2
#         self.enemy_direction = 1
#         self.size = size
#         self.dirt_image = pygame.image.load("./src/assets/images/dirt.png").convert_alpha()
#         self.grass_image = pygame.image.load("./src/assets/images/grass.png").convert_alpha()
#         self.enemy1_image = pygame.image.load("./src/assets/images/enemy1.png").convert_alpha()
#         row_count = 0
#         for row in data:
#             col_count = 0
#             for tile in row:
#                 if tile == 1:
#                     img = pygame.transform.scale(self.dirt_image, (self.size, self.size))
#                     img_rect = img.get_rect()
#                     img_rect.x =col_count * self.size
#                     img_rect.y =row_count * self.size
#                     tile = (img, img_rect)
#                     self.tile_list.append(tile)
#                 elif tile == 2:
#                     img = pygame.transform.scale(self.grass_image, (self.size, self.size))
#                     img_rect = img.get_rect()
#                     img_rect.x =col_count * self.size
#                     img_rect.y =row_count * self.size
#                     tile = (img, img_rect)
#                     self.tile_list.append(tile)
#                 elif tile == 3:
#                     img = pygame.transform.scale(self.enemy1_image, (self.size, self.size))
#                     img_rect = img.get_rect()
#                     img_rect.x =col_count * self.size
#                     img_rect.y =row_count * self.size
#                     self.enemy_rect = img_rect
#                     tile = (img, img_rect)
#                     self.tile_list.append(tile)
#                 col_count += 1
#             row_count += 1

#     def update_enemy(self):
#         if self.enemy_rect.x + self.enemy_rect.width >= 2 * self.size or self.enemy_rect.x <= self.size:
#             self.enemy_direction *= -1

#         self.enemy_rect.x += self.enemy_speed * self.enemy_direction

#     def draw(self, screen):
#         for tile in self.tile_list:
#             screen.blit(tile[0], tile[1])

#         self.update_enemy()
#         screen.blit(self.enemy1_image, self.enemy_rect)
           

# class Enemy(pygame.sprite.Sprite):
#     def __init__(self, x, y, size):
#         pygame.sprite.Sprite.__init__(self)
#         self.enemy_img = pygame.image.load("./src/assets/images/enemy1.png")
#         self.enemy_rect = self.enemy_img.get_rect()
#         self.enemy_rect.x = x
#         self.enemy_rect.y = y
#         self.move_direction = 1
#         self.size = size

#     def update(self):
#         if self.enemy_rect.x >= 10 * self.size:
#             self.move_direction = -1
#         elif self.enemy_rect.x <= 0:
#             self.move_direction = 1

    
    
        
        



