import pygame

SIZE_BLOCK = 20  # Размер блока
FRAME_COLOR = (0, 255, 204)  # Цвет поля
WHITE = (255, 255, 255)  # Цвет блока
BLUE = (204, 255, 255)  # Используется при раскрашивании кубиков через один
size = [500, 600]  # Размер поля
COUNT_BLOCKS = 20  # количество блоков в нашем ряду
MARGIN = 1  # Отступы между кубиками
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Змейка Артема')
while True:


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print('exit, он же выход)')
            pygame.quit()

    screen.fill(FRAME_COLOR)

    for row in range(COUNT_BLOCKS):
        for column in range(COUNT_BLOCKS):
            if (row + column) % 2 == 0:  # Раскрашиваем кубики через один, разным цветом
                color = BLUE
            else:
                color = WHITE
            pygame.draw.rect(screen, color, [10 + column * SIZE_BLOCK + MARGIN * (column + 1),
                                             20 + row * SIZE_BLOCK + MARGIN * (row + 1),
                                             SIZE_BLOCK,
                                             SIZE_BLOCK])

    pygame.display.flip()
