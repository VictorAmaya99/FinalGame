import pygame

class SoundManager:
    def __init__(self):
        pygame.mixer.pre_init(44100, -16, 2, 512)
        pygame.init()
       
        self.coin = pygame.mixer.Sound("./src/assets/sound/coin.mp3")
        self.coin.set_volume(0.5)

        self.cherry = pygame.mixer.Sound("./src/assets/sound/cherry.wav")
        self.cherry.set_volume(0.5)

        self.game_over = pygame.mixer.Sound("./src/assets/sound/game_over.wav")
        self.game_over.set_volume(0.5)

        self.jump = pygame.mixer.Sound("./src/assets/sound/jump.mp3")
        self.jump.set_volume(0.5)

        self.shot = pygame.mixer.Sound("./src/assets/sound/shot.wav")
        self.shot.set_volume(0.5)

        self.fire_rain = pygame.mixer.Sound("./src/assets/sound/fire_rain.mp3")
        self.fire_rain.set_volume(0.5)

        self.flop = pygame.mixer.Sound("./src/assets/sound/game_flop.mp3")
        self.flop.set_volume(0.5)


    def play_coin_sound(self):
        self.coin.play()

    def play_cherry_sound(self):
        self.cherry.play()

    def play_game_over_sound(self):
        self.game_over.play()

    def play_jump_sound(self):
        self.jump.play()

    def play_shot_sound(self):
        self.shot.play()

    def play_fire_rain(self):
        self.fire_rain.play()

    def play_flop_sound(self):
        self.flop.play()
