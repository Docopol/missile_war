import sys
import pygame.time
import pygame as pg

from Usefullfunctions import *
from environment import *

pg.init()  # initialise pygame
resolution = (1280, 720)
screen = pg.display.set_mode(resolution)

#background music
pg.mixer.init()
pygame.mixer.music.load("Star-Wars-Main-Theme-_Full_.ogg")
pygame.mixer.music.play(-1,0.0)

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
backbuttonImage = pg.transform.scale(backbuttonImage,(50,50))
spaceshipImage = pg.image.load("Images/spaceship.png")
spaceshipImage = pg.transform.scale(spaceshipImage,(96,54))

# buttons
button_1 = pg.Rect(int(0.22 * resolution[0]), int(0.8 * resolution[1]), 200, 50)
button_2 = pg.Rect(int(0.42 * resolution[0]), int(0.8 * resolution[1]), 200, 50)
button_3 = pg.Rect(int(0.62 * resolution[0]), int(0.8 * resolution[1]), 200, 50)
backbutton = pg.Rect(int(0.95 * resolution[0]), int(0.02 * resolution[0]), 50, 50)

Click = False


def main_menu():
    while True:
        gameTime = pygame.time.get_ticks() / 1000.
        screen.blit(mainMenuBackground, (0, 0))
        screen.blit(mainMenuText, (200, 100))

        mouseX, mouseY = pygame.mouse.get_pos()

        if button_1.collidepoint((mouseX, mouseY)):
            if click:
                level(1)
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

        housekeepingdata(gameTime, resolution, screen)  # displays runtime and fps

        pg.display.flip()


def game():
    pass

def level(levelNb):
    GameStartTime = pygame.time.get_ticks() / 1000.
    running = True

    background = pg.image.load("Images/background.jpg")
    background = pg.transform.scale(background, resolution)

    Space = Environment(resolution)
    Space.addPlanet(100, (400, 200))
    imageNumb = 0

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

        mouseX, mouseY = pygame.mouse.get_pos()
        if backbutton.collidepoint((mouseX, mouseY)):
            if click:
                running = False


        screen.blit(background, (0, 0))
        screen.blit(backbuttonImage, backbutton)

        
        # screen.blit(Planets.Planets.planetVisual(self=0, planetNumb=1), (planet1Position))
        Space.showPlanet(1, screen)
        screen.blit(target, ( 520,  250))
        scCoords = (40,350)
        screen.blit(spaceshipImage,(scCoords))
        # screen.blit(Planets.Planets.planet2Visual(self=0), (200, 200))

        housekeepingdata(gameTime, resolution, screen)  # displays runtime and fps
        pg.display.flip()  # displaying on the screen



def options_menu():
    GameStartTime = pygame.time.get_ticks() / 1000.
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

        screen.blit(mainMenuBackground, (0, 0))
        screen.blit(backbuttonImage, backbutton)

        housekeepingdata(gameTime, resolution, screen)  # displays runtime and fps
        pg.display.flip()  # displaying on the screen


main_menu()
