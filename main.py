import pygame
import os
import random

from Bird import Bird
from Cloud import Cloud
from Dino import Dino
from Obstacle import LargeCactus, SmallCactus

pygame.init()

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
RUNNING = [pygame.image.load(os.path.join("resources/dino", "DinoRun1.png")),
           pygame.image.load(os.path.join("resources/dino", "DinoRun2.png"))]
SMALL_CACTUS = [pygame.image.load(os.path.join("resources/cactus", "SmallCactus1.png")),
                pygame.image.load(os.path.join("resources/cactus", "SmallCactus2.png")),
                pygame.image.load(os.path.join("resources/cactus", "SmallCactus3.png"))]
LARGE_CACTUS = [pygame.image.load(os.path.join("resources/cactus", "LargeCactus1.png")),
                pygame.image.load(os.path.join("resources/cactus", "LargeCactus2.png")),
                pygame.image.load(os.path.join("resources/cactus", "LargeCactus3.png"))]
BIRD = [pygame.image.load(os.path.join("resources/bird", "Bird1.png")),
        pygame.image.load(os.path.join("resources/bird", "Bird2.png"))]
BG = pygame.image.load(os.path.join("resources/other", "Track.png"))


def main(agent):
    global game_speed, x_pos_bg, y_pos_bg, points, obstacles
    run = True
    clock = pygame.time.Clock()
    dino = Dino()
    cloud = Cloud()
    game_speed = 20
    x_pos_bg = 0
    y_pos_bg = 380
    points = 0
    font = pygame.font.Font('freesansbold.ttf', 20)
    obstacles = []
    death_count = 0

    def score():
        global points, game_speed
        points += 1
        if points % 100 == 0:
            game_speed += 1

        text = font.render("Pontuação: " + str(points), True, (0, 0, 0))
        text_rect = text.get_rect()
        text_rect.center = (1000, 40)
        SCREEN.blit(text, text_rect)

        if agent == 1:
            player_text = "IA Jogando - Agente Reativo Simples"
        elif agent == 2:
            player_text = "IA Jogando - Agente Baseado em Modelo"
        else:
            player_text = "Joador Manual"

        text_ia = font.render(player_text, True, (0, 0, 0))
        text_rect_ia = text_ia.get_rect()
        text_rect_ia.center = (550, 40)
        SCREEN.blit(text_ia, text_rect_ia)

    def background():
        global x_pos_bg, y_pos_bg
        image_width = BG.get_width()
        SCREEN.blit(BG, (x_pos_bg, y_pos_bg))
        SCREEN.blit(BG, (image_width + x_pos_bg, y_pos_bg))
        if x_pos_bg <= -image_width:
            SCREEN.blit(BG, (image_width + x_pos_bg, y_pos_bg))
            x_pos_bg = 0
        x_pos_bg -= game_speed

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        SCREEN.fill((255, 255, 255))
        user_input = pygame.key.get_pressed()

        dino.draw(SCREEN)
        dino.update(user_input, obstacles, agent)

        if len(obstacles) == 0:
            if random.randint(0, 2) == 0:
                obstacles.append(SmallCactus(SMALL_CACTUS))
            elif random.randint(0, 2) == 1:
                obstacles.append(LargeCactus(LARGE_CACTUS))
            elif random.randint(0, 2) == 2:
                obstacles.append(Bird(BIRD))

        for obstacle in obstacles:
            obstacle.draw(SCREEN)
            obstacle.update(game_speed, obstacles)
            if dino.dino_rect.colliderect(obstacle.rect):
                pygame.time.delay(2000)
                death_count += 1
                menu(death_count, agent)

        background()

        cloud.draw(SCREEN)
        cloud.update(game_speed)

        score()

        clock.tick(30)
        pygame.display.update()


def menu(death_count, agent):
    global points
    run = True

    while run:
        SCREEN.fill((255, 255, 255))
        font = pygame.font.Font('freesansbold.ttf', 30)

        if death_count > 0:
            if agent == 1:
                player_name = "Pontuação do Agente Reativo Simples: "
            elif agent == 2:
                player_name = "Pontuação do Agente Baseado em Modelo: "
            else:
                player_name = "Sua pontuação: "

            score = font.render(player_name + str(points), True, (0, 0, 0))
            score_rect = score.get_rect()
            score_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50)
            SCREEN.blit(score, score_rect)

        text = font.render("Selecione um agente para iniciar", True, (0, 0, 0))
        text_rect = text.get_rect()
        text_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        SCREEN.blit(text, text_rect)
        SCREEN.blit(RUNNING[0], (SCREEN_WIDTH // 2 - 20, SCREEN_HEIGHT // 2 - 140))

        manual_text = font.render("Selecionar Jogo Manual", True, (0, 0, 0))
        manual_rect = manual_text.get_rect()
        manual_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 100)
        SCREEN.blit(manual_text, manual_rect)

        ia1_text = font.render("Selecionar IA: Agente Reativo Simples", True, (0, 0, 0))
        ia1_rect = ia1_text.get_rect()
        ia1_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 150)
        SCREEN.blit(ia1_text, ia1_rect)

        ia2_text = font.render("Selecionar IA: Agente Baseado em Modelo", True, (0, 0, 0))
        ia2_rect = ia2_text.get_rect()
        ia2_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 200)
        SCREEN.blit(ia2_text, ia2_rect)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
            if event.type == pygame.KEYDOWN:
                main()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if manual_rect.collidepoint(mouse_pos):
                    agent = 0
                    main(agent)
                if ia1_rect.collidepoint(mouse_pos):
                    agent = 1
                    main(agent)
                elif ia2_rect.collidepoint(mouse_pos):
                    agent = 2
                    main(agent)


menu(0, 0)
