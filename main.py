import pygame, sys
import random
import math
import os
from os.path import join
from random import randint as rnd
from pygame.time import delay as slp

from colors import *
from pygame_config import *

def init_game():
    pygame.init() #PYGAME INITIALIZES
    pygame.display.set_caption(PYGAME_CAPTION) # Window Caption

    #Pygame Window
    window = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    return window

# Draw Function to update graphics
def draw(window, texts):
    #BACKGROUND
    window.fill(BLACK) # WHITE BACKGROUND

    #FOREGROUND
    for text in texts:
        text.draw_textbox()

    pygame.display.update()

def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # QUIT
            return False
    
    return True

def main(): # MAIN FUNCTION
    window = init_game() #INITIALIZES PYGAME AND DEFINES WINDOW
    clock = pygame.time.Clock()

    run = True

    text1 = Text_box(window, SCREEN_HEIGHT//2 -50,SCREEN_WIDTH//2 - 50,100,100,"THAYER YANG", draw_rect=False)
    text2 = Text_box(window, SCREEN_HEIGHT//2 -50,SCREEN_WIDTH//2 +50,100,100,"TC CENTRAL", draw_rect=False)

    text1.bolden()
    text1.italicize()
    text2.change_font("fonts/MoreSugar-Regular.ttf")

    while run: # run set to true, program runs while run is true.

        clock.tick(FPS) # FPS Tick

        run = handle_events() # HANDLES EVENTS
        # for event in pygame.event.get():
        #     if event.type == pygame.QUIT: # QUIT
        #         run = False
        #         break
        
        draw(window,[text1, text2]) # UPDATES SCREEN

    #PROGRAM QUITS WHILE RUN IS FALSE
    pygame.quit()
    quit()

class Text_box():

    def __init__(self, window, x, y, width, height, text, font="Comic Sans MS",text_size = 24, draw_rect = True):
        self.rect = pygame.Rect(x,y,width,height)
        self.window = window

        self.x = x
        self.y = y
        self.height = height
        self.width = width

        self.draw_rect = draw_rect

        self.text = text
        self.text_size = text_size
        self.font = font
        self.text_font = pygame.font.SysFont(font, text_size)

    def change_font(self, new_font):
        if (new_font[-4:] == ".ttf" or new_font[-4:] == ".otf"):
            self.text_font = pygame.font.Font(new_font, self.text_size)
        else:
            self.text_font = pygame.font.SysFont(new_font, self.text_size)

    def italicize(self, italicize = True):
        if not (self.font[-4:] == ".ttf" or self.font[-4:] == ".otf"):
            self.text_font = pygame.font.SysFont(self.font, self.text_size, italic=italicize)
    
    def bolden(self, boldize = True):
        if not (self.font[-4:] == ".ttf" or self.font[-4:] == ".otf"):
            self.text_font = pygame.font.SysFont(self.font, self.text_size, bold=boldize)

    def draw_textbox(self):
        text = self.text_font.render(self.text, True, WHITE)
        if self.draw_rect:
            pygame.draw.rect(self.window, (50, 200, 50), self.rect)
        text_rect = text.get_rect(center=self.rect.center)
        self.window.blit(text, text_rect)

if __name__ == "__main__": 
    main() # EXECUTES MAIN

