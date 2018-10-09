from pico2d import *
import random

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

class Small_Ball:
    def __init__(self):
        self.image=load_image('ball21x21.png')
        self.x, self.y = random.randint(0, 800), 600
        self.spd = random.randint(8-5, 8+5)
    def draw(self):
        self.image.draw(self.x, self.y)
    def update(self):
        self.y-=self.spd
        if(self.y < 62 + 10):
            self.spd=0
            self.y=62+10
            
class Big_Ball:
    pass

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

# initialization code
WIDTH=800
HEIGHT=600
MAX_BALL_NUM = 10
SMALL_BALL_NUM=random.randint(0, MAX_BALL_NUM-1)

open_canvas()
grass = Grass()
team=[Boy() for i in range(11)]
S_Balls=[Small_Ball() for i in range(5)]

running = True

# game main loop code
while running:
    handle_events()
    for boy in team:
        boy.update()
    for ball in S_Balls:
        ball.update()
    clear_canvas()
    grass.draw()
    for boy in team:
        boy.draw()
    for ball in S_Balls:
        ball.draw()
    update_canvas()
    delay(0.05)
# finalization code
close_canvas()
