import pygame 
from scripts.data_handel import load_data
from data.settings import *

class player(pygame.sprite.Sprite):
	def __init__(self,pos,groups,obstacle_sprites):
		super().__init__(groups)
		self.image = pygame.image.load('assests/sprites/player_ph.png').convert_alpha()
		self.rect = self.image.get_rect(topleft = pos)
		self.hitbox = self.rect.inflate(0,-26)

		self.direction = pygame.math.Vector2()
		self.speed = 4

		self.health = 100
		self.data = load_data()
		self.inventory = self.data["inventory"]

		self.dash_dist = 65
		self.is_dashing = False
		self.dash_cd = 0
		self.dash_steps = 0
		self.dash_step_count = 0  
        
		self.is_god = False

		self.obstacle_sprites = obstacle_sprites

	def input(self):
		keys = pygame.key.get_pressed()

		self.direction = pygame.math.Vector2(0,0)

		if keys[pygame.K_UP] or keys[pygame.K_w]:
			self.direction.y = -1
		if keys[pygame.K_DOWN] or keys[pygame.K_s]:
			self.direction.y = 1
		if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
			self.direction.x = 1
		if keys[pygame.K_LEFT] or keys[pygame.K_a]:
			self.direction.x = -1

		# dash
		self.dash_cd = max(0,(self.dash_cd-1))
		if keys[pygame.K_SPACE] and not self.is_dashing and self.dash_cd == 0:
			self.is_dashing = True
			self.is_god = True
			self.dash_steps = 10  #number of animation steps
			self.dash_step_count = 0
			self.dash_cd = 45 #frames



	def move(self,speed):
		if self.direction.magnitude() != 0:
			self.direction = self.direction.normalize()

		self.hitbox.x += self.direction.x * speed
		self.collision('horizontal')
		self.hitbox.y += self.direction.y * speed
		self.collision('vertical')

		# dash
		if self.is_dashing:
			if self.dash_step_count < self.dash_steps:
				dash = self.direction * (self.dash_dist / self.dash_steps)
				self.hitbox.x += dash.x
				self.collision('horizontal')
				self.hitbox.y += dash.y
				self.collision('vertical')
				self.dash_step_count += 1
			else:
				self.is_dashing = False
				self.is_god = False
				self.dash_step_count = 0

		self.rect.center = self.hitbox.center
		

	def collision(self,direction):
		if direction == 'horizontal':
			for sprite in self.obstacle_sprites:
				if sprite.hitbox.colliderect(self.hitbox):
					if self.direction.x > 0: # moving right
						self.hitbox.right = sprite.hitbox.left
					if self.direction.x < 0: # moving left
						self.hitbox.left = sprite.hitbox.right

		if direction == 'vertical':
			for sprite in self.obstacle_sprites:
				if sprite.hitbox.colliderect(self.hitbox):
					if self.direction.y > 0: # moving down
						self.hitbox.bottom = sprite.hitbox.top
					if self.direction.y < 0: # moving up
						self.hitbox.top = sprite.hitbox.bottom

	def update(self):
		self.input()
		self.move(self.speed)