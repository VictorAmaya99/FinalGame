import pygame
from exit import Exit
from coin import Coin
from cherry import Cherry
from enemy import Enemy
from plataforma import Platform
from ghost import Ghost

class World2():
    def __init__(self, level, tile_size):
        self.tile_list2 = []
        self.tile_size = tile_size
        self.ghost_group = pygame.sprite.Group()
        self.enemy_group = pygame.sprite.Group()
        self.exit_group = pygame.sprite.Group()
        self.coin_group = pygame.sprite.Group()
        self.cherry_group = pygame.sprite.Group()
        self.platform_group = pygame.sprite.Group()
        self.level = level
        self.dirt_image = pygame.image.load("./src/assets/images/dirt.png").convert_alpha()
        self.grass_image = pygame.image.load("./src/assets/images/grass.png").convert_alpha()
        self.world_data = Level2()        
        row_count = 0
        for row in self.world_data.data2:
            col_count = 0
            for tile in row:
                if tile == 1:
                    img = pygame.transform.scale(self.dirt_image, (self.tile_size, self.tile_size))
                    img_rect = img.get_rect()
                    img_rect.x =col_count * self.tile_size
                    img_rect.y =row_count * self.tile_size
                    tile = (img, img_rect)
                    self.tile_list2.append(tile)
                if tile == 2:
                    img = pygame.transform.scale(self.grass_image, (self.tile_size, self.tile_size))
                    img_rect = img.get_rect()
                    img_rect.x =col_count * self.tile_size
                    img_rect.y =row_count * self.tile_size
                    tile = (img, img_rect)
                    self.tile_list2.append(tile)
                if tile == 3:
                    enemy_1 = Enemy(col_count * self.tile_size, row_count * self.tile_size + 10, self.tile_size)
                    self.enemy_group.add(enemy_1)
                if tile == 4:
                    platform = Platform(col_count * self.tile_size, row_count * self.tile_size, 80, 1, 0)
                    self.platform_group.add(platform)
                if tile == 5:
                    platform = Platform(col_count * self.tile_size, row_count * self.tile_size + 10, 80, 0, 1)
                    self.platform_group.add(platform)
                if tile == 6:
                    exit_door = Exit(col_count * self.tile_size, row_count * self.tile_size - (self.tile_size // 2), self.tile_size)
                    self.exit_group.add(exit_door)
                if tile == 7:
                    coin = Coin(col_count * self.tile_size, row_count * self.tile_size - (self.tile_size // 2), self.tile_size)
                    self.coin_group.add(coin)
                if tile == 8:
                    cherry = Cherry(col_count * self.tile_size, row_count * self.tile_size - (self.tile_size // 2), self.tile_size)
                    self.cherry_group.add(cherry)
                if tile == 9:
                    ghost = Ghost(col_count * self.tile_size, row_count * self.tile_size - 15, 50)
                    self.ghost_group.add(ghost)
                col_count += 1
            row_count += 1

   
    def draw(self, screen):
        for tile in self.tile_list2:
            screen.blit(tile[0], tile[1]) 

        self.ghost_group.draw(screen)
        self.platform_group.draw(screen)
        self.exit_group.draw(screen)
        self.coin_group.draw(screen)
        self.cherry_group.draw(screen)
        
    def update_ghosts(self):
        self.ghost_group.update()

    def update_platforms(self):
        self.platform_group.update()


class Level2:
    def __init__(self):
        self.data2 =[
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [2,2,0,0,0,0,0,0,0,0,0,8,0,8,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,7,0,0,0,0,0,0,0,0,0],
        [0,9,0,0,0,8,0,8,0,0,0,0,0,0,0,0,0,0,0,0],
        [2,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,7],
        [1,1,1,0,0,0,0,0,0,0,0,5,0,5,0,0,0,0,9,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,2],
        [0,0,8,0,0,4,0,4,0,0,0,0,0,0,0,0,0,1,1,1],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,8,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,5,0,5,0,0,0,0,0],
        [0,0,4,0,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,8,0,8,0,0,0,0,0,0,8,0,8],
        [0,0,0,0,0,0,0,9,0,0,0,0,0,0,0,0,0,0,9,0],
        [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
        ]

    def get_world_data2(self):
        return self.world_data2
    



