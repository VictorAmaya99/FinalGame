import pygame

class Lava(pygame.sprite.Sprite):
    def __init__(self, x, y, size):
        pygame.sprite.Sprite.__init__(self)
        self.enemy_img = pygame.image.load("./src/assets/images/lava.png").convert_alpha()
        self.image = pygame.transform.scale(self.enemy_img, (size, size))  # Redimensionar la imagen
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y 



        
        
