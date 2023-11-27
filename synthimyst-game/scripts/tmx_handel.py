from pytmx.util_pygame import load_pygame
from data.settings import TILESIZE
from scripts.tile import Tile

def usetmx(path, collision_group, visible_group):
    tmx = load_pygame(path)
    for layer in tmx.layers:
        if layer.name == "collisionBound":
            for posX, posY, surf in layer.tiles():
                posX = (posX*TILESIZE)
                posY = (posY*TILESIZE) +32
                Tile((posX,posY), [collision_group])
        if not (layer.name in ["ground","collisionBound"]):
            for posX, posY, surf in layer.tiles():
                posX = (posX*TILESIZE)
                posY = (posY*TILESIZE) +32
                Tile((posX,posY), [visible_group, collision_group], surf)