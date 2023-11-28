from sys import exit
from data.settings import *
from level import Level

import pygame

from debug import debug
# scripts 
from scripts.data_handel import save_data
#init
pygame.init()

#primary var
clock = pygame.time.Clock()
pygame.display.set_caption("SynthiMyst: prototype")
WIDTH = 640
HEIGTH = 480
screen = pygame.display.set_mode((WIDTH,HEIGTH))
running = True

pygame.mouse.set_visible(False)
level = Level(screen)

# gameloop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:

            save_data(level.player.data)
            pygame.quit()
            exit()
    screen.fill((14, 135, 158))
    level.run()
    debug(f"FPS: {int(clock.get_fps())}",screen)
    screen.blit((pygame.transform.scale(screen, screen.get_size())), (0,0))
    pygame.display.flip()
    clock.tick(FPS)
