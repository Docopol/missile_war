import pygame as pg

dt=0.001
imageNumb = 0

class Planets:

    def __init__(self): # im a noob wtf im I supposed to do here
        pass
    def planetVisual(self, planetNumb):  # trying a moving planet by replacing and reloading the png every time. probs pretty slow; edit taakes aabout 2ms per gameloop so thats okay I guess
        global imageNumb
        imageNumb += dt * 100
        numberOfImages = 399
        if imageNumb > numberOfImages:
           imageNumb = 0
        n = str(round(imageNumb))
        filename = "Images/planet1/planet"+ str(planetNumb) + "-"+ str(n) + ".png"
        planetImage = pg.image.load(filename)
        return planetImage




