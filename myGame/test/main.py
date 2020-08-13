# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import sys
import pygame
import math
import common
import random
from Bat import Bat

DISPLAY_WIDTH = 600
DISPLAY_HEIGHT = 600

class Ball(pygame.sprite.Sprite):

    def __init__(self, xy, vector):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = common.load_png('ball.png',(30,30))
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        self.vector = vector
        self.hit = 0

    def update(self):
        newpos = self.calcnewpos(self.rect,self.vector)
        self.rect = newpos
        (angle,z) = self.vector

        if not self.area.contains(newpos):
            tl = not self.area.collidepoint(newpos.topleft)
            tr = not self.area.collidepoint(newpos.topright)
            bl = not self.area.collidepoint(newpos.bottomleft)
            br = not self.area.collidepoint(newpos.bottomright)
            if tr and tl or (br and bl):
                angle = -angle
            if tl and bl:
                #self.offcourt()
                angle = math.pi - angle
            if tr and br:
                angle = math.pi - angle
                #self.offcourt()
        else:
            # Deflate the rectangles so you can't catch a ball behind the bat
            player1.rect.inflate(-3, -3)
            player2.rect.inflate(-3, -3)

            # Do ball and bat collide?
            # Note I put in an odd rule that sets self.hit to 1 when they collide, and unsets it in the next
            # iteration. this is to stop odd ball behaviour where it finds a collision *inside* the
            # bat, the ball reverses, and is still inside the bat, so bounces around inside.
            # This way, the ball can always escape and bounce away cleanly
            if self.rect.colliderect(player1.rect) == 1 and not self.hit:
                angle = math.pi - angle
                self.hit = not self.hit
            elif self.rect.colliderect(player2.rect) == 1 and not self.hit:
                angle = math.pi - angle
                self.hit = not self.hit
            elif self.hit:
                self.hit = not self.hit
        self.vector = (angle,z)

    def calcnewpos(self,rect,vector):
        (angle,z) = vector
        (dx,dy) = (z*math.cos(angle),z*math.sin(angle))
        return rect.move(int(round(dx)),int(round(dy)))

def main():
    # Use a breakpoint in the code line below to debug your script.
    pygame.init()
    pygame.display.set_caption('mygame')
    screen = pygame.display.set_mode((DISPLAY_WIDTH,DISPLAY_HEIGHT))

    background=pygame.Surface(screen.get_size())
    #convert해주는게 속도면에서 여러개의 이미지처리에서 유리
    background=background.convert()
    #배경화면색 채워줌
    background.fill((255,255,255))

    #font객체생성(폰트,크기)
    font = pygame.font.Font(None,36)
    #글자, 안티얼라이즈 유무, 색깔
    text = font.render("Hello Game",1,(10,10,10))
    textpos = text.get_rect()
    textpos.centerx = background.get_rect().centerx
    background.blit(text, textpos)

    screen.blit(background,(0,0))
    pygame.display.flip()

    global player1
    global player2
    player1 = Bat("left")
    player2 = Bat("right")

    # Initialise ball
    speed = 13
    rand = ((0.1 * (random.randint(5, 8))))
    ball = Ball((0, 0), (0.47, speed))

    # Initialise sprites
    playersprites = pygame.sprite.RenderPlain((player1, player2))
    ballsprite = pygame.sprite.RenderPlain(ball)

    # Blit everything to the screen
    screen.blit(background, (0, 0))
    pygame.display.flip()

    # Initialise clock
    clock = pygame.time.Clock()

    # Event loop
    while 1:
        # Make sure game doesn't run at more than 60 frames per second
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    player1.moveup()
                if event.key == pygame.K_z:
                    player1.movedown()
                if event.key == pygame.K_UP:
                    player2.moveup()
                if event.key == pygame.K_DOWN:
                    player2.movedown()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_a or event.key == pygame.K_z:
                    player1.movepos = [0, 0]
                    player1.state = "still"
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    player2.movepos = [0, 0]
                    player2.state = "still"

        screen.blit(background, ball.rect, ball.rect)
        screen.blit(background, player1.rect, player1.rect)
        screen.blit(background, player2.rect, player2.rect)
        ballsprite.update()
        playersprites.update()
        ballsprite.draw(screen)
        playersprites.draw(screen)
        pygame.display.flip()



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
