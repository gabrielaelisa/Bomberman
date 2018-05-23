from OpenGL.GL import *
from math import *
import random
import pygame


class Figure():

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
        self.crear()

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


    def isDestroyed(self, x, y):
        if x== self.x0 and y== self.y0:
            return True
        else:
            return False


