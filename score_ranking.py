
import pygame

class ScorePopup:
    def __init__(self, screen, width, height):
        self.screen = screen
        self.width = width
        self.height = height
        self.score = 0

        self.popup_width = 300
        self.popup_height = 200
        self.popup_rect = pygame.Rect((width - self.popup_width) // 2, (height - self.popup_height) // 2, self.popup_width, self.popup_height)

        self.exit_button_width = 30
        self.exit_button_height = 30
        self.exit_button_rect = pygame.Rect(self.popup_rect.right - self.exit_button_width, self.popup_rect.top, self.exit_button_width, self.exit_button_height)
        self.exit_button_text = "X"
        self.exit_button_font = pygame.font.Font(None, 36)
        self.exit_button_text_surface = self.exit_button_font.render(self.exit_button_text, True, (255, 0, 0))
        self.exit_button_text_rect = self.exit_button_text_surface.get_rect(center=self.exit_button_rect.center)

        self.score_text = f"Score: {self.score}"
        self.score_font = pygame.font.Font(None, 28)
        self.score_text_surface = self.score_font.render(self.score_text, True, (255, 255, 255))
        self.score_text_rect = self.score_text_surface.get_rect(center=(self.popup_rect.centerx, self.popup_rect.centery - 20))        
    
    def set_score(self, score):
        self.score = score

    def draw(self):
        pygame.draw.rect(self.screen, (0, 0, 0), self.popup_rect)
        pygame.draw.rect(self.screen, (255, 0, 0), self.exit_button_rect)
        self.screen.blit(self.exit_button_text_surface, self.exit_button_text_rect)

        # Renderizar el texto del puntaje con la fuente definida para el puntaje
        self.score_text_surface = self.score_font.render(f"Score: {self.score}", True, (255, 255, 255))
        self.score_text_rect = self.score_text_surface.get_rect(center=(self.popup_rect.centerx, self.popup_rect.centery - 20))
        self.screen.blit(self.score_text_surface, self.score_text_rect)

    def check_exit(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.exit_button_rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0]:
                return True
        return False



