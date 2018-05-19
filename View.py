from OpenGL.GL import *
from pygame.locals import *
import pygame
from OpenGL.GLU import *
from Model.Model import *
from Model.Enemy.EvilPenguin import *
from Model.Enemy.EvilPig import *
from Model.Hero.Frutilla import *
from Model.Hero.Melon import *
from Model.Hero.Robot import *

class View:
    def __init__(self,alto,ancho):
        '''

        :param alto: alto de la ventana del juego
        :param ancho: ancho de la ventana del juego

        '''
        self.alto=alto
        self.ancho=ancho
        self.pjs = []
        self.enemies= []
        self.hero=[]
        self.surface = None

    def dibujar(self):
        # limpia la pantalla
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        for p in self.pjs:
            p.dibujar()

        for p in self.enemies:
            p.dibujar()

    def init(self):

        # init pygame
        pygame.init()
        self.surface = pygame.display.set_mode((self.ancho, self.alto), OPENGL | DOUBLEBUF)
        #pygame.display.set_caption(titulo)

        # init opengl
        glViewport(0, 0, self.ancho, self.alto)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluOrtho2D(0.0, self.ancho, 0.0, self.alto)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

        # definir variables de opengl
        glClearColor(0.0, 50/255, 0.0, 0.0)  # color del fondo
        glShadeModel(GL_SMOOTH)
        glClearDepth(1.0)
        # glDisable(GL_DEPTH_TEST)


        #init view objects
        self.frutilla = Frutilla(5, 140, 140)
        self.robot = Robot(5, 60, 60)
        self.melon = Melon(5, 250, 250)
        self.pig = EvilPig(5, 60, 60)
        self.penguin = EvilPenguin(5, 350, 350)
        self.laberinto = Laberinto(5, 520, 600)

        self.pjs.append(self.laberinto)
        self.pjs.append(self.robot)
        self.enemies.append(self.melon)
        self.enemies.append(self.frutilla)
        self.enemies.append(self.pig)
        self.enemies.append(self.penguin)

        return


