from pico2d import *
import random

WIDTH=800
HEIGHT=600

# Game object class here
class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)

class Boy:
    def __init__(self):
        self.direction=1
        self.move=1
        self.x, self.y = random.randint(0, 800), 90
        self.frame = random.randint(0, 7)
        self.image = load_image('animation_sheet.png')

    def update(self):
        global WIDTH
        if((self.x >= WIDTH) | (self.x<0)):
            self.move *= -1
            if(self.direction):
                self.direction=0
            else:
                self.direction=1
        self.frame=(self.frame +1) %8
        self.x += self.move*5
        
    def draw(self):
        self.image.clip_draw(self.frame*100, self.direction*100, 100, 100, self.x, self.y)

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

# initialization code
open_canvas()
team=[Boy() for i in range(11)]
grass = Grass()
running = True

# game main loop code
while running:
    handle_events()
    for boy in team:
        boy.update()
    clear_canvas()
    grass.draw()
    for boy in team:
        boy.draw()
    update_canvas()
    delay(0.05)
# finalization code
close_canvas()
