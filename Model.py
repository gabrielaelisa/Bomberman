from Hero.Personaje import *
from Muro import *
from MuroDestructible import *

class Laberinto():
    def __init__(self, scale, ALTO, ANCHO):
        self.scale=scale
        self.ancho =ANCHO
        self.alto= ALTO
        self.laberinto=[]
        self.ocupados=[]
        self.muros_indest=[]
        self.muros_dest=[]

        self.init()

    def init(self):

        #hola=[1,2,3,4]
        #chao=[4,3]
        #l3 = [x for x in hola if x not in chao]
        #print(l3)
        #print(random.choice(l3))
        step= 8*self.scale
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

        #creacion de las paredes destructibles interiores
        self.ocupados = list(map(lambda x: x.getPosition(), self.muros_indest))
        desocupados=[x for x in self.laberinto if x not in self.ocupados]
        for x in range(int((i*j)/4)):
            pos= random.choice(desocupados)
            xpos= pos[0]
            ypos=pos[1]
            self.muros_dest.append(MuroDestructible(self.scale,xpos,ypos))
            self.ocupados.append(pos)



    def figura(self):
            for i in range(self.muros_indest.__len__()):
                self.muros_indest[i].figura()
            for i in range(self.muros_dest.__len__()):
                self.muros_dest[i].figura()

    def dibujar(self):
        for i in range(self.muros_indest.__len__()):
            self.muros_indest[i].dibujar()

        for i in range(self.muros_dest.__len__()):
            self.muros_dest[i].dibujar()

