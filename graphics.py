import pygame as pg


def _init(display_size=(800, 600)):
    pg.init()

    display = pg.display.set_mode(display_size)
    pg.display.set_caption('Game of Life')

    return display


def _draw(file, display_size=(800, 600)):
    return


def _loop(display):
    clock = pg.time.Clock()
    fps = 10
    end = False

    while not end:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                end = True

        pg.display.update()
        clock.tick(fps)
