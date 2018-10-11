import game_framework
from pico2d import *
import main_state

name = "pause_state"
image = None
local_time = None
visible = None

def enter():
    global image, local_time, visible
    local_time = 0.0
    visible = True
    image = load_image('pause.png')

def exit():
    global image
    del(image)


def handle_events():
    events=get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if(event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif(event.type, event.key) == (SDL_KEYDOWN, SDLK_p):
                game_framework.pop_state()

def draw():
    global image, visible
    clear_canvas()
    game_framework.stack[-2].draw()
    if(visible):
        image.draw(400, 300, 100, 100)
    update_canvas()

def update():
    global local_time, visible
    if(local_time > 0.5):
        local_time=0
        if(visible):
            visible=False
        else:
            visible=True
    local_time+=0.01

def pause():
    pass


def resume():
    pass






