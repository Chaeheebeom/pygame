import pygame as pg

import common

import Player
import Missile
import Enemy

###색깔들.###
RED = 255, 0, 0        # 적색:   적 255, 녹   0, 청   0
GREEN = 0, 255, 0      # 녹색:   적   0, 녹 255, 청   0
BLUE = 0, 0, 255       # 청색:   적   0, 녹   0, 청 255
PURPLE = 127, 0, 127   # 보라색: 적 127, 녹   0, 청 127
BLACK = 0, 0, 0        # 검은색: 적   0, 녹   0, 청   0
GRAY = 127, 127, 127   # 회색:   적 127, 녹 127, 청 127
WHITE = 255, 255, 255  # 하얀색: 적 255, 녹 255, 청 255
#####
###화면크기###
DISPLAY_WIDTH = 1000
DISPLAY_HEIGHT = 600
DISPLAY = (DISPLAY_WIDTH,DISPLAY_HEIGHT)
######

class GameMaster:
    def __init__(self):
        self._running = True
        self._display_surf = None
        self.size = self.weight, self.height = DISPLAY_WIDTH,DISPLAY_HEIGHT

    def on_init(self):
        pg.init()
        #처음세팅.
        self.init_background()
        self.init_objects()
        self.initMusic('music\\rainbownote-line1.mp3')

        self._running = True

    #배경화면 초기화
    def init_background(self):
        self._display_surf = pg.display.set_mode(DISPLAY, pg.HWSURFACE | pg.DOUBLEBUF)
        pg.display.set_caption("welcome")
        # 배경이미지.
        self.background = pg.image.load("image/background.jpg")
        self.background2 = self.background.copy()
        self.background1_x = 0
        self.background2_x = DISPLAY_WIDTH
        self._display_surf.blit(self.background, (0, 0))

    #오브젝트초기화
    def init_objects(self):
        self.player1 = Player.Player(self._display_surf)
        self.playerSprites = pg.sprite.RenderPlain(self.player1)

        self.missile = Missile.Missile(self._display_surf)
        self.missileSprites = pg.sprite.RenderPlain(self.missile)

        self.enemy= Enemy.Enemy(self._display_surf)
        self.enemySprites = pg.sprite.RenderPlain(self.enemy)

    #화면 움직이기
    def draw_background(self):
        self.background1_x-=2
        self.background2_x-=2

        if self.background1_x == -DISPLAY_WIDTH:
            self.background1_x = DISPLAY_WIDTH
        if self.background2_x == -DISPLAY_WIDTH:
            self.background2_x = DISPLAY_WIDTH

        self._display_surf.blit(self.background, (self.background1_x, 0))
        self._display_surf.blit(self.background2, (self.background2_x, 0))

    #화면에 오브젝트 그리기
    def draw_objects(self):
        self._display_surf.blit(self._display_surf, self.player1.rect, self.player1.rect)
        self.playerSprites.update()
        self.playerSprites.draw(self._display_surf)

        self._display_surf.blit(self._display_surf, self.missile.rect, self.missile.rect)
        self.missileSprites.update()
        self.missileSprites.draw(self._display_surf)

        self._display_surf.blit(self._display_surf, self.enemy.rect, self.enemy.rect)
        self.enemySprites.update()
        self.enemySprites.draw(self._display_surf)

    def movePlayer(self):
        self.player1.move()

    def moveMissile(self):
        for missile in self.missileSprites.sprites():
            missile.moveMissile()

    def moveEnemy(self):
        self.enemy.moveEnemy()

    def deleteMissile(self):
        self.missileSprites.remove(self.missile)

    APMMaximum = 4
    attackPlayerMissiles = 0
    def attackPlayer(self,playerRect):
        self.enemy.attackPlayer(playerRect)

    #음악재생
    def initMusic(self,soundfile):
        pg.mixer.init()
        pg.mixer.music.load(soundfile)
        pg.mixer.music.set_volume(1.0)
        #-1반복재생
        pg.mixer.music.play(-1)

    def on_event(self, event):
        if event.type == pg.QUIT:
            return
        # 키입력 감지
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_UP:
                self.player1.moveup()
            if event.key == pg.K_DOWN:
                self.player1.movedown()
            if event.key == pg.K_LEFT:
                self.player1.moveleft()
            if event.key == pg.K_RIGHT:
                self.player1.moveright()
            if event.key == pg.K_SPACE:
                missile = Missile.Missile(self._display_surf)
                self._display_surf.blit(self._display_surf, missile.rect, missile.rect)
                self.missileSprites.add(missile)
                self.missileSprites.update()
                self.missileSprites.draw(self._display_surf)
                missile.fire(self.player1.rect)

        elif event.type == pg.KEYUP:
            self.player1.movepos = [0, 0]
            self.player1.state = "still"

        #if self.missile.rect[0]+ self.missile.rect[2] == self._display_surf.get_rect()[2]:
        #    self.deleteMissile()

    def on_loop(self):
        self.movePlayer()
        self.moveMissile()
        self.moveEnemy()
        if self.APMMaximum < self.attackPlayerMissiles:
            self.attackPlayer(self.player1.rect)
            self.attackPlayerMissiles+=1

    def on_render(self):
        self.draw_background()
        self.draw_objects()
        pg.display.flip()

    def on_cleanup(self):
        pg.quit()

    def on_execute(self):
        if self.on_init() == False:
            self._running = False

        clock = pg.time.Clock()
        while self._running:
            clock.tick(60)
            for event in pg.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()


def main():
    gm = GameMaster()
    gm.on_execute()

if __name__ == '__main__':
    main()

