import pygame
import random

class FireRain(pygame.sprite.Sprite):
    def __init__(self, width):
        pygame.sprite.Sprite.__init__(self)
        self.width = width
        self.fire_img = pygame.image.load("./src/assets/images/fire.png").convert_alpha()
        self.fire_img = pygame.transform.scale(self.fire_img, (40,40))
        self.image = self.fire_img  # Definir el atributo image
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, self.width - self.rect.width)
        self.rect.y = random.randint(-100, -40)
        self.speed_y = random.randint(4, 10)

        self.creation_time = pygame.time.get_ticks()
        self.duration = 15000

    def update(self):
        current_time = pygame.time.get_ticks()
        time_elapsed = current_time - self.creation_time

        if time_elapsed >= self.duration:
            self.kill()
        else:
            self.rect.y += self.speed_y
            if self.rect.top > self.width + 10:
                self.rect.x = random.randint(0, self.width - self.rect.width)
                self.rect.y = random.randint(-100, -40)
                self.speed_y = random.randint(4, 10)




