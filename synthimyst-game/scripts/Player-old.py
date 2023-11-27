
import pygame
from scripts.data_handel import load_data as load
# from scripts.Items import item 

data = load()

class player(pygame.sprite.Sprite):
    def __init__(self, pos, groups,obstacle_sprites):
        super().__init__(groups)
        self.image = pygame.image.load("assests/sprites/player_ph.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = (pos)
        self.hitbox  = self.rect.inflate(0, -8)

        self.obstacle_sprites = obstacle_sprites


        self.health = 100
        self.data = data
        self.inventory = self.data["inventory"]
        
        self.direction = pygame.math.Vector2()
        self.speed = 2

        self.dash_dist = 30
        self.is_dashing = False
        self.dash_cd = 0
        self.dash_steps = 0
        self.dash_step_count = 0  
        
        self.is_god = False

    def input(self):
        # util
        keys = pygame.key.get_pressed()
        # movement
        # if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        #     self.direction.x = 1
        # if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        #     self.direction.x = -1
        # if keys[pygame.K_w] or keys[pygame.K_UP]:
        #     self.direction.y = -1
        # if keys[pygame.K_s] or keys[pygame.K_DOWN]:
        #     self.direction.y = 1

        # test
        if keys[pygame.K_UP]:
            self.direction.y = -1
        elif keys[pygame.K_DOWN]:
            self.direction.y = 1
        else:
            self.direction.y = 0
        
        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
        else:
            self.direction.x = 0

        # dash
        # self.dash_cd = max(0,(self.dash_cd-1))
        # if keys[pygame.K_SPACE] and not self.is_dashing and self.dash_cd == 0:
        #     self.is_dashing = True
        #     self.is_god = True
        #     self.dash_steps = 10  #number of animation steps
        #     self.dash_step_count = 0
        #     self.dash_cd = 45 #frames

    def movement(self, speed):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()

        self.hitbox.x += self.direction.x * speed
        self.hitbox.y += self.direction.y * speed

        # dash
        # if self.is_dashing:
        #     if self.dash_step_count < self.dash_steps:
        #         dash = self.direction * (self.dash_dist / self.dash_steps)
        #         self.hitbox.move_ip(dash)
        #         self.dash_step_count += 1
        #     else:
        #         self.is_dashing = False
        #         self.is_god = False
        #         self.dash_step_count = 0
        self.rect.center = self.hitbox.center
        
        self.collision()

    def collision(self):
        for sprite in self.obstacle_sprites:
            if sprite.hitbox.colliderect(self.hitbox):
                if self.direction.magnitude() != 0:
                    if self.direction.x > 0: # moving right
                        self.hitbox.right = sprite.hitbox.left
                    if self.direction.x < 0: # moving left
                        self.hitbox.left = sprite.hitbox.right
                    if self.direction.y > 0: # moving down
                        self.hitbox.bottom = sprite.hitbox.top
                    if self.direction.y < 0: # moving up
                        self.hitbox.top = sprite.hitbox.bottom
                    # diagonal movement collision
                    # else:
                    #     direction = self.direction*-1
                    #     while sprite.hitbox.colliderect(self.hitbox):
                    #         self.hitbox.move_ip(direction)


        
    def update(self):
        self.input()
        self.movement(self.speed)

    # def useItem(self, index_value):
    #     Item_type = self.inventory["hotbar"][index_value]
    #     Item = item(self.rect.centerx, self.rect.centery , Item_type)
    #     Item.use()
