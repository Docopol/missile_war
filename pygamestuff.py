import sys

import pygame.time
import pygame as pg
import Planets

pg.init()  # initialise pygame
resolution = (1280, 720)
screen = pg.display.set_mode(resolution)

# setting background
background = pg.image.load("Images/background.jpg")
background = pg.transform.scale(background, resolution)
pg.display.set_caption("Missile war")

# loading images
button1Image = pg.image.load("Images/Buttons/button_play.png")
button2Image = pg.image.load("Images/Buttons/button_options.png")
button3Image = pg.image.load("Images/Buttons/button_quit.png")
mainMenuBackground = pg.image.load("Images/menuBackground.jpg")
mainMenuBackground = pg.transform.scale(mainMenuBackground, resolution)

# basic font
font = pygame.font.SysFont(None, 32)

Click = False


def main_menu():
    while True:
        gameTime = pygame.time.get_ticks() / 1000.
        screen.blit(mainMenuBackground,(0,0))

        mouseX, mouseY = pygame.mouse.get_pos()

        button_1 = pg.Rect(int(0.22 * resolution[0]), int(0.8 * resolution[1]), 200, 50)
        button_2 = pg.Rect(int(0.42 * resolution[0]), int(0.8 * resolution[1]), 200, 50)
        button_3 = pg.Rect(int(0.62 * resolution[0]), int(0.8 * resolution[1]), 200, 50)

        if button_1.collidepoint((mouseX, mouseY)):
            if click:
                game()
        if button_2.collidepoint((mouseX, mouseY)):
            if click:
                options_menu()
        if button_3.collidepoint((mouseX, mouseY)):
            if click:
                pg.quit()
                sys.exit()

        screen.blit(button1Image, button_1)
        screen.blit(button2Image, button_2)
        screen.blit(button3Image, button_3)

        click = False
        for event in pygame.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        Text = str(gameTime)
        timeText = font.render(Text, True, (0, 0, 200))
        screen.blit(timeText, (1400, 20))

        pg.display.flip()

        # calculating number of fps
        endLoopTime = pygame.time.get_ticks() / 1000.
        looptime = endLoopTime - gameTime
        # print(looptime)
        print("fps:", 1 / (looptime+0.000001))


def game():
    GameStartTime = pygame.time.get_ticks() / 1000.
    running = True
    while running:

        gameTime = pygame.time.get_ticks() / 1000.

        for event in pygame.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    running = False

        screen.blit(background, (0, 0))
        screen.blit(Planets.Planets.planet1Visual(self=0), (400, 400))
        screen.blit(Planets.Planets.planet2Visual(self=0), (200, 200))

        Text = str(gameTime)
        timeText = font.render(Text, True, (0, 0, 200))
        screen.blit(timeText, (1400, 20))

        pg.display.flip()  # displaying on the screen

        # calculating number of fps
        endLoopTime = pygame.time.get_ticks() / 1000.
        looptime = endLoopTime - gameTime
        # print(looptime)
        print("fps:", 1 / (looptime+0.000001))


def options_menu():
    GameStartTime = pygame.time.get_ticks() / 1000.
    running = True
    while running:

        gameTime = pygame.time.get_ticks() / 1000.

        for event in pygame.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    running = False

        screen.fill((3, 200, 70))

        Text = str(gameTime)
        timeText = font.render(Text, True, (0, 0, 200))
        screen.blit(timeText, (1400, 20))

        pg.display.flip()  # displaying on the screen

        # calculating number of fps
        endLoopTime = pygame.time.get_ticks() / 1000.
        looptime = endLoopTime - gameTime
        # print(looptime)
        print("fps:", 1 / (looptime+0.000001))


main_menu()
