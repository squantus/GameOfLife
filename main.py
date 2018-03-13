import model
import pygame as pg

pg.init()

display_size = (800, 600)
display = pg.display.set_mode(display_size)
pg.display.set_caption('Game of Life')
clock = pg.time.Clock()

world = model.World()

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            quit()

    pg.display.update()
    clock.tick(60)
