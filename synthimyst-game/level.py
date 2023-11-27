import pygame 
from data.settings import *
from scripts.tile import Tile
from scripts.Player import player
from scripts.tmx_handel import usetmx

class Level:
	def __init__(self, surf):

		# get the display surface 
		# self.display_surface = pygame.display.get_surface()
		self.display_surface = surf
		# sprite group setup
		self.visible_sprites = CameraGroup(surf)
		self.obstacle_sprites = pygame.sprite.Group()

		# sprite setup
		self.create_map()

	def create_map(self):
		# for row_index,row in enumerate(WORLD_MAP):
		# 	for col_index, col in enumerate(row):
		# 		x = col_index * TILESIZE
		# 		y = row_index * TILESIZE
		# 		if col == 'x':
		# 			Tile((x,y),[self.visible_sprites,self.obstacle_sprites])
		# 		if col == 'p':
		# 			self.player = player((x,y),[self.visible_sprites],self.obstacle_sprites)
		self.player = player((1400,2000),[self.visible_sprites],self.obstacle_sprites)
		usetmx("data/map.tmx", self.obstacle_sprites, self.visible_sprites)

	def run(self):
		# update and draw the game
		self.visible_sprites.custom_draw(self.player)
		self.visible_sprites.update()


class CameraGroup(pygame.sprite.Group):
	def __init__(self, surf):

		# general setup 
		super().__init__()
		# self.display_surface = pygame.display.get_surface()
		self.display_surface = surf
		self.half_width = self.display_surface.get_size()[0] // 2
		self.half_height = self.display_surface.get_size()[1] // 2
		self.offset = pygame.math.Vector2()

		self.ground = pygame.image.load("assests/sprites/Texture/ground.png").convert_alpha()
		self.groundrect = self.ground.get_rect(topleft = (0,0))

	def custom_draw(self,player):

		# getting the offset 
		self.offset.x = player.rect.centerx - self.half_width
		self.offset.y = player.rect.centery - self.half_height

		# floor 
		floor_offset = self.groundrect.topleft - self.offset
		self.display_surface.blit(self.ground, floor_offset)

		# for sprite in self.sprites():
		for sprite in sorted(self.sprites(),key = lambda sprite: sprite.rect.centery):
			offset_pos = sprite.rect.topleft - self.offset
			self.display_surface.blit(sprite.image,offset_pos)
