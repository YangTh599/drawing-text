# These are Classes that help with on screen graphics

#font = pygame.font.Font("C:\\Windows/Users/YangTh599/Documents/GitHub/pygame-template/fonts/MoreSugar-Regular.ttf") # MORESUGAR Font

"""

import pygame
from os.path import join
pygame.init()

class Text_box():

    def __init__(self, x, y, width, height, text, text_size = 24):
        self.rect = pygame.Rect(x,y,width,height)
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.text = text
        self.text_size = text_size
        self.text_font = pygame.font.SysFont('Comic Sans MS', text_size)

    def change_font(self, new_font):
        if (new_font[-4:] == ".ttf" or new_font[-4:] == ".otf"):
            self.text_font = pygame.font.Font(new_font, self.text_size)
        else:
            self.text_font = pygame.font.SysFont(new_font, self.text_size)

    def draw_textbox(self):
        img = self.text_font.render(self.text, True, WHITE)
        pygame.draw.rect(window, (50, 200, 50), self.rect)
        text_rect = img.get_rect(center=self.rect.center)
        window.blit(img, text_rect)

class Image_box():

    def __init__(self, x, y, width, height, image):
        self.rect = pygame.Rect(x,y,width,height)
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.image = pygame.image.load(join('assets','images',image))

    def draw_image(self):
        window.blit(self.image, (self.x, self.y))

"""