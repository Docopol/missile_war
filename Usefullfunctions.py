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