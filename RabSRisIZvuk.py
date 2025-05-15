import pygame as pg

pg.init()
pg.mixer.init()

size=(500,500)
screen=pg.display.set_mode(size)
pg.display.set_caption("window")

fps=15
clock=pg.time.Clock()

background=pg.image.load('background.png')
background=pg.transform.scale(background,size)

character=pg.image.load('Character.png')
character=pg.transform.scale(character,(150,238))
character_rect=character.get_rect(center=(size[0]//2,size[1]//2))

character2=pg.transform.flip(character,True,False)

pg.mixer.music.load('musik.mp3')
pg.mixer.music.set_volume(0.1)

pg.mixer.music.play()
#pg.mixer.music.pause()

hello_sound=pg.mixer.Sound('Zvuk.mp3')
hello_sound.play()

small_rect=pg.Rect(0,0,20,20)

runGame = True
while runGame:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            runGame = False
#нажатие на мышь 0 - левая кнопка мыши, 1 - колесико, 2 - правая кнопка мыши
#Событие типа pg.MOUSEBUTTONDOWN находит все клавиши мыши, нажатые в данный момент.
        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:
                small_rect.center=event.pos
#pg.KEYDOWN находит только появившиеся в данный момент.
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT:
              character_rect.x -= 10
            if event.key == pg.K_RIGHT:
              character_rect.x += 10
        #     if event.key == pg.K_SPACE:
        #         hello_sound.play()
#Функция pg.key.get_pressed() считывает нажатые клавиши каждый кадр,
#все нажатые клавиши
    keys=pg.key.get_pressed()

    if keys[pg.K_LEFT]:
        character_rect.x -= 5
    if keys[pg.K_RIGHT]:
        character_rect.x += 5

#координаты курсора () - кортеж
    mouse_pos=pg.mouse.get_pos()
#нажатые клавиши мыши {} - словарь
    mouse_keys=pg.mouse.get_pressed()
    if mouse_keys[0]:
        character_rect.center=mouse_pos

    screen.blit(background,(0,0))
    screen.blit(character,character_rect)
    screen.blit(character2, (300, 100))

    pg.draw.rect(screen,pg.Color('red'),small_rect)

    pg.display.flip()
    clock.tick(fps)
pg.quit()
