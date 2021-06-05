import math

import numpy as np
import pygame
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
		timeStep = 0

		time = np.arange(0, self.maxTime, self.dt)


		for index, value in enumerate(time):

			if((round(xPos[index])>= 1680) or (round(xPos[index]) <= -500) or (round(yPos[index]) >= 1220) or (round(yPos[index]) <= -500)):
				break

			newX = xPos[index] + xSpeed[index]*self.dt + environment.Gx[round(yPos[index])+500, round(xPos[index])+500]*self.dt**2/2 
			newY = yPos[index] + ySpeed[index]*self.dt + environment.Gy[round(yPos[index])+500, round(xPos[index])+500]*self.dt**2/2
			newXSpeed = xSpeed[index]+environment.Gx[round(yPos[index])+500, round(xPos[index])+500]*self.dt
			newYSpeed = ySpeed[index]+environment.Gy[round(yPos[index])+500, round(xPos[index])+500]*self.dt
			
			xPos.append(newX)
			yPos.append(newY)
			xSpeed.append(newXSpeed) 
			ySpeed.append(newYSpeed)

		self.xFinal = xPos
		self.yFinal = yPos
		self.xSpeed = xSpeed
		self.ySpeed = ySpeed
		self.timeStep = timeStep

	def ReturnPositions(self, screen, Planetposition,targetPosition): #insert object position
		ready = False


		if(self.timeStep < len(self.xFinal)):
			vx = self.xSpeed[self.timeStep]
			vy = self.ySpeed[self.timeStep]
			phi = -math.atan2(vy, vx) * 180 / math.pi

			filename = "Images/Missile/projectile" + str(round(phi)) + ".png"
			missileImage = pg.image.load(filename)
#			missileRect = pygame.Rect(missileImage)

			#calculating distance between objects
			xProj,yProj = self.xFinal[self.timeStep]+61, self.yFinal[self.timeStep]+10
			for object in range(len(Planetposition)):
				distance = ((xProj+-(Planetposition[object][0]))**2 + (yProj-Planetposition[object][1])**2)**0.5

				if distance <= 50:
					ready = True
					print(distance)
					explosion = True
					return ready, explosion, xProj, yProj

			targetDistance = ((xProj-(targetPosition[0]+20))**2 + (yProj- (targetPosition[1])+10)**2)**0.5
			if targetDistance <= 24:
				ready = True
				explosion = True
				return ready, explosion, xProj, yProj



			if(self.xFinal[self.timeStep] <= 1280 or (self.xFinal[self.timeStep] >= -200) or (self.yFinal[self.timeStep] <= 720) or (self.yFinal[self.timeStep] >= -200)):
				screen.blit(missileImage, (self.xFinal[self.timeStep], self.yFinal[self.timeStep]))
		else:
			ready = True
		self.timeStep += 3
		return ready
