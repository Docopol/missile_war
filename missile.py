import math

import numpy as np
import pygame as pg

class Missile:
	dt = 0.01
	maxTime = 100

	def __init__ (self, mass, position):
		self.position = position
		self.mass = mass
		self.timeStep = 0

	def Launch(self, speed, angle, environment):
		xPos = [self.position[0],]
		yPos = [self.position[1],]
		xSpeed = [speed*np.cos(np.radians(angle)), ]
		ySpeed = [speed*np.sin(np.radians(angle)), ]

		time = np.arange(0, self.maxTime, self.dt)


		for index, value in enumerate(time):

			if((round(xPos[index])>= 1280) or (round(xPos[index]) <= -200) or (round(yPos[index]) >= 720) or (round(yPos[index]) <= -200)):
				break

			newX = xPos[index] + xSpeed[index]*self.dt + environment.Gx[round(yPos[index]), round(xPos[index])]*self.dt**2/2 
			newY = yPos[index] + ySpeed[index]*self.dt + environment.Gy[round(yPos[index]), round(xPos[index])]*self.dt**2/2
			newXSpeed = xSpeed[index]+environment.Gx[round(yPos[index]), round(xPos[index])]*self.dt
			newYSpeed = ySpeed[index]+environment.Gy[round(yPos[index]), round(xPos[index])]*self.dt
			
			xPos.append(newX)
			yPos.append(newY)
			xSpeed.append(newXSpeed) 
			ySpeed.append(newYSpeed)

		self.xFinal = xPos
		self.yFinal = yPos
		self.xSpeed = xSpeed
		self.ySpeed = ySpeed

	def ReturnPositions(self, screen):
		ready = False


		if(self.timeStep < len(self.xFinal)):
			vx = self.xSpeed[self.timeStep]
			vy = self.ySpeed[self.timeStep]
			phi = -math.atan2(vy, vx) * 180 / math.pi

			filename = "Images/Missile/projectile" + str(round(phi)) + ".png"
			missileImage = pg.image.load(filename)
			screen.blit(missileImage, (self.xFinal[self.timeStep], self.yFinal[self.timeStep]))
		else:
			ready = True
		self.timeStep += 3
		return ready
