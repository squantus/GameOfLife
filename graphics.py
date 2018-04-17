import pygame as pg
from random import randrange as rnd

CELL_COLORS = {'.': lambda: (rnd(130, 180), 255, 255),
               '#': lambda: (160, 160, 160),
               'F': lambda: (102, 255, 178),
               'S': lambda: (255, 204, 255)}
BLACK = (0, 0, 0)
FPS = 10


def init(display_size):
    pg.init()

    display = pg.display.set_mode(display_size)
    pg.display.set_caption('Game of Life')

    return display


def draw(world, display, block_size):
    field_log = world.get_field_log()

    bad_launch = False

    for i in range(len(field_log)):
        for j in range(len(field_log[i])):
            log_name = field_log[i][j]
            color = BLACK

            try:
                color = CELL_COLORS[log_name]()
            except KeyError:
                print('Wrong cell at {} {}: {}'.format(i, j, log_name))
                bad_launch = True

            pg.draw.rect(display, color,
                         pg.Rect(j * block_size, i * block_size,
                                 block_size,
                                 block_size))

    if bad_launch:
        quit()


def loop(world, display, block_size):
    clock = pg.time.Clock()
    end = False

    while not end:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                end = True

        if not world.update():
            end = True

        display.fill(BLACK)
        draw(world, display, block_size)
        pg.display.update()

        clock.tick(FPS)
