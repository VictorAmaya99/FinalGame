import pygame

class Exit(pygame.sprite.Sprite):
    def __init__(self, x, y, size):
        pygame.sprite.Sprite.__init__(self)
        self.exit_img = pygame.image.load("./src/assets/images/exit_door.png").convert_alpha()
        self.image = pygame.transform.scale(self.exit_img, (size, int(size *1.5)))  # Redimensionar la imagen
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y 