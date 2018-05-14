from OpenGL.GL import *
from OpenGL.GL import *
from math import *
import random
class Personaje():

    def __init__(self,scale,x0,y0,rgb=(1.0, 1.0, 1.0)):
        '''

        :param scale:
        :param color:
        :param x0:
        :param y0:
        '''
        self.x0=x0
        self.y0=y0
        self.color=rgb
        self.scale=scale
        self.lista = 0
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