import classes as cls
import pygame
def load_level(file_path):
    with open(file_path, "r") as file:
        level_data = file.readlines()
    return level_data

def render_level(level_data, win, walls = []):
    tile_size = 36
    for y, row in enumerate(level_data):
        for x, tile in enumerate(row.strip()):
            if tile == "#":
                wall = cls.Wall(win, (x * tile_size, y * tile_size))
                walls.append(wall)
    return  walls

def render_objects(level_data, win, objs = []):
    tile_size = 36
    for y, row in enumerate(level_data):
        for x, tile in enumerate(row.strip()):
            if tile == "c" or tile == 'C':
                coin = cls.Coin(win, (x * tile_size, y * tile_size))
                objs.append(coin)
            elif tile == "H" or tile == 'h':
                heart = cls.Life_Heart(win, (x * tile_size, y * tile_size))
                objs.append(heart)
            elif tile == "K" or tile == 'k':
                key = cls.Key(win, (x * tile_size, y * tile_size))
                objs.append(key)
            elif tile == "b" or tile == 'B':
                box = cls.Chest(win, (x * tile_size, y * tile_size))
                objs.append(box)

    return  objs
def render_enemies(level_data , win , enemy = []):
    tile_size = 36
    for y, row in enumerate(level_data):
        for x, tile in enumerate(row.strip()):
            if tile == "e" or tile == 'E':
                e = cls.Enemy(win, (x * tile_size, y * tile_size))
                enemy.append(e)

    return enemy

def render_Hero(level_data, win,):
    tile_size = 36
    for y, row in enumerate(level_data):
        for x, tile in enumerate(row.strip()):
            if tile == "A" or tile == 'a':
                Hero = cls.Hero(win, (x * tile_size, y * tile_size))
                return  Hero