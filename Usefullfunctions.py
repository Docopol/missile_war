import pygame
import sys


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
    screen.blit(text_func("runtime:"+str(gameTime), 32, (0, 0, 255)),
                (0.87 * resolution[0], 0.85 * resolution[1]))  # displaying runtime

    screen.blit(text_func("fps:" + str(fps_count(gameTime)), 32, (0, 0, 255)),  # displaying fps
                (0.9 * resolution[0], 0.9 * resolution[1]))
