import numpy as np
import pygame
import math
import numpy

sc0 = pygame.image.load("Images/spaceship.png")


angles = np.arange(-50,51,1)


for i in angles:
    sc = pygame.transform.scale(sc0,(96,54))
    sc = pygame.transform.rotate(sc, i)

    filename = "Images/spacecraft/sc"+str(i)+".png"
    pygame.image.save(sc,filename)
