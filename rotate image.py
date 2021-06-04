import numpy as np
import pygame
import math
import numpy

sc0 = pygame.image.load("Images/Missile/pngegg.png")


angles = np.arange(-181,181,1)


for i in angles:
    sc = pygame.transform.scale(sc0,(123,40))
    sc = pygame.transform.rotate(sc, i)

    filename = "Images/Missile/projectile"+str(i)+".png"
    pygame.image.save(sc,filename)
