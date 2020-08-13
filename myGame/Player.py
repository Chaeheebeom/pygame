import pygame.sprite as sp
import pygame as pg
import common

PLAYER_IMG_WIDTH = 60
PLAYER_IMG_HEIGHT = 100
PLAYER_IMG_SIZE =(PLAYER_IMG_WIDTH,PLAYER_IMG_HEIGHT)

PLAYER_COLOR = (0,255,0)

class Player(sp.Sprite):

    def __init__(self,screen):
        sp.Sprite.__init__(self)

        # rect : x y 가로 세로
        self.image, self.rect = common.load_png('SDchar.png', (50, 50))

        self.speed = 10
        self.movepos = [0, 0]
        self.state = "still"
        self.area = screen.get_rect()

    def move(self):
        newpos = self.rect.move(self.movepos)
        if self.area.contains(newpos):
            self.rect = newpos
        pg.event.pump()

    def moveup(self):
        self.movepos[1] = self.movepos[1] - (self.speed)
        self.state = "moveup"

    def movedown(self):
        self.movepos[1] = self.movepos[1] + (self.speed)
        self.state = "movedown"

    def moveleft(self):
        self.movepos[0] = self.movepos[0] - (self.speed)
        self.state = "moveleft"

    def moveright(self):
        self.movepos[0] = self.movepos[0] + (self.speed)
        self.state = "moveright"



