from View import *
import os
from Hero.Frutilla import *
from Hero.Robot import *
from Hero.Melon import *
from Enemy.EvilPig import *
from Enemy.EvilPenguin import *
from Muro import *
from MuroDestructible import*
from Model import *

os.environ['SDL_VIDEO_CENTERED'] = '1'  # centrar pantalla
def main():
    ventana = View(520, 600)
    ventana.init()
    frutilla=Frutilla(5,100,100)
    robot= Robot(5, 60,60)
    melon= Melon(5, 250, 250)
    pig= EvilPig(5, 300, 300)
    penguin= EvilPenguin(5, 350, 350)
    laberinto=Laberinto(5,520,600)

    ventana.pjs.append(laberinto)
    ventana.pjs.append(robot)
    ventana.pjs.append(melon)
    ventana.pjs.append(frutilla)
    ventana.pjs.append(pig)
    ventana.pjs.append(penguin)
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == QUIT:  # cerrar ventana
                run = False
            if event.type == KEYDOWN:

                if event.key == K_SPACE:
                    pass

                if event.key == K_RIGHT:
                    robot.move(laberinto.ocupados, 1,0)

                if event.key == K_LEFT:

                    robot.move(laberinto.ocupados, -1, 0)

                if event.key == K_UP:
                    robot.move(laberinto.ocupados, 0, 1)

                if event.key == K_DOWN:
                    robot.move(laberinto.ocupados, 0, -1)
                    
        pygame.display.flip()  # actualizar pantalla
        pygame.time.wait(int(1000 / 30))  # ajusta a 30 fps
        ventana.dibujar()
    pygame.quit()
main()