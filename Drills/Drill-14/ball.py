import random
from pico2d import *
import game_world
import game_framework

class Ball:
    image = None
    bg = None

    def __init__(self, bg):
        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')
        self.x, self.y, self.fall_speed = random.randint(0, 1837-1), random.randint(0, 1109-1), 0
        if Ball.bg == None:
            Ball.bg = bg

    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def draw(self):
        cx, cy = self.x-self.bg.window_left, self.y-self.bg.window_bottom
        self.image.draw(cx, cy)
        #draw_rectangle(*self.get_bb())

    def update(self):
        self.y -= self.fall_speed * game_framework.frame_time