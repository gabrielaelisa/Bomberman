import operator
from Model.Muro import *
from Model.MuroDestructible import *
from Model.PowerUps.MultipleBomb import *
from Model.PowerUps.MoreFire import *
from Model.PowerUps.Salida import *
from Model.Hero.Frutilla import *
from Model.Enemy.Robot import *
from Model.Enemy.Melon import *
from Model.Enemy.Pig import *

ops = {"+": operator.add, "-": operator.sub}

class Laberinto():
    def __init__(self, scale, ALTO, ANCHO):
        self.scale=scale
        self.step= 8*self.scale
        self.ancho =ANCHO
        self.alto= ALTO
        self.laberinto=[] #discretizacio del laberinto
        self.ocupados=[]
        self.muros_indest=[]
        self.muros_dest=[]
        self.enemies= []
        self.powerups=[]
        self.init()

    def init(self):

        self.hero = Frutilla(5, 140, 140)
        robot = Robot(5, 60, 60)
        melon = Melon(5, 140, 140)
        pig = Pig(5, 60, 60)

        self.enemies.append(melon)
        self.enemies.append(robot)
        self.enemies.append(pig)


        step= self.step
        halfstep= step/2

        #discretizacion del ancho en cuadrantes
        d_ancho = int(self.ancho/step)

        #discretizacion del alto en cuadrantes
        d_alto = int(self.alto/step)

        #matriz de posiciones del laberinto
        for n in range(d_ancho):
            x= halfstep + n*step
            for m in range(d_alto):
                y= halfstep + m*step
                self.laberinto.append((x,y))
        #print(self.laberinto)

        i= d_ancho
        j= d_alto -2
        ypos= step +halfstep
        xpos=halfstep

        #creacion de las paredes exteriores del laberinto
        for n in range(i):
            self.muros_indest.append(Muro(self.scale, xpos,halfstep))
            self.muros_indest.append(Muro(self.scale,xpos, self.alto-halfstep))
            xpos+=step
        for n in range(j):
            self.muros_indest.append(Muro(self.scale,halfstep, ypos))
            self.muros_indest.append(Muro(self.scale,self.ancho-halfstep, ypos))
            ypos+=step

        #creacion de paredes interiores del laberinto
        i= i-2
        xpos= 2*step + halfstep
        for n in range(int(i/2)):
            ypos = 2 * step + halfstep
            for m in range(int(j/2)):
                self.muros_indest.append(Muro(self.scale, xpos, ypos))
                ypos+= 2*step
            xpos+= 2*step

        #creacion de las paredes destructibles interiores y powerups
        self.ocupados = list(map(lambda x: x.getPosition(), self.muros_indest))
        for x in range(int((i*j)/4)):
            desocupados = [x for x in self.laberinto if x not in self.ocupados]
            pos= random.choice(desocupados)
            xpos= pos[0]
            ypos=pos[1]
            self.muros_dest.append(MuroDestructible(self.scale,xpos,ypos))
            self.ocupados.append(pos)
            # even
            if x==1:
                self.powerups.append(Salida(self.scale,xpos,ypos))

            if x%4==0:
                choice= random.choice([1, 2])
                if choice==1:
                    self.powerups.append(MultipleBomb(self.scale, xpos, ypos))
                if choice==2:
                    self.powerups.append(MoreFire(self.scale, xpos, ypos))


    def figura(self):
        for i in range(self.muros_indest.__len__()):
            self.muros_indest[i].figura()

        for i in range(self.powerups.__len__()):
            self.powerups[i].figura()

        for i in range(self.muros_dest.__len__()):
            self.muros_dest[i].figura()

        for i in range(self.enemies.__len__()):
            self.enemies[i].figura()

        self.hero.figura()


    def dibujar(self):
        for i in range(self.muros_indest.__len__()):
            self.muros_indest[i].dibujar()

        for i in range(self.powerups.__len__()):
            self.powerups[i].dibujar()

        for i in range(self.muros_dest.__len__()):
            self.muros_dest[i].dibujar()

        for i in range(self.enemies.__len__()):
            self.enemies[i].dibujar()

        self.hero.dibujar()


    def putBomb(self, vector, time):
        xpos = vector[0]
        ypos = vector[1]
        self.ocupados.append(vector)

    def removeItems(self, Bomba):
        pos=Bomba.getPosition()
        xpos = pos[0]
        ypos = pos[1]
        #muro arriba
        up= ypos+ self.step
        #muro abajo
        down= ypos -self.step
        #muro a la izquierda
        left= xpos -self.step
        #muro a la derecha
        right= xpos +self.step

        destroyed=[(xpos,up), (xpos,down), (left,ypos), (right, ypos)]

        for x in self.muros_dest:
            if x.getPosition() in destroyed:
                self.muros_dest.remove(x)
                self.ocupados.remove(x.getPosition())

        for e in self.enemies:
            if e.getPosition() in destroyed:
                self.enemies.remove(e)

        self.ocupados.remove(Bomba.getPosition())

    def loop(self, v_x, v_pos, s_pos, op):
        """

        :param v_x: boolean is x variable? if False-> y is variable
        :param v_pos: variable position
        :param s_pos: static position
        :param op: incrementation or decrementation
        :return: void
        """

        indest = list(map(lambda x: x.getPosition(), self.muros_indest))
        for p in range(int(v_pos), int(v_pos + ops[op](0,1)* 4*self.step), int(ops[op](0,1)*self.step)):
            print(p)
            if v_x:
                point= (p, s_pos)

            if not v_x:
                point=(s_pos, p)

            if point in indest:
                return
            else:
                for m in self.muros_dest:
                    if m.getPosition()== point:
                        self.muros_dest.remove(m)
                        self.ocupados.remove(m.getPosition())
                for e in self.enemies:
                    if e.getPosition()== point:
                        self.enemies.remove(e)



    def removeMoreItems(self,Bomb):
        pos = Bomb.getPosition()
        xpos = pos[0]
        ypos = pos[1]
        #abajo:
        self.loop(False,ypos,xpos, "-")
        #arriba:
        self.loop(False,ypos,xpos,"+")
        #izquierda
        self.loop(True,xpos, ypos, "-")
        #derecha
        self.loop(True,xpos,ypos, "+")
        self.ocupados.remove(Bomb.getPosition())

    def givePowerup(self, hero):
        for x in self.powerups:
            pos = x.getPosition()
            if pos == hero.getPosition():
                hero.getPowerup(x)
                self.powerups.remove(x)








