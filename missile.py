import numpy as np 

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

		time = np.arange(0, 10, self.dt)


		for index, value in enumerate(time):

			if((round(xPos[index])>= 1080) or (round(xPos[index]) <= 0) or (round(yPos[index]) >= 720) or (round(yPos[index]) <= 0)):
				break

			newX = xPos[index] + xSpeed[index]*self.dt + environment.Gx[round(yPos[index]), round(xPos[index])]*self.dt**2/2 
			newY = yPos[index] + ySpeed[index]*self.dt + environment.Gy[round(yPos[index]), round(xPos[index])]*self.dt**2/2
			newXSpeed = xSpeed[index]+environment.Gx[round(yPos[index]), round(xPos[index])]*self.dt
			newYSpeed = ySpeed[index]+environment.Gy[round(yPos[index]), round(xPos[index])]*self.dt
			print(newX, newY)
			
			xPos.append(newX)
			yPos.append(newY)
			xSpeed.append(newXSpeed) 
			ySpeed.append(newYSpeed)

		return xPos, yPos

	def ReturnPositions(self, screen):

		filename = "Images/Missile0/missile.png"
		missileImage = pg.image.load(filename)
		screen.blit(missileImage, (self.xPos[timeStep], self.yPos[timeStep]))
		timeStep += 1