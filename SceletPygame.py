import pygame as pg

pg.init()
size = (500, 500)
screen = pg.display.set_mode(size)
pg.display.set_caption("window")

fps = 15

clock = pg.time.Clock()

runGame = True
while runGame:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            runGame = False

    screen.fill(pg.Color(255, 129, 158))

    pg.display.flip()
    clock.tick(fps)
pg.quit()
