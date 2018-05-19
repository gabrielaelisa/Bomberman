from Model.Figure import *
class Hero(Figure):
    def __init__(self, scale, x, y):
        super().__init__(scale,x,y)

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