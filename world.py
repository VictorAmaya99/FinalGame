import pygame
from enemy import Enemy
from lava import Lava
from exit import Exit
from coin import Coin
from cherry import Cherry

class World():
    def __init__(self, level, tile_size):
        self.tile_list = []
        self.tile_size = tile_size
        self.enemy_group = pygame.sprite.Group()
        self.lava_group = pygame.sprite.Group()
        self.exit_group = pygame.sprite.Group()
        self.coin_group = pygame.sprite.Group()
        self.cherry_group = pygame.sprite.Group()
        self.level = level
        self.dirt_image = pygame.image.load("./src/assets/images/dirt.png").convert_alpha()
        self.grass_image = pygame.image.load("./src/assets/images/grass.png").convert_alpha()
        world_data = Level()
        row_count = 0
        for row in world_data.data:
            col_count = 0
            for tile in row:
                if tile == 1:
                    img = pygame.transform.scale(self.dirt_image, (self.tile_size, self.tile_size))
                    img_rect = img.get_rect()
                    img_rect.x =col_count * self.tile_size
                    img_rect.y =row_count * self.tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 2:
                    img = pygame.transform.scale(self.grass_image, (self.tile_size, self.tile_size))
                    img_rect = img.get_rect()
                    img_rect.x =col_count * self.tile_size
                    img_rect.y =row_count * self.tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 3:
                    enemy_1 = Enemy(col_count * self.tile_size, row_count * self.tile_size -20, 80)
                    self.enemy_group.add(enemy_1)
                if tile == 4:
                    lava = Lava(col_count * self.tile_size, row_count * self.tile_size + (self.tile_size // 2), self.tile_size)
                    self.lava_group.add(lava)
                if tile == 5:
                    exit_door = Exit(col_count * self.tile_size, row_count * self.tile_size - (self.tile_size // 2), self.tile_size)
                    self.exit_group.add(exit_door)
                if tile == 6:
                    coin = Coin(col_count * self.tile_size, row_count * self.tile_size - (self.tile_size // 2), self.tile_size)
                    self.coin_group.add(coin)
                if tile == 7:
                    cherry = Cherry(col_count * self.tile_size, row_count * self.tile_size - (self.tile_size // 2), self.tile_size)
                    self.cherry_group.add(cherry)
                col_count += 1
            row_count += 1

   
    def draw(self, screen):
        for tile in self.tile_list:
            screen.blit(tile[0], tile[1]) 

        self.enemy_group.draw(screen)
        self.lava_group.draw(screen)
        self.exit_group.draw(screen)
        self.coin_group.draw(screen)
        self.cherry_group.draw(screen)
        
    def update_enemies(self):
        self.enemy_group.update()

    def get_world_data(self):
        return self.world_data
    
class Level:
    def __init__(self):
        self.data =[
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,7,6,0,7],
        [0,0,0,0,0,3,0,0,0,0,0,0,0,0,0,2,2,2,2,2],
        [0,0,0,0,2,2,2,2,0,0,0,0,0,0,0,0,1,1,1,1],
        [7,7,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [2,2,0,0,0,0,0,0,0,0,0,7,0,7,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,7,0,2,2,2,0,0,0,0,0,0],
        [0,0,7,0,0,0,0,0,0,2,2,0,0,0,0,0,0,0,0,0],
        [0,0,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,1,1,0,0,7,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,3,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,2,2,2,2,2,2,0,0,0,0,0,6,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,7,0,0,7,2,2],
        [0,0,0,0,0,0,0,7,0,0,0,0,0,0,0,3,0,0,1,1],
        [0,0,0,0,2,2,2,2,0,0,0,0,0,2,2,2,2,2,1,1],
        [0,0,0,0,1,1,1,1,4,4,4,4,4,1,1,1,1,1,1,1],
        [2,2,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
        ]

    
    



