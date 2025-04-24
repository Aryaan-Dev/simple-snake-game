import pygame
import random
import os

pygame.mixer.init()
pygame.init()

white = (250, 250, 250)
red = (250 ,0 , 0)
black = (0, 0, 0)

screen_width = 900
screen_height = 670
gameWindow = pygame.display.set_mode((screen_width,screen_height))

gameWindow = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("SNAKE WITH ARYAAN")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 55)

def score_text(text, color, x, y):
    score_text = font.render(text, True, color)
    gameWindow.blit(score_text, (x, y))

def plot_snake(gameWindow, color, snk_list, snake_size):
    for x, y in snk_list:
         pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])

def welcome():
    pygame.mixer.music.load('start.mp3')
    pygame.mixer.music.play()

    exit_game = False
    while not exit_game:
        gameWindow.fill(white)
        score_text("WELCOME TO THE SNAKE GAME", red , 128 , 180)
        score_text("PRESS SPACE TO CONTINUE", red , 170 , 280)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                        pygame.mixer.music.stop()
                        pygame.mixer.music.load('background.mp3')
                        pygame.mixer.music.play(-1)
                        gameloop()

        pygame.display.update()
        clock.tick(45)

def gameloop():
    
    gameover_sound = pygame.mixer.Sound('gameover.mp3')

    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 55
    velocity_x = 0
    velocity_y = 0
    snk_list = []
    snk_length = 1


    if not os.path.exists("highscore.txt"):
        with open("highscore.txt","w") as f:
            f.write("0")

    with open("highscore.txt", "r") as f:
        highscore = f.read()

    food_x = random.randint(20,screen_width - 20 )
    food_y = random.randint(20,screen_height - 20 )
    score = 0
    init_velocity = 4
    food_size = 8
    snake_size = 13
    fps = 30

    while not exit_game:
        if game_over:
            pygame.mixer.music.stop()
            gameover_sound.play()

            with open("highscore.txt", "w") as f:
                f.write(str(highscore))

            gameWindow.fill(black)
            score_text("GAME OVER ! PRESS ENTER TO REPLAY ", red, 65, 300)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        pygame.mixer.music.stop()
                        welcome()

        else:    
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_LEFT:
                        velocity_x = - init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_UP:
                        velocity_y = - init_velocity
                        velocity_x = 0

                    if event.key == pygame.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x = 0

            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y


            if abs(snake_x - food_x) < 7 and abs(snake_y - food_y) < 7:
                score += 10
                food_x = random.randint (0, screen_width // 2)
                food_y = random.randint(0, screen_height // 2)
                snk_length += 4
                if score > int (highscore):
                    highscore = score

            gameWindow.fill(white)
            score_text (f"SCORE : {score} HIGHSCORE: {highscore}", red, 5, 5)
            pygame.draw.rect(gameWindow, red, [food_x, food_y, food_size, food_size])

            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list) > snk_length:
                del snk_list[0]

            if head in snk_list[:-1]:
                game_over = True

            if snake_x < 0 or snake_x > screen_width or snake_y < 0 or snake_y > screen_height:
                game_over = True

            plot_snake(gameWindow, black, snk_list, snake_size)
            pygame.display.update()
            clock.tick(fps)
    
    pygame.quit()
    quit()

welcome()