from OpenGL.GL import *
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
        if (self.x0 + xstep*self.step, self.y0 + ystep*self.step) in laberinto:
            return
        else:
            self.x0+= xstep*self.step
            self.y0+= ystep*self.step
           # self.direccion= (xstep, ystep)

    def putBomb(self, laberinto, time):

        pos= (self.x0, self.y0)
        if pos in laberinto.ocupados:
            return
        #if self.bomas==3:
        #    return
        else:
            #self.bomas+=1
            laberinto.putBomb(pos, time)