import pygame
# https://habr.com/ru/articles/858050/
# https://is42-2018.susu.ru/blog/2019/04/29/pygame-shpargalka-dlya-ispolzovaniya/
# сайт цветов www.w3schools.com
pygame.init()
size=(400,200)
pygame.display.set_mode(size)
pygame.display.set_caption("window")

run = True
while run:
    # 1-й Раздел ----- Обработка событий -----------
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    # -----------------------------------------------

    # 2-й Раздел ----- Логика игры ------------------
    #
    # -----------------------------------------------

    # 3-й Раздел -----  Отображение графики ---------
    # Очищаем экран
    # Рисуем все объекты на экране
    # Обновление экрана
    # -----------------------------------------------

pygame.quit()
