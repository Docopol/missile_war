import pygame as pg

dt=0.001
imageNumb1, imageNumb2, imageNumb3 = 0,0,0

class Planets:
    def __init__(self): # im a noob wtf im I supposed to do here
        pass
    def planet1Visual(self):  # trying a moving planet by replacing and reloading the png every time. probs pretty slow; edit taakes aabout 2ms per gameloop so thats okay I guess
        global imageNumb2
        imageNumb2 += dt * 100
        numberOfImages = 399
        if imageNumb2 > numberOfImages-1:
           imageNumb2 = 0
        n = str(round(imageNumb2))
        filename = "Images/planet1/planet1-" + n + ".png"
        planet1 = pg.image.load(filename)
        return planet1


    def planet2Visual(self):
        global imageNumb1
        imageNumb1 += dt * 100
        numberOfImages = 399
        if imageNumb1 > numberOfImages-1:
           imageNumb1 = 0
        n = str(round(imageNumb1))
        filename = "Images/planet2/planetlocations-" + n + ".png"
        planet2 = pg.image.load(filename)
        return planet2

