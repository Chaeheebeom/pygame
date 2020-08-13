import pygame as pg
import pygame.sprite as ps
import common

class Enemy(ps.Sprite):

    def __init__(self,screen):
        ps.Sprite.__init__(self)

        self.image, self.rect = common.load_png('bat.png', (40, 40))
        self.speed = 1

        screen = pg.display.get_surface()
        self.area = screen.get_rect()
        self.rect[0], self.rect[1] = 800, 300
        self.movepos = [-10, 0]

    def fire(self,playerRect):
        self.rect = playerRect

    def moveEnemy(self):
        #self.movepos[0] = self.movepos[0] + (self.speed)
        newpos = self.rect.move(self.movepos)
        if self.area.contains(newpos):
            self.rect = newpos
        pg.event.pump()