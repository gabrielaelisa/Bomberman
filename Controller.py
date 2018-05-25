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
            self.V.model.hero.removeBomb(self.V.model,time)
            """bombas= self.V.laberinto.bombas
            for b in bombas:
                b.destroyWall(self.V.laberinto, time)
                b.destroyEnemy(self.V.enemies, time)
                b.destroyHero(self.V.hero, time)
            """
            """"
            if key_pressed[K_UP]:
                self.V.hero.move(self.V.laberinto, 0, 1)

            if key_pressed[K_DOWN]:
                self.V.hero.move(self.V.laberinto, 0, -1)

            if key_pressed[K_LEFT]:
                self.V.hero.move(self.V.laberinto, -1, 0)

            if key_pressed[K_RIGHT]:
                self.V.hero.move(self.V.laberinto, 1, 0)
             """
            # verify if game ended
            if self.V.model.hero.salida:
                run=False
            if self.V.model.hero.dead:
                run=False
            # make enemies move randombly
            for e in self.V.model.enemies:
                e.move(self.V.model, pygame.time.get_ticks())

            for event in pygame.event.get():
                if event.type == QUIT:  # cerrar V
                    run = False

                if event.type == KEYDOWN:

                    if event.key == K_SPACE:
                        pass

                    if event.key == K_RIGHT:
                        self.V.model.hero.move(self.V.model, 1, 0)

                    if event.key == K_LEFT:
                        self.V.model.hero.move(self.V.model, -1, 0)

                    if event.key == K_UP:
                        self.V.model.hero.move(self.V.model, 0, 1)

                    if event.key == K_DOWN:
                        self.V.model.hero.move(self.V.model, 0, -1)

                    if event.key == K_a:
                        self.V.model.hero.putBomb(self.V.model, time)



            pygame.display.flip()  # actualizar pantalla
            pygame.time.wait(int(1000 / 30))  # ajusta a 30 fps
            self.V.dibujar()
        pygame.quit()