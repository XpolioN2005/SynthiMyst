import pygame 
from data.settings import *

class Tile(pygame.sprite.Sprite):
	def __init__(self,pos,groups, surf = pygame.Surface((TILESIZE,TILESIZE))):
		super().__init__(groups)
		self.image = surf.convert_alpha()
		self.rect = self.image.get_rect(bottomleft = pos)
		self.hitbox = self.rect.inflate(0,-10)