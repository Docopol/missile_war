import sys
import numpy as np
import pygame.time
import pygame as pg
import os

from functionsGame import *
from environment import Environment
from missile import Missile

pg.init()  # initialise pygame
resolution = (1280, 720)
screen = pg.display.set_mode(resolution)
pg.mouse.set_cursor(pg.cursors.diamond)

# Sounds
pg.mixer.init(48000,-16,1,10240)
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
mainMenuBackground = pg.image.load("Images/menuBackground.jpg")
mainMenuBackground = pg.transform.scale(mainMenuBackground, resolution)
target = pg.image.load("Images/target.png")
target = pg.transform.scale(target, (int(0.05 * resolution[0]), int(0.035 * resolution[0])))
mainMenuText = pg.image.load("Images/Missile War.png")
backbuttonImage = pg.image.load("Images/Buttons/button_back.png")
backbuttonImage = pg.transform.scale(backbuttonImage, (50, 50))
spaceshipImage = pg.image.load("Images/spaceship.png")
pg.display.set_icon(spaceshipImage)
spaceshipImage = pg.transform.scale(spaceshipImage, (96, 54))
lvl1screenshot = pg.image.load("Images/lvlscrshots/scrsht.png")
Leveltext = pg.image.load("Images/Level.png")
background = pg.image.load("Images/background.jpg")
background = pg.transform.scale(background, resolution)

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
                pg.mixer.Sound.play(clickSound)
                levelSelect()
        if button_2.collidepoint((mouseX, mouseY)):
            if click:
                pg.mixer.Sound.play(clickSound)
                options_menu(volume)
        if button_3.collidepoint((mouseX, mouseY)):
            if click:
                pg.mixer.Sound.play(clickSound)
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


def levelSelect():
    # button stuff - sorry for being a lazy bitch in this part
    buttonLevel = np.empty(8,dtype=pg.Rect)
    ImageLevel = np.empty(8,dtype=pg.Rect)
    for j in range(0,8):
        buttonLevel[j] = pg.Rect(int((0.08 + 0.22* j) * resolution[0]), int(0.34 * resolution[1]), 200, 200)
        ImageLevel[j] = pg.image.load("Images/lvlscrshots/scrsht.png")
        #ImageLevel[j].set_colorkey((255,255,255))
        ImageLevel[j] = pg.transform.scale(ImageLevel[j], (200, 200))
    for j in range(4,8):
        buttonLevel[j] = pg.Rect(int((-0.8 + 0.22* j) * resolution[0]), int(0.7 * resolution[1]), 200, 200)
        ImageLevel[j] = pg.image.load("Images/lvlscrshots/scrshot"+str(j)+".png")
        ImageLevel[j].set_colorkey((255,255,255))
        ImageLevel[j] = pg.transform.scale(ImageLevel[j], (200, 200))



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



        if backbutton.collidepoint((mouseX,mouseY)):
            if click:
                pg.mixer.Sound.play(clickSound)
                running = False




        screen.blit(mainMenuBackground, (0, 0))
        screen.blit(backbuttonImage, backbutton)
        screen.blit(Leveltext, (510,50))

        for k in range(8):
            screen.blit(ImageLevel[k], buttonLevel[k])
            screen.blit(text_func(k,42,(0,0,255)),((buttonLevel[k][0])+90,(buttonLevel[k][1])+170))

        for i in range(8):
            if buttonLevel[i].collidepoint((mouseX, mouseY)):
                if click:
                    pg.mixer.Sound.play(clickSound)
                    level(i)

        housekeepingdata(gameTime, resolution, screen)  # displays runtime and fps
        pg.display.flip()  # displaying on the screen'''


def level(lvlnumb):
    GameStartTime = pygame.time.get_ticks() / 1000.
    running = True

    Space = Environment(resolution)

    PlanetPosition = [(500, 200),(700, 500)]

    Space.addPlanet(0, 100, 5e5, PlanetPosition[0])
    #Space.addPlanet(3e5, PlanetPosition[1])
    Space.addPlanet(1, 300, 1e6, PlanetPosition[1])
    Space.calcTotalGravityField()
    scCoords = (40, 350)
    targetPosition = (800,400)
    projectileCoords = (scCoords[0] + 30, scCoords[1] + 10)
    Projectile = Missile(1, projectileCoords)

    imageNumb = 0
    fireProjectile = False
    explosion = False
    soundOn = True
    timeWin = []

    while running:

        gameTime = pygame.time.get_ticks() / 1000.
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
                    Projectile.Launch(60, firingAngle, Space)
                    fireProjectile = True
                    explosion = False
                    imageNumb = 0
                    soundOn = True


        if backbutton.collidepoint((mouseX, mouseY)):
            if click:
                pg.mixer.Sound.play(clickSound)
                running = False

        screen.blit(background, (0, 0))
        screen.blit(backbuttonImage, backbutton)

        Space.showPlanets(screen)
        
        screen.blit(target, targetPosition)

        firingAngle = playermove(screen, mouseX, mouseY, (40, 350))

        if fireProjectile:
            if not Projectile.ReturnPositions(screen, PlanetPosition, targetPosition)[0]:
                pass
            else:
                fireProjectile = False
                ready, explosion, xProj,yProj, win = Projectile.ReturnPositions(screen, PlanetPosition,targetPosition)

        if explosion:

            imageNumb = ExplosionFunc(screen, imageNumb, xProj, yProj, explosion)[0]
            explosion = ExplosionFunc(screen, imageNumb, xProj, yProj, explosion)[1]
            if soundOn:
                pg.mixer.Sound.play(boomsound)
                soundOn = False
            if win:
                timeWin.append(pygame.time.get_ticks() / 1000.)
                if gameTime - timeWin[0] > 1:
                    main_menu()

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

def loadingscreen():

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



        screen.blit(mainMenuBackground, (0, 0))
        screen.blit(text_func("Loading Level",200,(0,0,255)),(140,140))
        pg.time.wait(3000)
        running = False





        housekeepingdata(gameTime, resolution, screen)  # displays runtime and fps
        pg.display.flip()  # displaying on the screen


main_menu()
