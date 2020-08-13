import os
import pygame

def load_png(name,xy=(0,0)):
    x, y = xy
    fullname = os.path.join('image',name)
    try:
        image = pygame.image.load(fullname)
        if image.get_alpha() is None:
            image = image.convert()
        else:
            image = image.convert_alpha()
    except pygame.error as message:
        print('Cannot load image: ', fullname)
        raise SystemExit
    if x == 0 and y == 0:
        return image, image.get_rect()
    image_scale = pygame.transform.scale(image,(x,y))
    return image_scale, image_scale.get_rect()