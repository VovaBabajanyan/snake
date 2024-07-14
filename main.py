"""Игра Змейка"""
import random
import pygame


pygame.init()

yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)
snake_color = black
background_color = blue
food_color = green

dis_width = 800
dis_height = 600
dis=pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption("Змейка")
clock = pygame.time.Clock()
snake_block = 10
snake_speed = 15

font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)


def your_score(score):
    value = score_font.render("Ваш счет: " + str(score), True, yellow)
    dis.blit(value, [0, 0])


def our_snake(block, snake_list):
    """Отрисовка змейки"""
    for x in snake_list:
        pygame.draw.rect(dis, snake_color, [x[0], x[1], block, block])

def message(msg, color):
    """ Вывод сообщения на экран """
    text_surface = font_style.render(msg, True, color)
    dis.blit(text_surface,
             [
                 dis_width/2 - text_surface.get_width()/2,
                 dis_height/2 - text_surface.get_height()/2
             ]
             )


def game_loop():
    """Основной цикл игры"""
    game_over = False
    game_close = False
    x1 = dis_width / 2
    y1 = dis_height / 2
    x1_change = 0
    y1_change = 0
    snake_list = []
    length_of_snake = 1
    food_x = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    food_y = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    while not game_over:
        while game_close:
            dis.fill(background_color)
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
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(background_color)

        pygame.draw.rect(
            dis, food_color, [food_x, food_y, snake_block, snake_block])
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
                0, dis_width - snake_block) / 10.0) * 10.0
            food_y = round(random.randrange(
                0, dis_height - snake_block) / 10.0) * 10.0
            length_of_snake += 1

        clock.tick(snake_speed)
    pygame.quit()
    quit()


game_loop()
