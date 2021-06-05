import sys

import numpy as np
import pygame.time
import pygame as pg

from functionsGame import *
from environment import Environment
from missile import Missile

pg.init()  # initialise pygame
resolution = (1280, 720)
screen = pg.display.set_mode(resolution)
pg.mouse.set_cursor(pg.cursors.diamond)

# background music
pg.mixer.init()
thing = backGroundMusic = pygame.mixer.music.load("Star-Wars-Main-Theme-_Full_.ogg")
pygame.mixer.music.play(-1, 0.0)
volume = 0.3
pg.mixer.music.set_volume(volume)

# setting background
pg.display.set_caption("Missile war")

# loading images
button1Image = pg.image.load("Images/Buttons/button_play.png")
button2Image = pg.image.load("Images/Buttons/button_options.png")
button3Image = pg.image.load("Images/Buttons/button_quit.png")
mainMenuBackground = pg.image.load("Images/menuBackground.jpg")
mainMenuBackground = pg.transform.scale(mainMenuBackground, resolution)
target = pg.image.load("Images/target.png")
target = pg.transform.scale(target, (int(0.05 * resolution[0]), int(0.035 * resolution[0])))
mainMenuText = pg.image.load("Images/Missile War.png")
backbuttonImage = pg.image.load("Images/Buttons/button_back.png")
backbuttonImage = pg.transform.scale(backbuttonImage, (50, 50))
spaceshipImage = pg.image.load("Images/spaceship.png")
spaceshipImage = pg.transform.scale(spaceshipImage, (96, 54))
lvl1screenshot = pg.image.load("Images/lvlscrshots/scrsht.png")

# buttons
button_1 = pg.Rect(int(0.22 * resolution[0]), int(0.8 * resolution[1]), 200, 50)
button_2 = pg.Rect(int(0.42 * resolution[0]), int(0.8 * resolution[1]), 200, 50)
button_3 = pg.Rect(int(0.62 * resolution[0]), int(0.8 * resolution[1]), 200, 50)
backbutton = pg.Rect(int(0.95 * resolution[0]), int(0.02 * resolution[0]), 50, 50)

Click = False


def main_menu():
    alpha = 0
    while True:
        gameTime = pygame.time.get_ticks() / 1000.
        screen.blit(mainMenuBackground, (0, 0))
        alpha = fade(screen, mainMenuText, (180, 100), alpha)

        mouseX, mouseY = pygame.mouse.get_pos()

        if button_1.collidepoint((mouseX, mouseY)):
            if click:
                level(1)
        if button_2.collidepoint((mouseX, mouseY)):
            if click:
                options_menu(volume)
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

        housekeepingdata(gameTime, resolution, screen)  # displays runtime and fps

        pg.display.flip()


''''def levelSelect():
    # button stuff - sorry for being a lazy bitch in this part
    buttonLevel = np.zeros(8)
    for j in range(0,8):
        buttonLevel[j] = pg.Rect(int((0.12 + 0.08* j) * resolution[0]), int(0. * resolution[1]), 100, 100)
    buttonLevel1 = pg.Rect(int(0.32 * resolution[0]), int(0. * resolution[1]), 200, 200)
    buttonLevel2 = pg.Rect(int(0.42 * resolution[0]), int(0.5 * resolution[1]), 200, 200)
    buttonLevel3 = pg.Rect(int(0.62 * resolution[0]), int(0.5 * resolution[1]), 200, 200)
    buttonLevel4 = pg.Rect(int(0.62 * resolution[0]), int(0.5 * resolution[1]), 200, 200)
    buttonLevel5 = pg.Rect(int(0.32 * resolution[0]), int(0.8 * resolution[1]), 200, 200)
    buttonLevel6 = pg.Rect(int(0.42 * resolution[0]), int(0.8 * resolution[1]), 200, 200)
    buttonLevel7 = pg.Rect(int(0.52 * resolution[0]), int(0.8 * resolution[1]), 200, 200)
    buttonLevel8 = pg.Rect(int(0.62 * resolution[0]), int(0.8 * resolution[1]), 200, 200)


    ImageLevel1 = pg.image.load("Images/lvlscrshots/scrsht.png")
    ImageLevel1 = pg.transform.scale(ImageLevel1, (200, 200))
    ImageLevel2 = pg.image.load("Images/lvlscrshots/scrsht.png")
    ImageLevel2 = pg.transform.scale(ImageLevel1, (200, 200))
    ImageLevel3 = pg.image.load("Images/lvlscrshots/scrsht.png")
    ImageLevel3 = pg.transform.scale(ImageLevel1, (200, 200))
    ImageLevel4 = pg.image.load("Images/lvlscrshots/scrsht.png")
    ImageLevel4 = pg.transform.scale(ImageLevel1, (200, 200))
    ImageLevel5 = pg.image.load("Images/lvlscrshots/scrsht.png")
    ImageLevel5 = pg.transform.scale(ImageLevel1, (200, 200))
    ImageLevel6 = pg.image.load("Images/lvlscrshots/scrsht.png")
    ImageLevel6 = pg.transform.scale(ImageLevel1, (200, 200))
    ImageLevel7 = pg.image.load("Images/lvlscrshots/scrsht.png")
    ImageLevel7 = pg.transform.scale(ImageLevel1, (200, 200))
    ImageLevel8 = pg.image.load("Images/lvlscrshots/scrsht.png")
    ImageLevel8 = pg.transform.scale(ImageLevel1, (200, 200))


    running = True
    while running:
        click = False
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
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        mouseX, mouseY = pygame.mouse.get_pos()
        for i in range(8):
            if buttonLevel[i].collidepoint((mouseX, mouseY)):
                if click:
                    level(i)


        screen.blit(mainMenuBackground, (0, 0))
        screen.blit(backbuttonImage, backbutton)

        for k in range(8):
            screen.blit(ImageLevel[k], buttonVolumeDown)
        screen.blit(buttonRightImage, buttonVolumeUp)

        housekeepingdata(gameTime, resolution, screen)  # displays runtime and fps
        pg.display.flip()  # displaying on the screen'''


def level(levelNb):
    GameStartTime = pygame.time.get_ticks() / 1000.
    running = True

    background = pg.image.load("Images/background.jpg")
    background = pg.transform.scale(background, resolution)

    Space = Environment(resolution)

    Space.addPlanet(5e5, (500, 200))
    Space.addPlanet(3e5, (200, 300))
    Space.addPlanet(1e6, (700, 500))
    Space.calcTotalGravityField()
    scCoords = (40, 350)
    Projectile = Missile(1, (scCoords[0] + 30, scCoords[1] + 10))

    imageNumb = 0
    fireProjectile = False

    while running:

        gameTime = pygame.time.get_ticks() / 1000.
        click = False
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
                if event.key == pg.K_SPACE:
                    Projectile.Launch(60, firingAngle, Space)
                    fireProjectile = True

        mouseX, mouseY = pygame.mouse.get_pos()
        if backbutton.collidepoint((mouseX, mouseY)):
            if click:
                running = False

        screen.blit(background, (0, 0))
        screen.blit(backbuttonImage, backbutton)

        Space.showPlanet(1, screen, 200)
        Space.showPlanet(2, screen, 100)
        Space.showPlanet(3, screen, 200)
        screen.blit(target, (800, 400))

        firingAngle = playermove(screen, mouseX, mouseY, (40, 350))

        if (fireProjectile == True):
            if Projectile.ReturnPositions(screen) == False:
                pass
            else:
                running = False
                level(levelNb)
                # fireProjectile = False
        print(fireProjectile)

        housekeepingdata(gameTime, resolution, screen)  # displays runtime and fps
        pg.display.flip()  # displaying on the screen


def options_menu(volume):
    # button stuff
    buttonVolumeUp = pg.Rect(int(0.32 * resolution[0]), int(0.5 * resolution[1]), 200, 50)
    buttonVolumeDown = pg.Rect(int(0.58 * resolution[0]), int(0.5 * resolution[1]), 200, 50)
    buttonLeftImage = pg.image.load("Images/Buttons/button_right.png")
    buttonLeftImage = pg.transform.scale(buttonLeftImage, (100, 50))
    buttonRightImage = pg.transform.flip(buttonLeftImage, True, False)

    running = True
    while running:
        click = False
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
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        mouseX, mouseY = pygame.mouse.get_pos()
        if backbutton.collidepoint((mouseX, mouseY)):
            if click:
                running = False

        if buttonVolumeUp.collidepoint((mouseX, mouseY)):
            if click:
                volume -= 0.1
                if volume <= 0:
                    volume = 0
                pg.mixer.music.set_volume(volume)

        if buttonVolumeDown.collidepoint((mouseX, mouseY)):
            if click:
                volume += 0.1
                if volume >= 1:
                    volume = 1
                pg.mixer.music.set_volume(volume)

        screen.blit(mainMenuBackground, (0, 0))
        screen.blit(backbuttonImage, backbutton)

        screen.blit(buttonLeftImage, buttonVolumeDown)
        screen.blit(buttonRightImage, buttonVolumeUp)
        screen.blit(text_func("Music volume", 50, (105, 220, 13)), (520, 320))
        screen.blit(text_func(round(volume * 10), 50, (105, 220, 13)), (610, 370))

        housekeepingdata(gameTime, resolution, screen)  # displays runtime and fps
        pg.display.flip()  # displaying on the screen


main_menu()
