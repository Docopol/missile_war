import numpy as np
import pygame as pg
import matplotlib.pyplot as plt


class Environment:

    def __init__(self):
        
        self.x = np.linspace(-500, 1680, 2180)
        self.y = np.linspace(-500, 1220, 1720)
        
        self.X, self.Y = np.meshgrid(self.x, self.y)

        self.Gx, self.Gy = np.zeros((2180, 1720)).T, np.zeros((2180, 1720)).T
        self.planets = []
        self.planetPositions = []
        self.imageNumb = 0

    def addPlanet(self, planetNumb, imageSize, mass, position):
        self.planets.append((planetNumb, imageSize, mass, position))
        self.planetPositions.append(position)

    def showPlanets(self, screen): #Planet animation    
        dt = 0.001
        self.imageNumb += dt * 100
        numberOfImages = 399
        if self.imageNumb > numberOfImages:
            self.imageNumb = 0
        n = str(round(self.imageNumb))

        for planet in self.planets:
            filename = "Images/planets/planet"+ str(planet[0]) +"/planet"+ str(planet[0]) + "-"+ str(n) + ".png"
            planetImage = pg.image.load(filename)
            screen.blit(planetImage, (planet[3][0]-planet[1]/2, planet[3][1]-planet[1]/2))
        
    def calcTotalGravityField(self):
        for planet in self.planets:
            if(planet != None):
                gx, gy = self.gravityField(*planet, x=self.X, y=self.Y)
                self.Gx -= gx
                self.Gy -= gy
            
    def gravityField(self, number, imageSize, mass, r0, x, y):
        dist = np.hypot(x-r0[0], (y-r0[1]))**3
        return mass * (x - r0[0]) / dist, mass * (y - r0[1]) / dist

    def displayGravityField(self): #Function only used for testing purposes
        fig = plt.figure()
        ax = fig.add_subplot(111)

        color = 2 * np.log(np.hypot(self.Gx, self.Gy))
        ax.streamplot(self.x, self.y, self.Gx, self.Gy, color=color, linewidth=1, cmap=plt.cm.inferno,
              density=1, arrowstyle='->', arrowsize=1.5)

        plt.savefig('test.png')

    def destructor(self): #Reinitilase the vector field for each level
        self.planets = []
        self.planetPositions = []
        self.imageNumb = 0

        self.Gx, self.Gy = np.zeros((2180, 1720)).T, np.zeros((2180, 1720)).T