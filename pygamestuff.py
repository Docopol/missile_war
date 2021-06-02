import pygame.time
import pygame as pg
import Planets


pg.init()  # initialise pygame
resolution = (1500, 800)
screen = pg.display.set_mode(resolution)

#setting background
background = pg.image.load("Images/background.jpg")
background = pg.transform.scale(background, resolution)
pg.display.set_caption("Missile war")

# loading images

# basic font
font = pygame.font.SysFont(None, 32)


# gameloop
running = True

GameStartTime = pygame.time.get_ticks() / 1000.
while running:

    gameTime = pygame.time.get_ticks() / 1000.
    pg.event.pump()
    keys = pg.key.get_pressed()
    if keys[pg.K_ESCAPE]:
        running = False
    if keys[pg.K_UP]:
        pass

    for event in pygame.event.get():
        if event.type == pg.QUIT:
            running = False

    screen.blit(background, (0, 0))
    screen.blit(Planets.Planets.planet1Visual(self=0),(400,400))
    screen.blit(Planets.Planets.planet2Visual(self=0),(200,200))

    Text = str(gameTime)
    timeText = font.render(Text, True, (0,0,200))
    screen.blit(timeText, (1400, 20))



    pg.display.flip()

    endLoopTime = pygame.time.get_ticks() / 1000.
    looptime = endLoopTime - gameTime
    print(looptime)
pg.quit()
