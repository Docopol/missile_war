import sys
import numpy as np
import pygame.time
import pygame as pg
import os

from functionsGame import *
from environment import Environment
from missile import Missile
from levels import Level

pg.init()  # initialise pygame
resolution = (1280, 720)
screen = pg.display.set_mode(resolution)
pg.mouse.set_cursor(pg.cursors.diamond)

# Sounds
pg.mixer.init(48000, -16, 1, 10240)
thing = backGroundMusic = pygame.mixer.music.load("Sounds/Star-Wars-Main-Theme-_Full_.ogg")
pygame.mixer.music.play(-1, 0.0)
volume = 0.3
pg.mixer.music.set_volume(volume)
boomsound = pg.mixer.Sound("Sounds/Explosion Sound Effect.wav")
boomsound.set_volume(0.15)
launchSound = pg.mixer.Sound("Sounds/RPG sound effect.wav")
launchSound.set_volume(0.15)
clickSound = pg.mixer.Sound("Sounds/Button_Plate Click (Minecraft Sound) - Sound Effect for editing.wav")
clickSound.set_volume(1)

# setting background
pg.display.set_caption("Mad Missile")

# loading images
button1Image = pg.image.load("Images/Buttons/button_play.png")
button2Image = pg.image.load("Images/Buttons/button_options.png")
button3Image = pg.image.load("Images/Buttons/button_quit.png")
nextLevelButton = pg.image.load("Images/Buttons/button_next-level.png")
retryLevelButton = pg.image.load("Images/Buttons/button_retry-level.png")
mainMenuButton = pg.image.load("Images/Buttons/button_main-menu.png")
mainMenuBackground = pg.image.load("Images/menuBackground.jpg")
mainMenuBackground = pg.transform.scale(mainMenuBackground, resolution)
target = pg.image.load("Images/target.png")
target = pg.transform.scale(target, (int(0.05 * resolution[0]), int(0.035 * resolution[0])))
mainMenuText = pg.image.load("Images/Text/Mad Missile.png")
backbuttonImage = pg.image.load("Images/Buttons/button_back.png")
backbuttonImage = pg.transform.scale(backbuttonImage, (50, 50))
spaceshipImage = pg.image.load("Images/spaceship.png")
pg.display.set_icon(spaceshipImage)
spaceshipImage = pg.transform.scale(spaceshipImage, (96, 54))
Leveltext = pg.image.load("Images/Text/Level.png")
background = pg.image.load("Images/background.jpg")
background = pg.transform.scale(background, resolution)
youWinText = pg.image.load("Images/Text/You Win!.png")
aliensText = pg.image.load("Images/Text/try to hit the evil aliens!.png")
spacebarText = pg.image.load("Images/Text/use spacebar to launch the missile.png")

# buttons
button_1 = pg.Rect(int(0.22 * resolution[0]), int(0.8 * resolution[1]), 200, 50)
button_2 = pg.Rect(int(0.42 * resolution[0]), int(0.8 * resolution[1]), 200, 50)
button_3 = pg.Rect(int(0.62 * resolution[0]), int(0.8 * resolution[1]), 200, 50)
backbutton = pg.Rect(int(0.95 * resolution[0]), int(0.02 * resolution[0]), 50, 50)

Click = False



def main_menu(volume):
    alpha = 0
    while True:
        gameTime = pygame.time.get_ticks() / 1000.
        screen.blit(mainMenuBackground, (0, 0))
        alpha = fade(screen, mainMenuText, (170, 100), alpha)

        mouseX, mouseY = pygame.mouse.get_pos()
        click = False

        screen.blit(button1Image, button_1)
        screen.blit(button2Image, button_2)
        screen.blit(button3Image, button_3)


        for event in pygame.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        if button_1.collidepoint((mouseX, mouseY)):
            if click:
                pg.mixer.Sound.play(clickSound)
                levelSelect()
        if button_2.collidepoint((mouseX, mouseY)):
            if click:
                pg.mixer.Sound.play(clickSound)
                volume = options_menu(volume)
        if button_3.collidepoint((mouseX, mouseY)):
            if click:
                pg.mixer.Sound.play(clickSound)
                pg.quit()
                sys.exit()


        housekeepingdata(gameTime, resolution, screen)  # displays runtime and fps

        pg.display.flip()


def levelSelect():
    # button stuff
    buttonLevel = np.empty(8, dtype=pg.Rect)
    ImageLevel = np.empty(8, dtype=pg.Rect)
    for j in range(0, 5):
        buttonLevel[j] = pg.Rect(int((0.08 + 0.22 * j) * resolution[0]), int(0.34 * resolution[1]), 200, 200)
        filename = "Images/Buttons/button ("+str(j)+").png"
        ImageLevel[j] = pg.image.load(filename)

    for j in range(4, 8):
        buttonLevel[j] = pg.Rect(int((-0.8 + 0.22 * j) * resolution[0]), int(0.7 * resolution[1]), 200, 200)
        filename = "Images/Buttons/button ("+str(j)+").png"
        ImageLevel[j] = pg.image.load(filename)

    running = True
    levelStart = False
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
                pg.mixer.Sound.play(clickSound)
                running = False

        screen.blit(mainMenuBackground, (0, 0))
        screen.blit(backbuttonImage, backbutton)
        screen.blit(Leveltext, (510, 50))

        for k in range(8):
            screen.blit(ImageLevel[k], buttonLevel[k])


        for i in range(8):
            if buttonLevel[i].collidepoint((mouseX, mouseY)):
                if click:
                    pg.mixer.Sound.play(clickSound)
                    #running = False
                    level(i)


        housekeepingdata(gameTime, resolution, screen)  # displays runtime and fps
        pg.display.flip()  # displaying on the screen'''


def level(lvlnumb):
    global tries, GameStartTime, levelTime
    GameStartTime = pygame.time.get_ticks() / 1000.
    running = True

    tries = 0

    #LevelCur = Level([(0, 100, 5e5, (500, 200)), (1, 300, 1e6, (700, 500))], (800, 400))
    LevelCur = Level(lvlnumb)
    alpha2, alpha3 = 300,300
    imageNumb = 0
    fireProjectile = False
    explosion = False
    soundOn = True
    textON = True
    timeWin = []

    while running:

        gameTime = pygame.time.get_ticks() / 1000.
        levelTime = gameTime - GameStartTime
        click = False

        mouseX, mouseY = pygame.mouse.get_pos()
        firingAngle = playermove(screen, mouseX, mouseY, (40, 350))
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
                    pg.mixer.Sound.play(launchSound, maxtime=3000)
                    LevelCur.Projectile.Launch(60, firingAngle, Level.Space)
                    fireProjectile = True
                    explosion = False
                    imageNumb = 0
                    soundOn = True
                    tries += 1

        if backbutton.collidepoint((mouseX, mouseY)):
            if click:
                pg.mixer.Sound.play(clickSound)
                running = False

        screen.blit(background, (0, 0))
        screen.blit(backbuttonImage, backbutton)

        LevelCur.Space.showPlanets(screen)
        if lvlnumb == 0 and levelTime > 2 and textON:
            alpha2 = fadout(screen, aliensText, (150,100),alpha2)
            if levelTime >6:
                alpha3 = fadout(screen, spacebarText, (50,100),alpha3)
                if levelTime>9:
                    textON = False

        
        screen.blit(target, (LevelCur.targetPosition[0]-30, LevelCur.targetPosition[1]-15))

        firingAngle = playermove(screen, mouseX, mouseY, (40, 350))

        if fireProjectile:
            if not LevelCur.Projectile.ReturnPositions(screen, LevelCur.Space.planetPositions, LevelCur.targetPosition)[0]:
                pass
            else:
                fireProjectile = False
                ready, explosion, xProj,yProj, win = Level.Projectile.ReturnPositions(screen, LevelCur.Space.planetPositions, LevelCur.targetPosition)

        if explosion:

            imageNumb = ExplosionFunc(screen, imageNumb, xProj, yProj, explosion)[0]
            explosion = ExplosionFunc(screen, imageNumb, xProj, yProj, explosion)[1]
            if soundOn:
                pg.mixer.Sound.play(boomsound)
                soundOn = False
            if win:
                timeWin.append(pygame.time.get_ticks() / 1000.)
                if gameTime - timeWin[0] > 1:
                    winnerScreen(lvlnumb)
                    running = False


        housekeepingdata(gameTime, resolution, screen)  # displays runtime and fps
        pg.display.flip()  # displaying on the screen


    return tries


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
                pg.mixer.Sound.play(clickSound)
                running = False

        if buttonVolumeUp.collidepoint((mouseX, mouseY)):
            if click:
                pg.mixer.Sound.play(clickSound)
                volume -= 0.1
                if volume <= 0:
                    volume = 0
                pg.mixer.music.set_volume(volume)

        if buttonVolumeDown.collidepoint((mouseX, mouseY)):
            if click:
                pg.mixer.Sound.play(clickSound)
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
    return volume


def winnerScreen(levelNumber):
    running = True
    #levelTime = round(pygame.time.get_ticks() / 1000. - GameStartTime)
    totalScore = round((1/levelTime +5/tries) *1000)
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

        if button_1.collidepoint((mouseX, mouseY)):
            if click:
                if levelNumber < 7:
                    pg.mixer.Sound.play(clickSound)
                    level(levelNumber+1)
                    running = False
        if button_2.collidepoint((mouseX, mouseY)):
            if click:
                pg.mixer.Sound.play(clickSound)
                level(levelNumber)
                running = False
        if button_3.collidepoint((mouseX, mouseY)):
            if click:
                pg.mixer.Sound.play(clickSound)
                main_menu(volume)
                running = False

        screen.blit(mainMenuBackground, (0, 0))
        screen.blit(youWinText, (340, 20))

        if levelNumber < 7:
            screen.blit(nextLevelButton, button_1)
        screen.blit(retryLevelButton, button_2)
        screen.blit(mainMenuButton, button_3)



        screen.blit(text_func((f'Number of tries: {tries} times'), 60, (116, 252, 114)), (390, 200))
        screen.blit(text_func((f'Completion time: {round(levelTime)} seconds'), 60, (116, 252, 114)), (390, 300))
        screen.blit(text_func((f'Score: {totalScore} points'), 60, (116, 252, 114)), (390, 400))

        housekeepingdata(gameTime, resolution, screen)  # displays runtime and fps
        pg.display.flip()  # displaying on the screen


main_menu(volume)

