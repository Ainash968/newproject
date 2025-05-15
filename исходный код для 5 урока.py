import pygame as pg

pg.mixer.init()

size = (500, 500)
screen = pg.display.set_mode(size)

fps = 100
clock = pg.time.Clock()

character = pg.image.load("character.png")
character = pg.transform.scale(character, (200, 400))
character_rect = character.get_rect(center=(size[0] // 2, size[1] // 2))

background = pg.image.load("background.png")
background = pg.transform.scale(background, size)
pg.mixer.music.load("music.mp3")
pg.mixer.music.set_volume(0.1)

# pg.mixer.music.play()

while True:

    screen.blit(background, (0, 0))

    screen.blit(character, character_rect)


    pg.display.flip()
    clock.tick(fps)
