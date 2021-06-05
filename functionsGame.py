import pygame
import pygame as pg
import sys
import math


def text_func(message, size, color):
    font = pygame.font.SysFont(None, size)
    Text = str(message)
    output = font.render(Text, True, color)
    return output

def fps_count(gameTime):
    endLoopTime = pygame.time.get_ticks() / 1000.
    looptime = endLoopTime - gameTime
    fps = round(1/(looptime+0.00000001))
    return fps

def housekeepingdata(gameTime,resolution,screen):
    screen.blit(text_func("runtime:"+str(gameTime), 25, (0, 0, 255)),
                (0.87 * resolution[0], 0.92 * resolution[1]))  # displaying runtime

    screen.blit(text_func("fps:" + str(fps_count(gameTime)), 25, (0, 0, 255)),  # displaying fps
                (0.9 * resolution[0], 0.95 * resolution[1]))


def playermove(screen, mouseX, mouseY, scCoords):
    #trigonometry
    opposite = scCoords[1] +27 - mouseY
    adjacent = mouseX - scCoords[0] + 80
    angle = round(math.atan2(opposite,adjacent) / math.pi *180)
    if angle < - 90:
        angle = -90
    if angle > 90:
        angle = 90

    filename = "Images/spacecraft/sc" + str(angle) +".png"
    playerimage = pg.image.load(filename)
    screen.blit(playerimage,(scCoords))

    return -angle

def fade(screen, image, position,alpha):

        image.set_alpha(alpha)
        screen.blit(image,(position))
        alpha = float(alpha) + 0.7
        return alpha

class LoadingImages:
    def __init__(self):
        pass





