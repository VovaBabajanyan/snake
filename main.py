"""Игра Змейка"""
import random  # добавляем библиотеку random
import pygame  # добавляем библиотеку pygame


pygame.init()  # Инициализация библиотеки pygame

# Задаем цвета
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Указываем цвета объектов
snake_color = black      # Цвет змейки
background_color = blue  # Цвет фона
food_color = green       # Цвет еды
score_color = yellow     # Цвет счета

display_width = 1200   # Ширина игрового поля
display_height = 1000  # Высота игрового поля

snake_block = 20  # Размер блока змейки и еды

font_style = pygame.font.SysFont("bahnschrift", 25)  # Основой шрифт игры
score_font = pygame.font.SysFont("comicsansms", 35)  # Шрифт для счета


# display = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

display = pygame.display.set_mode(
    (display_width, display_height))  # Уставка размера окна
pygame.display.set_caption("Змейка")  # Задается название окна
clock = pygame.time.Clock()  # Инициализация переменной clock

def your_score(score):
    """Вывод результата игры"""
    value = score_font.render("Ваш счет: " + str(score), True, score_color)
    display.blit(value, [0, 0])


def our_snake(block, snake_list):
    """Отрисовка змейки"""
    for k, x in enumerate(snake_list):
        pygame.draw.rect(display, snake_color,
                         [x[0], x[1], block, block])

def message(msg, color):
    """ Вывод сообщения на экран """
    text_surface = font_style.render(msg, True, color)
    display.blit(text_surface,
             [
                 display.get_width()/2 - text_surface.get_width()/2,
                 display.get_height()/2 - text_surface.get_height()/2
             ]
             )


def game_loop():
    """Основной цикл игры"""
    snake_speed = 10  # Скорость змейки
    game_over = False
    game_close = False
    x1 = display.get_width() / 2
    y1 = display.get_height() / 2
    x1_change = 0
    y1_change = 0
    snake_list = []
    length_of_snake = 1
    food_x = round(random.randrange(
        0, display.get_width() - snake_block) / snake_block) * snake_block
    food_y = round(random.randrange(
        0, display.get_height() - snake_block) / snake_block) * snake_block

    while not game_over:
        while game_close:
            display.fill(background_color)
            message("Вы проиграли! Нажмите Q для выхода или C для повторной игры", red)
            your_score(length_of_snake - 1)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                if event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                if event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                if event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0
        if x1 >= display.get_width() or x1 < 0 or y1 >= display.get_height() or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        display.fill(background_color)

        pygame.draw.rect(
            display, food_color, [food_x, food_y, snake_block, snake_block])
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for i in snake_list[:-1]:
            if i == snake_head:
                game_close = True

        our_snake(snake_block, snake_list)
        your_score(length_of_snake - 1)
        pygame.display.update()

        if x1 == food_x and y1 == food_y:
            food_x = round(random.randrange(
                0, display.get_width() - snake_block) / snake_block) * snake_block
            food_y = round(random.randrange(
                0, display.get_height() - snake_block) / snake_block) * snake_block
            length_of_snake += 1
            if length_of_snake % 5 == 0:
                snake_speed += 1

        clock.tick(snake_speed)
    pygame.quit()
    quit()


game_loop()
