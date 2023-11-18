import pygame
import time
import random

pygame.init()

display_width = 600
display_height = 600

game_display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Snake Game')

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (22, 100, 8)

snake_block_size = 10
snake_speed = 20

def snake(snake_block_size, snake_list):
    for x in snake_list:
        pygame.draw.rect(game_display, green, [x[0], x[1], snake_block_size, snake_block_size])

def game():
    game_over = False
    game_exit = False

    snake_x = display_width / 2
    snake_y = display_height / 5
    snake_x_change = snake_block_size
    snake_y_change = 0

    snake_list = []
    snake_length = 5

    food_x = round(random.randrange(0, display_width - snake_block_size) / 10.0) * 10.0
    food_y = round(random.randrange(0, display_height - snake_block_size) / 10.0) * 10.0

    clock = pygame.time.Clock()

    while not game_exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    snake_x_change = -snake_block_size
                    snake_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    snake_x_change = snake_block_size
                    snake_y_change = 0
                elif event.key == pygame.K_UP:
                    snake_y_change = -snake_block_size
                    snake_x_change = 0
                elif event.key == pygame.K_DOWN:
                    snake_y_change = snake_block_size
                    snake_x_change = 0

        snake_x += snake_x_change
        snake_y += snake_y_change

        if snake_x >= display_width or snake_x < 0 or snake_y >= display_height or snake_y < 0:
            game_over = True

        if game_over:
            game_display.fill(black)
            pygame.draw.rect(game_display, red, [display_width/4, display_height/3, display_width/2, display_height/3])
            
            font = pygame.font.Font(None, 50)
            text = font.render("Game Over", True, white)
            game_display.blit(text, (display_width/2 - text.get_width()/2, display_height/2 - text.get_height()/2))

            pygame.display.update()
            time.sleep(2)  # Pause for 2 seconds before quitting the game
            game_exit = True

        game_display.fill(black)
        pygame.draw.rect(game_display, red, [food_x, food_y, snake_block_size, snake_block_size])

        snake_head = [snake_x, snake_y]
        snake_list.append(snake_head)

        if len(snake_list) > snake_length:
            del snake_list[0]

        for segment in snake_list[:-1]:
            if segment == snake_head:
                game_over = True

        snake(snake_block_size, snake_list)

        if snake_x == food_x and snake_y == food_y:
            food_x = round(random.randrange(0, display_width - snake_block_size) / 10.0) * 10.0
            food_y = round(random.randrange(0, display_height - snake_block_size) / 10.0) * 10.0
            snake_length += 1

        pygame.display.update()
        clock.tick(snake_speed)

    pygame.quit()
    quit()
    

game()
