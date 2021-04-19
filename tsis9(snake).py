from snake import Snake
import pygame 
import time
import random
import pickle

pygame.init()

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
YELLOW = (255,255,102)
GREEN = (0,255,0)

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake game")

snake_block_size = 10
snake_speed = 20

clock = pygame.time.Clock()

font_style = pygame.font.SysFont("VERDANA", 20)
score_font = pygame.font.SysFont("VERDANA", 20)

FILE_NAME = 'snakes_saved.data'

def message(font, msg, color, x, y):
    mesg = font.render(msg, True, color)
    screen.blit(mesg, (x, y))

def game_loop():
    game_over = False
    game_close = False
    choose = False

    snake1 = Snake(snake_block_size, WHITE, [WIDTH // 2, HEIGHT // 2])
    keys = {
        'UP': pygame.K_UP,
        'DOWN': pygame.K_DOWN,
        'RIGHT': pygame.K_RIGHT,
        'LEFT': pygame.K_LEFT
    }
    snake2 = Snake(snake_block_size, GREEN, [WIDTH // 2 + 50, HEIGHT // 2], keys=keys)

    while not choose:
        screen.fill(BLACK)
        message(font_style, "PRESS SPACE TO CONTINUE GAME", RED, WIDTH - 550, HEIGHT // 2)
        message(font_style, "PRESS ANY BUTTON TO START", RED, WIDTH - 550, HEIGHT // 2.5 )
        message(font_style, "WHILE PLAYING PRESS ESCAPE TO SAVE GAME", RED, WIDTH - 550, HEIGHT // 3)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    try:
                        with open(FILE_NAME, 'br') as f:
                            snakes = pickle.load(f) 
                    except Exception as e:
                        print(e)
                        snakes = (snake1, snake2)
                else:
                    snakes = (snake1, snake2)
                choose = True
    
    foodx = round(random.randrange(0, WIDTH - snake_block_size) / 10.0) * 10.0
    foody = round(random.randrange(0, HEIGHT - snake_block_size) / 10.0) * 10.0
    
    while not game_close:
        clock.tick(snake_speed)

        while game_over:
            screen.fill(BLACK)
            if (snake1.get_length() - 1) > (snake2.get_length() - 1):
                message(score_font, "PLAYER 1 WIN WITH SCORE: " + str(snake1.get_length() - 1),WHITE,WIDTH - 550, HEIGHT // 2)
            if (snake2.get_length() - 1) > (snake1.get_length() - 1):
              message(score_font, "PLAYER 2 WIN WITH SCORE: " + str(snake2.get_length() - 1),WHITE ,WIDTH - 550, HEIGHT // 2)
            if (snake2.get_length() - 1) == (snake1.get_length() - 1):
                 message(score_font, "DRAW" ,WHITE ,WIDTH //2, HEIGHT // 2)
            message(score_font, "PRESS 'q' TO CLOSE GAME ",WHITE,WIDTH - 550, HEIGHT // 3)
            message(score_font, "PRESS 'r' TO RESTART GAME ",WHITE,WIDTH - 550, HEIGHT // 3.5)
            
            
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = False
                        game_close = True
                    if event.key == pygame.K_r:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_close = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    with open(FILE_NAME, 'bw') as f:
                        pickle.dump(snakes, f)
                    game_close = True

        for snake in snakes:
            x1, y1 = snake.get_head_coordinates()
            if x1 >= WIDTH or x1 < 0 or y1 >= HEIGHT or y1 < 0:
                game_over = True
            if x1 == foodx and y1 == foody:
                foodx = round(random.randrange(0, WIDTH - snake_block_size) / 10.0) * 10.0
                foody = round(random.randrange(0, HEIGHT - snake_block_size) / 10.0) * 10.0
                snake.add_block()

        pressed_keys = pygame.key.get_pressed()
        for snake in snakes:
            snake.move(pressed_keys)

        screen.fill(BLACK)
        pygame.draw.rect(screen, RED, [foodx, foody, snake_block_size, snake_block_size]) 
        for snake in snakes:
            snake.draw(screen)

        message(score_font, "PLAYER 1: " + str(snake1.get_length() - 1), WHITE, 0, 0)
        message(score_font, "PLAYER 2: " + str(snake2.get_length() - 1), WHITE, 0, 20)
       
       
        
        pygame.display.update()
            
    pygame.quit()
    quit()

if __name__ == '__main__':
    game_loop()