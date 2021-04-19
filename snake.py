import pygame
from pygame.locals import *

class Snake:
    def __init__(self, block_size, color, coordinates,
                 keys = {'UP': K_w, 'RIGHT':K_d,
                         'DOWN': K_s, 'LEFT': K_a}):
        self.block_size = block_size
        self.speed = block_size
        self.color = color
        self.keys = keys
        self.elements = [coordinates]
        self.dx = 0
        self.dy = 0
        self.ate_food = False
    
    def move(self, pressed_keys):
        if pressed_keys[self.keys['UP']]:
            self.dx = 0
            self.dy = -1
        elif pressed_keys[self.keys['DOWN']]:
            self.dx = 0
            self.dy = 1
        elif pressed_keys[self.keys['RIGHT']]:
            self.dx = 1
            self.dy = 0
        elif pressed_keys[self.keys['LEFT']]:
            self.dx = -1
            self.dy = 0
        
        old_head = self.elements[0]
        head = [old_head[0] + self.dx * self.speed, old_head[1] + self.dy * self.speed]

        if self.ate_food:
            self.elements = [head] + self.elements
        else:
            self.elements = [head] + self.elements[:-1]
        self.ate_food = False
    
    def draw(self, screen):
        for item in self.elements:
            pygame.draw.rect(screen, self.color, [*item, self.block_size, self.block_size])

    def get_head_coordinates(self):
        return self.elements[0]
    
    def get_length(self):
        return len(self.elements)

    def add_block(self):
        self.ate_food = True
    