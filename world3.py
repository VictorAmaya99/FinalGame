import pygame
from exit import Exit
from coin import Coin
from cherry import Cherry
from enemy import Enemy
from plataforma import Platform
from ghost import Ghost
from monster import Monster
from dragon import Dragon
from shield1 import Shield1
# from soldier_enemy import Soldier
# from bullet import Bullet

import random

class World3():
    def __init__(self, level, tile_size, width, height):
        self.tile_list3 = []
        self.tile_size = tile_size
        self.ghost_group = pygame.sprite.Group()
        self.enemy_group = pygame.sprite.Group()
        self.exit_group = pygame.sprite.Group()
        self.coin_group = pygame.sprite.Group()
        self.cherry_group = pygame.sprite.Group()
        self.platform_group = pygame.sprite.Group()
        self.monster_group = pygame.sprite.Group()
        self.dragon_group = pygame.sprite.Group()
        self.shield_group = pygame.sprite.Group()
        # self.soldier_group = pygame.sprite.Group()
        # self.bullet_group = pygame.sprite.Group()
        self.level = level
        self.dirt_image = pygame.image.load("./src/assets/images/dirt.png").convert_alpha()
        self.grass_image = pygame.image.load("./src/assets/images/grass.png").convert_alpha()
        self.world_data = Level3()        
        self.width = width
        self.height = height
        
        row_count = 0
        for row in self.world_data.data3:
            col_count = 0
            for tile in row:
                if tile == 1:
                    img = pygame.transform.scale(self.dirt_image, (self.tile_size, self.tile_size))
                    img_rect = img.get_rect()
                    img_rect.x =col_count * self.tile_size
                    img_rect.y =row_count * self.tile_size
                    tile = (img, img_rect)
                    self.tile_list3.append(tile)
                if tile == 2:
                    img = pygame.transform.scale(self.grass_image, (self.tile_size, self.tile_size))
                    img_rect = img.get_rect()
                    img_rect.x =col_count * self.tile_size
                    img_rect.y =row_count * self.tile_size
                    tile = (img, img_rect)
                    self.tile_list3.append(tile)
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
                if tile == 10:
                    shield = Shield1(col_count * self.tile_size, row_count * self.tile_size - (self.tile_size // 2), self.tile_size)
                    self.shield_group.add(shield)                
                col_count += 1
            row_count += 1

    def spawn_monster(self):
        self.new_monster = Monster(self.width, self.height - 80)
        self.monster_group.add(self.new_monster)

    def spawn_dragon(self):
        self.new_dragon = Dragon(self.width, self.height)
        self.dragon_group.add(self.new_dragon)    

    # def spawn_soldier(self):
    #     self.new_soldier = Soldier(self.width, self.height - 80)
    #     self.soldier_group.add(self.new_soldier)

   
    def draw(self, screen):
        for tile in self.tile_list3:
            screen.blit(tile[0], tile[1]) 

        self.ghost_group.draw(screen)
        self.platform_group.draw(screen)
        self.exit_group.draw(screen)
        self.coin_group.draw(screen)
        self.cherry_group.draw(screen)
        self.monster_group.draw(screen)
        self.dragon_group.draw(screen)
        self.shield_group.draw(screen)
        # self.soldier_group.draw(screen)
        # self.bullet_group.draw(screen)
                
    def update_ghosts(self):
        self.ghost_group.update()

    def update_platforms(self):
        self.platform_group.update()

    # def update_soldiers(self):
    #     self.soldier_spawn_rate = 300  # Define la tasa de aparición de los soldados (puede ajustarse)
    #     if random.randint(1, self.soldier_spawn_rate) == 1:
    #         self.spawn_soldier()

    #     for soldier in self.soldier_group:
    #         soldier.update()  # Actualiza la posición y animación del soldado 

    #         if not soldier.has_shot:
    #             bullet = Bullet(soldier.rect.centerx, soldier.rect.centery, soldier.direction, soldier.width)
    #             self.bullet_group.add(bullet)
    #             soldier.has_shot = True

    #     self.bullet_group.update()

    def update_monsters(self):
        self.monster_spawn_rate = 200  
        if random.randint(1, self.monster_spawn_rate) == 1:
            self.spawn_monster()

        for monster in self.monster_group:
            monster.update() 

    def update_dragons(self):
        self.dragon_spawn_rate = 200
        if random.randint(1, self.monster_spawn_rate) == 1:
            self.spawn_dragon()
        
        for dragon in self.dragon_group:
            dragon.update()

    # def update_fin(self):
    #     self.update_monsters()

    # def update_drag(self):
    #     self.update_dragons()

    def update_shield(self):
        player_shield_collision = pygame.sprite.spritecollideany(self.player, self.shield_group)
        if player_shield_collision:
            self.player.shield_active = True

class Level3:
    def __init__(self):
        self.data3 =[
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,10,0,0,0,0],
        [0,0,0,0,0,0,2,2,1,0,0,0,0,0,2,2,2,0,0,0],
        [0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,10,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
        ]

    def get_world_data3(self):
        return self.world_data3


    