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
		planets = dict([('Icy-Despair', (0, 100, 5e5)), ('Saturn-Rewinded', (1, 300, 1e6)), ('Moon', (2, 100, 2e5)), ('Radioactive-sun', (3, 200, 3e6)), ('Jupiler', (4, 100, 1e6)), ('Earthish', (5, 100, 1e6)), ('Lavalamp', (6, 100, 1e6)), ('Smurfplanet', (7, 100, 1e6)), ('Doomhole', (8, 200, 1e8)), ('Greener', (9, 100, 1e6))])
		levels = dict([(0 , (((*planets['Moon'], (450, 350)), ), (850, 350))), 
			(1 , (((*planets['Moon'], (750, 500)), (*planets['Radioactive-sun'], (700, 250))), (800, 420))),
			(2 , (((*planets['Saturn-Rewinded'], (500, 500)), (*planets['Jupiler'], (200, 500)), (*planets['Smurfplanet'], (700, 250))), (700, 420))),
			(3,  (((*planets['Saturn-Rewinded'], (650, 550)), (*planets['Earthish'], (900  , 600)),(*planets['Icy-Despair'], (450, 320))), (800, 420))),
			(4, (((*planets['Doomhole'], (1200, 360)),(*planets['Lavalamp'], (400  , 200))), (1100, 130))),
			(5, (((*planets['Radioactive-sun'], (1000, 360)), (*planets['Greener'], (400, 360)), (*planets['Saturn-Rewinded'], (700, 360))), (1100, 360))),
			(6, (((*planets['Smurfplanet'], (1200, 360)), (*planets['Greener'], (700, 250)),(*planets['Lavalamp'], (400  , 200)),(*planets['Saturn-Rewinded'], (500, 500)),(*planets['Moon'], (750, 500))), (1000, 660))),
			(7, (((*planets['Earthish'], (800, 360)), (*planets['Jupiler'], (400, 200)),(*planets['Moon'], (900, 500))), (20, 130)))
					   ])

		return levels[levelNumber]