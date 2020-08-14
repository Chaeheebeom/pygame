import pygame as pg
import pygame.sprite as ps
import common

class EnemyMissile(ps.Sprite):

    def __init__(self,screen):
        ps.Sprite.__init__(self)

        self.image, self.rect = common.load_png('bullet.png', (20, 20))
        self.speed = 1

        screen = pg.display.get_surface()
        self.area = screen.get_rect()
        self.movepos = [-10, 0]

    def fire(self,playerRect):
        self.rect = playerRect

    def moveMissile(self,playerRect):
        #self.movepos[0] = self.movepos[0] + (self.speed)
        newpos = self.rect.move(self.movepos)
        self.rect = newpos
        pg.event.pump()