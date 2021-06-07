import math
import numpy as np
import pygame
import pygame as pg

class Missile:
	dt = 0.01
	maxTime = 1000

	def __init__ (self, position):
		self.position = position
		self.timeStep = 0

	def Launch(self, speed, angle, environment):
		xPos = [self.position[0],]
		yPos = [self.position[1],]
		xSpeed = [speed*np.cos(np.radians(angle)), ]
		ySpeed = [speed*np.sin(np.radians(angle)), ]
		timeStep = 0

		#The next lines of code are the numerical integration of the trajectory of the missile

		time = np.arange(0, self.maxTime, self.dt)

		for index, value in enumerate(time):

			#If the missile goes to far off break

			if((round(xPos[index])>= 1680) or (round(xPos[index]) <= -500) or (round(yPos[index]) >= 1220) or (round(yPos[index]) <= -500)):
				break 

			#Compute the new positions

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

	def ReturnPositions(self, screen, planetposition,targetPosition): 
		ready = False

		if(self.timeStep < len(self.xFinal)):

			#Making the missile turn

			vx = self.xSpeed[self.timeStep]
			vy = self.ySpeed[self.timeStep]
			phi = -math.atan2(vy, vx) * 180 / math.pi

			filename = "Images/Missile/projectile" + str(round(phi)) + ".png"
			missileImage = pg.image.load(filename)

			xProj,yProj = self.xFinal[self.timeStep]+50, self.yFinal[self.timeStep]+10

			#If the missile touches the planet it explodes and you're a noobie

			for planet in planetposition:
				distance = ((xProj-planet[0])**2 + (yProj-planet[1])**2)**0.5

				if distance <= 50:
					ready = True
					explosion = True
					win = False
					return ready, explosion, xProj, yProj, win

			#If the the missile touches a target, you win big time

			targetDistance = ((xProj-(targetPosition[0]+20))**2 + (yProj- (targetPosition[1])+10)**2)**0.5
			if targetDistance <= 24:
				ready = True
				explosion = True
				win = True
				return ready, explosion, xProj, yProj, win

			#Don't show a missile who's still flying but has got out of the screen
				
			if(self.xFinal[self.timeStep] <= 1280 or (self.xFinal[self.timeStep] >= -200) or (self.yFinal[self.timeStep] <= 720) or (self.yFinal[self.timeStep] >= -200)):
				screen.blit(missileImage, (self.xFinal[self.timeStep], self.yFinal[self.timeStep]))

		else:
			ready = True
		self.timeStep += 3

		return ready, None, None, None, None
