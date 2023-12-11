import pygame

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, size):
        pygame.sprite.Sprite.__init__(self)
        self.enemy_img = pygame.image.load("./src/assets/images/enemy1.png").convert_alpha()
        self.image = pygame.transform.scale(self.enemy_img, (size, size))  # Redimensionar la imagen
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y 
        self.move_direction = 1
        self.move_counter = 0

    def update(self):
         self.rect.x += self.move_direction
         self.move_counter += 1
         if abs(self.move_counter) > 50:
             self.move_direction *= -1
             self.move_counter *= -1
