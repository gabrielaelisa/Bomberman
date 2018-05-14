from View import *
import os
from Hero.Frutilla import *
from Hero.Robot import *
from Hero.Melon import *
from Muro import *
from MuroDestructible import*
from Model import *

os.environ['SDL_VIDEO_CENTERED'] = '1'  # centrar pantalla
def main():
    ventana = View(520, 600)
    ventana.init()
    frutilla=Frutilla(5,100,100)
    robot= Robot(5, 200,200)
    melon= Melon(5, 250, 250)
    muro= Muro(5, 20,20)
    laberinto=Laberinto(5,520,600)
    muroDest= MuroDestructible(5,60, 20)

    ventana.pjs.append(laberinto)
    ventana.pjs.append(robot)
    ventana.pjs.append(melon)
    ventana.pjs.append(frutilla)
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == QUIT:  # cerrar ventana
                run = False
        pygame.display.flip()  # actualizar pantalla
        pygame.time.wait(int(1000 / 30))  # ajusta a 30 fps
        ventana.dibujar()
    pygame.quit()
main()