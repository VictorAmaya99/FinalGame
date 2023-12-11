import pygame

class DangerButton(pygame.sprite.Sprite):
    def __init__(self, image_path, position, size):
        pygame.sprite.Sprite.__init__(self)
        loaded_image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(loaded_image, size)
        self.rect = self.image.get_rect(topleft=position)
        self.clicked = False

    def is_clicked(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)
    
