import os
from View import *

os.environ['SDL_VIDEO_CENTERED'] = '1'  # centrar pantalla

class Controller:
    def __init__(self):
        self.V = View(520, 600)
        self.V.init()


    def update(self):
        run = True
        while run:
            time = int(pygame.time.get_ticks()/1000)
            key_pressed = pygame.key.get_pressed()

            #verify if bomb exploded
            bombas= self.V.laberinto.bombas
            for b in bombas:
                b.destroyWall(self.V.laberinto, time)

            if key_pressed[K_UP]:
                self.V.frutilla.move(self.V.laberinto, 0, 1)
                
            # verify if game ended
            if self.V.frutilla.salida:
                run=False

            # make enemies move randombly
            for e in self.V.enemies:
                e.move(self.V.laberinto)

            for event in pygame.event.get():
                if event.type == QUIT:  # cerrar V
                    run = False

                if event.type == KEYDOWN:

                    if event.key == K_SPACE:
                        pass

                    if event.key == K_RIGHT:
                        self.V.frutilla.move(self.V.laberinto, 1, 0)

                    if event.key == K_LEFT:
                        self.V.frutilla.move(self.V.laberinto, -1, 0)

                    if event.key == K_UP:
                        self.V.frutilla.move(self.V.laberinto, 0, 1)

                    if event.key == K_DOWN:
                        self.V.frutilla.move(self.V.laberinto, 0, -1)

                    if event.key == K_a:
                        self.V.frutilla.putBomb(self.V.laberinto, time)



            pygame.display.flip()  # actualizar pantalla
            pygame.time.wait(int(1000 / 30))  # ajusta a 30 fps
            self.V.dibujar()
        pygame.quit()