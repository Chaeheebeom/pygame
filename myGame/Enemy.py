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
        self.rect[0], self.rect[1] = 900, 300
        self.movepos = [0, 7]

    def moveEnemy(self):

        if self.rect[1] >= 540:
            self.movepos = [0,-10]
        elif self.rect[1] <= 20:
            self.movepos = [0, 10]

        #self.movepos[0] = self.movepos[0] + (self.speed)
        newpos = self.rect.move(self.movepos)
        if self.area.contains(newpos):
            self.rect = newpos
        pg.event.pump()

    def attackPlayer(self,playerRect):
        pass