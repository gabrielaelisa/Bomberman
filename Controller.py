import os
from View import *
from Model.Model import *
from Model.Enemy.EvilPenguin import *
from Model.Enemy.EvilPig import *
from Model.Hero.Frutilla import *
from Model.Hero.Melon import *
from Model.Hero.Robot import *

os.environ['SDL_VIDEO_CENTERED'] = '1'  # centrar pantalla

class Controller:
    def __init__(self):
        self.ventana = View(520, 600)
        self.ventana.init()
        self.frutilla = Frutilla(5, 100, 100)
        self.robot = Robot(5, 60, 60)
        self.melon = Melon(5, 250, 250)
        self.pig = EvilPig(5, 200, 200)
        self.penguin = EvilPenguin(5, 350, 350)
        self.laberinto = Laberinto(5, 520, 600)
        self.ventana.pjs.append(self.laberinto)
        self.ventana.pjs.append(self.robot)
        self.ventana.pjs.append(self.melon)
        self.ventana.pjs.append(self.frutilla)
        self.ventana.pjs.append(self.pig)
        self.ventana.pjs.append(self.penguin)
        self.ex1 = pygame.image.load(os.path.join("images/explosion1.png"))
    def update(self):
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == QUIT:  # cerrar ventana
                    run = False
                if event.type == KEYDOWN:

                    if event.key == K_SPACE:
                        pass

                    if event.key == K_RIGHT:
                        self.robot.move(self.laberinto.ocupados, 1, 0)

                    if event.key == K_LEFT:
                        self.robot.move(self.laberinto.ocupados, -1, 0)

                    if event.key == K_UP:
                        self.robot.move(self.laberinto.ocupados, 0, 1)

                    if event.key == K_DOWN:
                        self.robot.move(self.laberinto.ocupados, 0, -1)

                    if event.key == K_a:
                        self.robot.putBomb(self.laberinto)
                   # if event.key== K_s:
                    #    self.laberinto.bombas[0].destroyWall(self.ventana.surface, 'images/explosion1.png')

            pygame.display.flip()  # actualizar pantalla
            pygame.time.wait(int(1000 / 30))  # ajusta a 30 fps
            self.ventana.dibujar()
        pygame.quit()