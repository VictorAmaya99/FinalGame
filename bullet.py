from typing import Any
import pygame

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, direction, width):
        pygame.sprite.Sprite.__init__(self)
        self.speed = 10
        self.image = pygame.image.load("./src/assets/images/bullet.png")
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.direction = direction
        self.screen_width = width

    def update(self):
        self.rect.x += (self.direction * self.speed)
        if self.rect.right < 0 or self.rect.left > self.screen_width:
            self.kill()

