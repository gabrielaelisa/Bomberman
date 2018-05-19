from OpenGL.GL import *
from math import *
import random
import pygame


class Personaje():

    def __init__(self,scale,x0,y0,rgb=(1.0, 1.0, 1.0)):
        '''

        :param scale:
        :param color:
        :param x0:
        :param y0:
        '''
        self.altura=8
        self.x0=x0
        self.y0=y0
        self.color=rgb
        self.scale=scale
        self.lista = 0
        self.step = self.scale * self.altura
        self.direccion =(1,0)
        self.crear()
        self.bomas=0
        self.multipleBomb= False
        self.moreFire= False
        self.salida= False

    def crear(self):
        self.lista = glGenLists(1)
        glNewList(self.lista, GL_COMPILE)
        self.figura()
        glEndList()

    def dibujar(self):
        glPushMatrix()
        glColor3fv(self.color)
        glTranslatef(self.x0, self.y0, 0.0)
        glCallList(self.lista)
        glPopMatrix()

    def figura(self):
        pass

    def getPosition(self):
        return((self.x0, self.y0))

    def move(self, laberinto, xstep, ystep):
        pos= self.getPosition()
        x=pos[0]
        y=pos[1]
        if (x + xstep*self.step, y + ystep*self.step) in laberinto.ocupados:
            return
        else:
            self.x0+= xstep*self.step
            self.y0+= ystep*self.step
            laberinto.givePowerup(self)
           # self.direccion= (xstep, ystep)

    def putBomb(self, laberinto, time):

        pos= self.getPosition()
        if pos in laberinto.ocupados:
            return
        #if self.bomas==3:
        #    return
        else:
            #self.bomas+=1
            laberinto.putBomb(pos, time)

    def isDestroyed(self, x, y):
        if x== self.x0 and y== self.y0:
            return True
        else:
            return False

    def getPowerup(self, power):
        if power.type == "multiplebomb":
            self.multipleBomb= True
        if power.type == "morefire":
            self.moreFire= True
        if power.type == "salida":
            self.salida = True
