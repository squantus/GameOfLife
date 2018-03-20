import pygame as pg


def init(display_size=(800, 600)):
    pg.init()

    display = pg.display.set_mode(display_size)
    pg.display.set_caption('Game of Life')

    return display


def draw(world, display_size=(800, 600)):
    return


def loop(world, display, display_size=(800, 600)):
    clock = pg.time.Clock()
    fps = 10
    end = False

    while not end:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                end = True

        if not world.update():
            end = False

        draw(world, display_size)
        pg.display.update()
        clock.tick(fps)
