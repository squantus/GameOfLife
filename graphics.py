import pygame as pg
from random import randrange as rnd


def init(display_size=(800, 600)):
    pg.init()

    display = pg.display.set_mode(display_size)
    pg.display.set_caption('Game of Life')

    return display


def draw(world, display, block_size):
    field = world.get_field_log()

    for i in range(len(field)):
        for j in range(len(field[i])):
            if field[i][j] == '.':
                color = (rnd(130, 180), 255, 255)
            elif field[i][j] == '#':
                color = (160, 160, 160)
            elif field[i][j] == 'F':
                color = (102, 255, 178)
            elif field[i][j] == 'S':
                color = (255, 204, 255)
            else:
                color = (0, 0, 0)

            pg.draw.rect(display, color,
                         pg.Rect(j * block_size, i * block_size, block_size,
                                 block_size))


def loop(world, display, block_size):
    clock = pg.time.Clock()
    fps = 10
    end = False

    while not end:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                end = True

        if not world.update():
            end = True

        display.fill((0, 0, 0))
        draw(world, display, block_size)
        pg.display.update()

        clock.tick(fps)
