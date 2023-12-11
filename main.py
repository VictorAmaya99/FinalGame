import pygame
from config import *
from pygame.locals import *
from pygame import mixer
from player import Player
from world import World, Level 
from world2 import World2, Level2
from world3 import World3, Level3
from bullet import Bullet
from fire import FireRain
from danger_button import DangerButton
from manage_sound import SoundManager
from gestor_niveles import GestorNiveles, Nivel
from level_screen import LevelScreen
from data_manager import DBManager
from score_ranking import ScorePopup

class FinalGame:
    def __init__(self) -> None:
        pygame.mixer.pre_init(44100, -16, 2, 512)
        mixer.init()
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Jumping shooter")
        self.icon = pygame.image.load("./src/assets/images/idle.png")
        pygame.display.set_icon(self.icon)

        self.clock = pygame.time.Clock()
        
        #Cargar imagenes
        self.bg_image = pygame.image.load("./src/assets/images/sky.png").convert_alpha()
        self.bg_image = pygame.transform.scale(self.bg_image, (WIDTH, HEIGHT))
        self.sun_image = pygame.image.load("./src/assets/images/sun.png").convert_alpha()  
        self.sun_image = pygame.transform.scale(self.sun_image, SUN_SIZE)
        self.sun_rect = self.sun_image.get_rect(midtop = (350, 40))

        #Imagen del Pause:
        self.pause_image = pygame.image.load("./src/assets/images/pause.jpg")
        self.pause_width = 250
        self.pause_height = 200
        self.pause_image = pygame.transform.scale(self.pause_image, (self.pause_width, self.pause_height))
        self.pause_rect = self.pause_image.get_rect(center = (WIDTH //2, HEIGHT //2))

        #musica de fondo:
        pygame.mixer.music.load("./src/assets/sound/music.wav")
        pygame.mixer.music.play(-1)
        self.sound_up = pygame.image.load("./src/assets/images/volume_up.png")
        self.sound_down = pygame.image.load("./src/assets/images/volume_down.png")
        self.sound_mute = pygame.image.load("./src/assets/images/volume_muted.png")
        self.sound_max = pygame.image.load("./src/assets/images/volume_max.png")

        #para cargar sonidos:
        self.sound_manager = SoundManager()
        
        #Definir variables
        self.tile_size = 40
        self.tile_size2 = 40
        self.tile_size3 = 40
        
        self.player_start_x = 80
        self.player_start_y = HEIGHT - 130

        self.test_font = pygame.font.Font(None, 36)
              
        self.level_instance = Level()
        self.world = World(self.level_instance, self.tile_size)

        self.level_2 = Level2()
        self.world_2 = World2(self.level_2, self.tile_size2)

        self.level_3 = Level3()
        self.world_3 = World3(self.level_3, self.tile_size3, WIDTH, HEIGHT)

        self.player = Player(self.player_start_x, self.player_start_y, WIDTH)
        self.player_group = pygame.sprite.Group()
        self.player_group.add(self.player)

        self.bullet_group = pygame.sprite.Group()
        self.player_shoot = False

        self.current_level = 1
        self.id_player = 1 * 1000

        self.running = True
        self.game_over = False
        self.playing_game = True
        
        self.score = 0
        self.lives = 3

        self.start_time = pygame.time.get_ticks()  # Tiempo de inicio del juego
        self.timer_offset = (WIDTH // 2, 20)
        self.elapsed_time = 0
        self.time_limit = 40000
        self.current_time = 0        
        self.remaining_time = 0

        self.fire_group = pygame.sprite.Group()
        self.create_fire_rain()

        self.fire_rain_active = False

        self.danger_btn_img = "./src/assets/images/danger_btn.png"
        self.danger_btn_pos = (30, 70)

        self.danger_btn = DangerButton(self.danger_btn_img, self.danger_btn_pos, BUTTON_SIZE)

        self.paused = False

        self.level_number = 1 

        self.db_manager = DBManager()
        self.gestor = GestorNiveles()

        self.level_start_screen = LevelScreen(self.screen, CUSTOM2, WIDTH, HEIGHT)
        self.showing_level_screen = True

        self.volume_down_pressed = False
        self.volume_up_pressed = False
        self.volume_mute_pressed = False
        self.volume_max_pressed = False

    def cargar_niveles(self):
        # Cargar la partida desde un archivo JSON
        self.gestor.cargar_partida('partida.json')

    def guardar_niveles(self):
        # Guardar la partida en un archivo JSON
        self.gestor.guardar_partida('partida.json')

    def ejecutar(self):
        # Creación de los objetos de niveles
        world_data_nivel1 = [[1, 1], [2, 2]]
        tile_size_nivel1 = 32

        world_data_nivel2 = [[3, 3], [4, 4]]
        tile_size_nivel2 = 32

        world_data_nivel3 = [[5, 5], [6, 6]]
        tile_size_nivel3 = 32

        # Crear niveles y agregarlos al gestor
        nivel1 = Nivel(world_data_nivel1, tile_size_nivel1)
        nivel2 = Nivel(world_data_nivel2, tile_size_nivel2)
        nivel3 = Nivel(world_data_nivel3, tile_size_nivel3)

        self.gestor.agregar_nivel('nivel1', nivel1)
        self.gestor.agregar_nivel('nivel2', nivel2)
        self.gestor.agregar_nivel('nivel3', nivel3)

        # Guardar la partida
        self.guardar_niveles()

        # Cargar la partida
        self.cargar_niveles()

        # Acceder a los niveles cargados en el gestor
        niveles_cargados = self.gestor.niveles
        print(niveles_cargados)

    def save_score_to_db(self):
        self.db_manager.save_score(self.current_level ,self.score)

    def show_ranking(self):
        latest_scores = self.db_manager.get_latest_scores()
        print("Last game scores by level:")
        for level in latest_scores:
            # Obtener el puntaje del último juego registrado para cada nivel
            score_data = self.db_manager.get_score_by_level(self.current_level)
            print(f"Level {level}: Score: {score_data}")

    def create_fire_rain(self):
        if self.current_level == 3:
            for _ in range(10):  # Puedes ajustar el número de meteoritos como desees
                fire = FireRain(WIDTH)
                self.fire_group.add(fire)

    def update_fire(self):
        self.fire_group.update()

    def activate_fire_rain(self):
        if self.current_level == 3 and not self.fire_rain_active:
            self.fire_rain_active = True
            self.create_fire_rain()
            self.fire_rain_active = False    
       
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    self.player_shoot = True
                    bullet = Bullet(self.player.img_rect.centerx + (0.6 * self.player.img_rect.size[0] * self.player.direction), self.player.img_rect.centery, self.player.direction, WIDTH)
                    self.bullet_group.add(bullet)

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_s:
                    self.player_shoot = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.current_level == 3:  # Verificar si estamos en el nivel 3
                    mouse_pos = pygame.mouse.get_pos()
                    if self.danger_btn.is_clicked(mouse_pos):                   
                        # Al presionar el botón, activar la lluvia de meteoritos
                        self.activate_fire_rain()
                        self.sound_manager.play_fire_rain()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    if not self.game_over:  # Evita que se pause el juego si ya terminó
                        self.paused = not self.paused  # Cambia el estado de pausa
                        if self.paused:
                            # Hacer que el juego se detenga mientras esté en pausa
                            pygame.mixer.music.pause()
                            pygame.time.set_timer(pygame.USEREVENT, 0)  # Detener temporizadores
                        else:
                            # Reanudar el juego
                            pygame.mixer.music.unpause()
                            pygame.time.set_timer(pygame.USEREVENT, 1000 // FPS)            
            
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_p:
                    pass
            
            keys = pygame.key.get_pressed()

            if keys[pygame.K_0]:
                pygame.mixer.music.set_volume(max(0.0, pygame.mixer.music.get_volume() - 0.01))
                self.volume_down_pressed = True
            else:
                self.volume_down_pressed = False

            if keys[pygame.K_1]:
                pygame.mixer.music.set_volume(min(1.0, pygame.mixer.music.get_volume() + 0.01))
                self.volume_up_pressed = True
            else:
                self.volume_up_pressed = False

            if keys[pygame.K_m]:
                pygame.mixer.music.set_volume(0.0)
                self.volume_mute_pressed = True                
            else:
                self.volume_mute_pressed = False

            if keys[pygame.K_x]:
                pygame.mixer.music.set_volume(1.0)
                self.volume_max_pressed = True
            else:
                self.volume_max_pressed = False
    
    def render(self):  #render donde va los blits y los draws
        self.screen.blit(self.bg_image, ORIGIN)
        self.screen.blit(self.sun_image, self.sun_rect)

        if self.playing_game:
            lives_text = self.test_font.render(f"Lives: {self.lives}", True, WHITE)
            self.screen.blit(lives_text, (20, 20))

            self.current_time = pygame.time.get_ticks()
            self.elapsed_time = self.current_time - self.start_time
            self.remaining_time = max(self.time_limit - self.elapsed_time, 0)
                                  
            minutes = self.remaining_time // 60000
            seconds = (self.remaining_time // 1000 ) % 60
            timer_text = self.test_font.render(f"Timer: {minutes:02}: {seconds:02}", True, WHITE)
            text_time_rect = timer_text.get_rect(midtop = self.timer_offset)
            self.screen.blit(timer_text, text_time_rect)

            score_text = self.test_font.render(f"Score: {self.score}", True, WHITE)
            score_text_rect = score_text.get_rect(topright = (WIDTH - 20, 20))
            self.screen.blit(score_text, score_text_rect)

            if self.paused:
                self.screen.blit(self.bg_image, (ORIGIN))
                self.screen.blit(self.pause_image, self.pause_rect)
                pygame.display.flip()
                return

            if self.current_level == 1:
                self.world.draw(self.screen)
                self.world.update_enemies()
                self.player.update(self.screen, HEIGHT, self.world.tile_list)                
            elif self.current_level == 2:
                self.world_2.draw(self.screen)
                self.world_2.update_platforms()
                self.world_2.update_ghosts()
                self.player.update(self.screen, HEIGHT, self.world_2.tile_list2) 
            elif self.current_level == 3:                
                self.world_3.draw(self.screen)
                self.world_3.update_monsters()
                self.world_3.update_dragons()
                #self.world_3.update_soldiers()
                self.player.update(self.screen, HEIGHT, self.world_3.tile_list3)
                self.player.update_shield1(self.screen, self.world_3.shield_group) 
                self.player.update_shield()

                if self.current_level == 3 and self.fire_rain_active:
                    self.update_fire()  # Actualizar la lluvia de meteoritos
                
                # Dibujar los meteoritos si la lluvia de meteoritos está activa en el nivel 3
                if self.current_level == 3:
                    self.fire_group.draw(self.screen)

                #if self.current_level == 3:
                self.screen.blit(self.danger_btn.image, self.danger_btn.rect)
                            
            #self.bullet_group.update()
            self.bullet_group.draw(self.screen)

            if self.volume_down_pressed:
                self.screen.blit(self.sound_down, (350,400))
                # Modificar el volumen de manera continua mientras se mantiene presionada la tecla correspondiente
                pygame.mixer.music.set_volume(max(0.0, pygame.mixer.music.get_volume() - 0.01))

            if self.volume_up_pressed:
                self.screen.blit(self.sound_up, (350, 400))
                # Modificar el volumen de manera continua mientras se mantiene presionada la tecla correspondiente
                pygame.mixer.music.set_volume(min(1.0, pygame.mixer.music.get_volume() + 0.01))

            if self.volume_mute_pressed:
                self.screen.blit(self.sound_mute, (350, 400))
                pygame.mixer.music.set_volume(0.0)  # Establecer volumen a 0 cuando se presiona la tecla                

            if self.volume_max_pressed:
                self.screen.blit(self.sound_max, (350, 400))
                pygame.mixer.music.set_volume(1.0)  # Establecer volumen al máximo cuando se presiona la tecla                   
                
            pygame.display.flip()             
                 
    def reset_game(self):
        if self.game_over:
            self.showing_level_screen = True
            self.score = 0
            self.lives = 3
            self.game_over = False
            self.playing_game = False
            self.paused = False
            self.start_time = pygame.time.get_ticks()
            self.save_score_to_db()

            score_popup = ScorePopup(self.screen, WIDTH, HEIGHT)
            showing_score_popup = True

            while showing_score_popup:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.running = False

                score = self.db_manager.get_score_by_level(self.current_level)
                score_popup.set_score(score)

                # Dibujar el popup de puntaje
                score_popup.draw()

                # Comprobar si se hace clic en el botón de salida del popup
                if score_popup.check_exit():
                    showing_score_popup = False
                    self.game_over = False  # Restablecer el juego para el siguiente nivel
                    # Lógica para pasar al siguiente nivel o mostrar la pantalla de nivel               

                pygame.display.flip()
                self.clock.tick(FPS)
                
           
    def check_collisions(self):
        player_rect = self.player.img_rect

        if self.current_level == 1:
            for enemy in self.world.enemy_group:
                if player_rect.colliderect(enemy.rect):
                    self.lives -= 1
                    # Restablecer jugador si pierde una vida
                    if self.lives > 0:
                        self.player.img_rect.x = self.player_start_x
                        self.player.img_rect.y = self.player_start_y
                        self.sound_manager.play_game_over_sound()
                    else:
                        self.game_over = True
                        self.sound_manager.play_flop_sound()
                for bullet in self.bullet_group:
                    if bullet.rect.colliderect(enemy.rect):
                        self.world.enemy_group.remove(enemy)
                        self.bullet_group.remove(bullet)
                        # Incrementar el puntaje u otras acciones cuando una bala golpea a un enemigo
                        self.score += 100  # Ejemplo: Incrementar el puntaje al eliminar un enemigo con una bala

            # Lógica de colisión con lava
            for lava in self.world.lava_group:
                if player_rect.colliderect(lava.rect):
                    self.lives -= 1
                    # Restablecer jugador si pierde una vida
                    if self.lives > 0:
                        self.player.img_rect.x = self.player_start_x
                        self.player.img_rect.y = self.player_start_y
                        self.sound_manager.play_game_over_sound()
                    else:
                        self.game_over = True
                        self.sound_manager.play_flop_sound()
            
            for coin in self.world.coin_group:
                if player_rect.colliderect(coin.rect):
                    self.world.coin_group.remove(coin)
                    self.lives += 1
                    self.sound_manager.play_coin_sound()
                for bullet in self.bullet_group:
                    if bullet.rect.colliderect(coin.rect):
                        self.world.coin_group.remove(coin)
                        self.bullet_group.remove(bullet)
                        # Incrementar vidas u otras acciones cuando una bala recolecta una moneda
                        self.lives += 1  # Ejemplo: Añadir vidas al recoger una moneda con una bala
            
            for cherry in self.world.cherry_group:
                if player_rect.colliderect(cherry.rect):
                    self.world.cherry_group.remove(cherry)
                    self.sound_manager.play_cherry_sound()
                    if self.volume_mute_pressed:
                        self.sound_manager.mute_cherry_sound()                   
                    self.score += 100
                for bullet in self.bullet_group:
                    if bullet.rect.colliderect(cherry.rect):
                        self.world.cherry_group.remove(cherry)
                        self.bullet_group.remove(bullet)
                        # Incrementar el puntaje u otras acciones cuando una bala recolecta una cereza
                        self.score += 100  # Ejemplo: Incrementar el puntaje al recoger una cereza con una bala
                                        
        if self.current_level == 2:
            for platform in self.world_2.platform_group:
                if player_rect.colliderect(platform.rect):
                    self.player.img_rect.bottom = platform.rect.top

            for ghost in self.world_2.ghost_group:
                if player_rect.colliderect(ghost.rect):
                    self.lives -= 1
                    # Restablecer jugador si pierde una vida
                    if self.lives > 0:
                        self.player.img_rect.x = self.player_start_x
                        self.player.img_rect.y = self.player_start_y
                        self.sound_manager.play_game_over_sound()
                    else:
                        self.game_over = True
                        self.sound_manager.play_flop_sound()
                for bullet in self.bullet_group:
                    if bullet.rect.colliderect(ghost.rect):
                        self.world_2.ghost_group.remove(ghost)
                        self.bullet_group.remove(bullet)
                        # Incrementar el puntaje u otras acciones cuando una bala golpea a un enemigo
                        self.score += 100 

            for cherry in self.world_2.cherry_group:
                if player_rect.colliderect(cherry.rect):
                    self.world_2.cherry_group.remove(cherry)
                    self.sound_manager.play_cherry_sound()
                    self.score += 100
                for bullet in self.bullet_group:
                    if bullet.rect.colliderect(cherry.rect):
                        self.world_2.cherry_group.remove(cherry)
                        self.bullet_group.remove(bullet)
                            # Incrementar el puntaje u otras acciones cuando una bala recolecta una cereza
                        self.score += 100 

            for coin in self.world_2.coin_group:
                if player_rect.colliderect(coin.rect):
                    self.world_2.coin_group.remove(coin)
                    self.sound_manager.play_coin_sound()
                    self.lives += 1
                    for bullet in self.bullet_group:
                        if bullet.rect.colliderect(coin.rect):
                            self.world_2.coin_group.remove(coin)
                            self.bullet_group.remove(bullet)
                            # Incrementar vidas u otras acciones cuando una bala recolecta una moneda
                            self.lives += 1  # Ejemplo: Añadir vidas al recoger una moneda con una bala
               
        if self.current_level == 3:
            for monster in self.world_3.monster_group:
                if player_rect.colliderect(monster.rect):
                    self.lives -= 1
                    self.world_3.monster_group.remove(monster)                
                    # Restablecer jugador si pierde una vida
                    if self.lives > 0:
                        self.player.img_rect.x = self.player_start_x
                        self.player.img_rect.y = self.player_start_y
                        self.sound_manager.play_game_over_sound()
                    else:
                        self.game_over = True  # Volver a empezar el juego cuando se agotan las vidas
                        self.sound_manager.play_flop_sound()
                for fire in self.fire_group:
                    if fire.rect.colliderect(monster.rect):
                        self.fire_group.remove(fire)
                        self.world_3.monster_group.remove(monster)
                    if fire.rect.colliderect(player_rect):
                        self.fire_group.remove(fire)
                        self.lives -= 1
                        self.game_over = True
            # Colisiones entre las balas del jugador y los monstruos
            for bullet in self.bullet_group:
                for monster in self.world_3.monster_group:
                    if bullet.rect.colliderect(monster.rect):
                        self.bullet_group.remove(bullet)
                        self.world_3.monster_group.remove(monster)
                        self.score += 100
            
            for dragon in self.world_3.dragon_group:
                if player_rect.colliderect(dragon.rect):
                    self.lives -= 1
                    self.world_3.dragon_group.remove(dragon)                
                    # Restablecer jugador si pierde una vida
                    if self.lives > 0:
                        self.player.img_rect.x = self.player_start_x
                        self.player.img_rect.y = self.player_start_y
                        self.sound_manager.play_game_over_sound()
                    else:
                        self.game_over = True  # Volver a empezar el juego cuando se agotan las vidas
                        self.sound_manager.play_flop_sound()
                for fire in self.fire_group:
                    if fire.rect.colliderect(dragon.rect):
                        self.fire_group.remove(fire)
                        self.world_3.dragon_group.remove(dragon)
                    if fire.rect.colliderect(player_rect):
                        self.fire_group.remove(fire)
                        self.lives -= 1
                        self.game_over = True
            # Colisiones entre las balas del jugador y los monstruos
            for bullet in self.bullet_group:
                for dragon in self.world_3.dragon_group:
                    if bullet.rect.colliderect(dragon.rect):
                        self.bullet_group.remove(bullet)
                        self.world_3.dragon_group.remove(dragon)
                        self.score += 100            

            for shield in self.world_3.shield_group:
                if player_rect.colliderect(shield.rect):
                    self.world_3.shield_group.remove(shield)
                    self.player.activate_shield()

            for fire in self.fire_group:
                if fire.rect.colliderect(player_rect) and self.player.shield_active:
                    self.fire_group.remove(fire)
                    self.score += 200

        if self.score >= 3500:
            self.game_over = True
                    
        if self.lives <= 0:  # Agregar el puntaje al condicional de finalización del juego
            self.reset_game()
                            
    def update(self):
        pygame.display.update()
        self.bullet_group.update()

    def show_level_screen(self):
        if self.showing_level_screen:
            self.level_start_screen.draw()
            if self.level_start_screen.check_start():
                mouse_pos = pygame.mouse.get_pos()
                if self.level_start_screen.btn_1_rect.collidepoint(mouse_pos):
                    self.current_level = 1
                    self.game_over = False
                    self.lives = 3
                    self.score = 0
                    self.start_time = pygame.time.get_ticks()  # Tiempo de inicio del juego
                    self.remaining_time = self.time_limit
                    self.player.img_rect.x = self.player_start_x
                    self.player.img_rect.y = self.player_start_y
                    self.player = Player(self.player_start_x, self.player_start_y, WIDTH)
                    self.level_instance = Level()
                    self.world = World(self.level_instance, self.tile_size)
                    self.playing_game = True
                    self.showing_level_screen = False

                if self.level_start_screen.btn_2_rect.collidepoint(mouse_pos):
                    self.current_level = 2
                    self.game_over = False
                    self.lives = 3
                    self.score = 0
                    self.start_time = pygame.time.get_ticks()  # Tiempo de inicio del juego
                    self.remaining_time = self.time_limit
                    self.player.img_rect.x = self.player_start_x
                    self.player.img_rect.y = self.player_start_y
                    self.player = Player(self.player_start_x, self.player_start_y, WIDTH)
                    self.level_2 = Level2()
                    self.world_2 = World2(self.level_2, self.tile_size2)
                    self.playing_game = True
                    self.showing_level_screen = False
                
                if self.level_start_screen.btn_3_rect.collidepoint(mouse_pos):
                    self.current_level = 3
                    self.game_over = False
                    self.lives = 3
                    self.score = 0
                    self.start_time = pygame.time.get_ticks()  # Tiempo de inicio del juego
                    self.remaining_time = self.time_limit
                    self.player.img_rect.x = self.player_start_x
                    self.player.img_rect.y = self.player_start_y
                    self.player = Player(self.player_start_x, self.player_start_y, WIDTH)
                    self.level_3 = Level3()
                    self.world_3 = World3(self.level_3, self.tile_size3, WIDTH, HEIGHT)
                    self.playing_game = True
                    self.showing_level_screen = False

    def run(self):        
        self.showing_level_screen = False
                     
        while self.running:            
            self.handle_events()
            self.update_fire()
            self.update()            
            self.check_collisions()

            self.current_time = pygame.time.get_ticks()
            self.elapsed_time = self.current_time - self.start_time
            self.remaining_time = max(self.time_limit - self.elapsed_time, 0)
            
            if self.remaining_time <= 0:
                self.game_over = True
                self.save_score_to_db()
                self.reset_game()           
                continue

            self.render()
            self.show_level_screen()              
            self.clock.tick(FPS)

            if self.danger_btn.clicked:  # Verifica si se hizo clic en el botón
                self.activate_fire_rain()

            pygame.display.flip()
            
        self.close()
        self.show_ranking()
    
    def run_game(self):
        while not self.game_over:
            self.handle_events()
            self.update()
            self.check_collisions()
            self.render()
            self.clock.tick(FPS)            
            
        self.reset_game() 
   
    def close(self):
        pygame.quit()
        
if __name__ == "__main__":

    game = FinalGame()
    game.run()


