import pygame
from manage_sound import SoundManager
from bullet import Bullet
import random

class Soldier(pygame.sprite.Sprite):
    def __init__(self, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.index = 0
        self.counter = 0
        self.width = width
        self.height = height
        for num in range(0, 5):
            image = pygame.image.load(f"./src/assets/images/soldier/en{num}.png").convert_alpha()
            image = pygame.transform.scale(image, (50, 100))
            self.images.append(image)

        self.image = self.images[self.index]
        self.rect = self.image.get_rect()

        self.rect.bottomright = (self.width, self.height)
        self.speed = 2
        self.direction = -1  # Dirección del movimiento, hacia la izquierda

        self.bullet_group = pygame.sprite.Group()

        self.has_shot = False

    # def shoot(self):
    #     if not self.has_shot:
    #         bullet = Bullet(self.rect.centerx, self.rect.centery, self.direction, self.width)
    #         self.bullet_group.add(bullet)
    #         self.has_shot = True  # Cambia el indicador a True para que no dispare más

    def update(self):
        self.rect.x += (self.direction * self.speed)
        self.rect.x += (self.direction * self.speed)
        if self.rect.right < 0 or self.rect.left > self.width:  # Ajusta la posición de desaparición a tu ancho de pantalla
            self.kill() 

        self.counter += 1
        if self.counter >= 10:  # Contador para cambiar la imagen del soldado y dar la sensación de animación
            self.counter = 0
            self.index += 1
            if self.index >= len(self.images):
                self.index = 0
            self.image = self.images[self.index]

        # if self.rect.centerx > self.width * 0.75 and not self.has_shot:
        #     self.shoot() 
      