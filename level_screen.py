import pygame
from score_ranking import ScorePopup

class LevelScreen:
    def __init__(self, screen, color1, width, height):
        self.screen = screen
        self.color = color1
        self.width = width
        self.height = height

        self.start_screen_width = 300
        self.start_screen_height = 200
        self.start_screen_rect = pygame.Rect((width - self.start_screen_width) // 2, (height - self.start_screen_height) // 2, self.start_screen_width, self.start_screen_height)

        self.title_text = "Game Levels"
        self.title_font = pygame.font.Font(None, 36)  # Especifica el tamaño de la fuente (36 aquí)
        self.title_surface = self.title_font.render(self.title_text, True, (255,0,0))  # WHITE es un color definido en tu archivo de configuración

        
        self.title_rect = self.title_surface.get_rect(midtop=self.start_screen_rect.midtop) 
        self.title_rect.y += 30

        self.btn_1_img = pygame.image.load("./src/assets/images/btn_1.png").convert_alpha()
        self.btn_1_width = 50
        self.btn_1_height = 50
        self.btn_1_img = pygame.transform.scale(self.btn_1_img, (self.btn_1_width, self.btn_1_height))
        btn_1_x = self.start_screen_rect.left + 20  # Ejemplo: colocar el botón a 20 píxeles del lado izquierdo del rectángulo de inicio
        btn_1_y = self.start_screen_rect.top + 80  # Ejemplo: colocar el botón a 20 píxeles desde la parte superior del rectángulo de inicio
        self.btn_1_rect = self.btn_1_img.get_rect(topleft=(btn_1_x, btn_1_y))

        self.btn_2_img = pygame.image.load("./src/assets/images/btn_2.png").convert_alpha()
        self.btn_2_width = 50
        self.btn_2_height = 50
        self.btn_2_img = pygame.transform.scale(self.btn_2_img, (self.btn_2_width, self.btn_2_height))
        btn_2_x = self.start_screen_rect.left + 150  # Ejemplo: colocar el botón a 20 píxeles del lado izquierdo del rectángulo de inicio
        btn_2_y = self.start_screen_rect.top + 105  # Ejemplo: colocar el botón a 20 píxeles desde la parte superior del rectángulo de inicio
        self.btn_2_rect = self.btn_2_img.get_rect(center=(btn_2_x, btn_2_y)) 

        self.btn_3_img = pygame.image.load("./src/assets/images/btn_3.png").convert_alpha()
        self.btn_3_width = 50
        self.btn_3_height = 50
        self.btn_3_img = pygame.transform.scale(self.btn_3_img, (self.btn_3_width, self.btn_3_height))
        btn_3_x = self.start_screen_rect.left + 280  # Ejemplo: colocar el botón a 30 píxeles del lado izquierdo del rectángulo de inicio
        btn_3_y = self.start_screen_rect.top + 105  # Ejemplo: colocar el botón a 30 píxeles desde la parte superior del rectángulo de inicio
        self.btn_3_rect = self.btn_3_img.get_rect(midright=(btn_3_x, btn_3_y)) 
        
    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.start_screen_rect)
        self.screen.blit(self.title_surface, self.title_rect)
        self.screen.blit(self.btn_1_img, self.btn_1_rect)
        self.screen.blit(self.btn_2_img, self.btn_2_rect)
        self.screen.blit(self.btn_3_img, self.btn_3_rect)

    def check_start(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.btn_1_rect.collidepoint(mouse_pos): 
            #return 1           
            if pygame.mouse.get_pressed()[0]:                
                return True
        if self.btn_2_rect.collidepoint(mouse_pos): 
            #return 2           
            if pygame.mouse.get_pressed()[0]:                
                return True
        if self.btn_3_rect.collidepoint(mouse_pos):
            #return 3            
            if pygame.mouse.get_pressed()[0]:                
                return True
        return False

    
    
    
# pygame.init()

# screen = pygame.display.set_mode((WIDTH, HEIGHT))

# clock = pygame.time.Clock()

# level = LevelScreen(screen, CUSTOM2, WIDTH, HEIGHT)

# while True:

#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit()

#     screen.fill(YELLOW)
#     level.draw()
#     if level.check_start():
#         print("Botón presionado")

#     pygame.display.update()
#     clock.tick(FPS)

