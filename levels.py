import numpy as np
import pygame as pg
from environment import Environment
from missile import Missile

class Level:

	scCoords = (40, 350)
	projectileCoords = (scCoords[0] + 30, scCoords[1] + 10)
	Space = Environment()
	Projectile = Missile(1, projectileCoords)



	def __init__ (self, levelNumber):
		
		self.Space.destructor()
		planets, target = self.LevelSelector(levelNumber)

		for planet in planets:
			self.Space.addPlanet(*planet)

		self.Space.calcTotalGravityField()
		self.targetPosition = target


	def LevelSelector(self, levelNumber):
		planets = dict([('Icy-Despair', (0, 100, 5e5)), ('Saturn-Rewinded', (1, 300, 1e6)), ('Moon', (2, 100, 2e5)), ('Radioactive-sun', (3, 200, 3e6)), ('Jupiler', (4, 100, 1e6))])
		levels = dict([(0 , (((*planets['Moon'], (450, 350)), ), (850, 350))), 
			(1 , (((*planets['Moon'], (750, 500)), (*planets['Radioactive-sun'], (700, 250))), (800, 420))),
			(2 , (((*planets['Saturn-Rewinded'], (500, 500)), (*planets['Jupiler'], (1200, 400))), (800, 420)))])

		return levels[levelNumber]