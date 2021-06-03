import numpy as np
import matplotlib.pyplot as plt

class Environment:
    gravitationParameter = 1

    def __init__(self, size):
        self.xLength = size[0]
        self.yLength = size[1]
        
        self.x = np.linspace(0, 1080, size[0])
        self.y = np.linspace(0, 720, size[1])
        
        self.X, self.Y = np.meshgrid(self.x, self.y)

        self.Gx, self.Gy = np.zeros(size).T, np.zeros(size).T
        
        self.planets = []

    def addPlanet(self, mass, position):
        self.planets.append((mass, position))
        
    def calcTotalGravityField(self):
        for planet in self.planets:
            gx, gy = self.gravityField(*planet, x=self.X, y=self.Y)
            self.Gx -= gx
            self.Gy -= gy
            
    def gravityField(self, mass, r0, x, y):
        dist = np.hypot(x-r0[0], (y-r0[1]))**3
        return mass * (x - r0[0]) / dist, mass * (y - r0[1]) / dist

    def displayGravityField(self):
        fig = plt.figure()
        ax = fig.add_subplot(111)

        color = 2 * np.log(np.hypot(self.Gx, self.Gy))
        ax.streamplot(self.x, self.y, self.Gx, self.Gy, color=color, linewidth=1, cmap=plt.cm.inferno,
              density=1, arrowstyle='->', arrowsize=1.5)

