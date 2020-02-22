import pygame
import random
import os

pygame.init()


clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 55)
width = 620
height = 500
gamewindow = pygame.display.set_mode((width, height))
pygame.display.set_caption("Believer")
pygame.display.update()

def text_screen(text, color, x, y):
    screen = font.render(text, True, color)
    gamewindow.blit(screen, [x, y])

def plot_snake(gamewindow, color, snake_list, snake_size):
    for i, j in snake_list:
        pygame.draw.rect(gamewindow, color, [i, j, snake_size, snake_size])

def welcome():
    exitgame = False
    while not exitgame:
        gamewindow.fill((255, 255, 255))
        text_screen("Welcome Chote", (0, 0, 0), 160, 180)
        text_screen("Press Enter to Play", (0, 0, 0), 130, 220)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exitgame = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    gameloop()
        pygame.display.update()
        clock.tick(60)

def gameloop():
    snakex = 240
    snakey = 240
    snake_size = 30
    velx = 0
    vely = 0
    vel = 5
    foodx = random.randint(20, width/2)
    foody = random.randint(20, height/2)
    exitgame = False
    gameover = False
    snake_list = []
    snake_len = 1
    score = 0
    fps = 60
    if not os.path.exists(r"C:\Users\vinay\PycharmProjects\SnakeGame\snak.text"):
        with open(r"C:\Users\vinay\PycharmProjects\SnakeGame\snak.text", 'w')as f:
            f.write("0")
    with open(r"C:\Users\vinay\PycharmProjects\SnakeGame\snak.text", 'r')as f:
        hs = f.read()

    while not exitgame:
        if gameover:

            with open(r"C:\Users\vinay\PycharmProjects\SnakeGame\snak.text", 'w')as f2:
                f2.write(str(hs))
            gamewindow.fill((0, 0, 0))
            text_screen("Gameover!", (255, 255, 255), 210, 180)
            text_screen("Chal enter daba firse khelna h toh!", (255, 255, 255), 0, 220)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exitgame = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        welcome()
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exitgame = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velx = vel
                        vely = 0
                    if event.key == pygame.K_LEFT:
                        velx = -vel
                        vely = 0
                    if event.key == pygame.K_UP:
                        vely = -vel
                        velx = 0
                    if event.key == pygame.K_DOWN:
                        vely = vel
                        velx = 0
                    if event.key == pygame.K_q:
                        score += 10

            snakex += velx
            snakey += vely

            if abs(snakex - foodx) < 12 and abs(snakey - foody) < 12:
                score += 10
                foodx = random.randint(20, width / 2)
                foody = random.randint(20, height / 2)
                snake_len += 4
                if score > int(hs):
                    hs = score

            head = []
            head.append(snakex)
            head.append(snakey)
            snake_list.append(head)

            gamewindow.fill((0, 0, 0))
            text_screen(f"Score: {score}" + f"  Highscore: {str(hs)}", (255, 255, 255), 5, 5)

            plot_snake(gamewindow, (0, 255, 255), snake_list, snake_size)
            pygame.draw.rect(gamewindow, (255, 255, 0), [foodx, foody, snake_size, snake_size])

            if len(snake_list) > snake_len:
                del snake_list[0]

            if head in snake_list[:-1]:
                gameover = True

            if snakex < 0 or snakex > width or snakey < 0 or snakey > height:
                gameover = True

        pygame.display.update()
        clock.tick(fps)
    pygame.quit()
    quit()

welcome()