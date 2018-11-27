from pico2d import *
import json

import game_framework
import world_build_state

live_time = 0
rank = None
font = None

def enter():
    load_rank()
    rank.append(live_time)
    rank.sort()
    del(rank[-1])
    save_rank()

def exit():
    del(rank)

def update():
    pass

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(world_build_state)

def draw():
    pass

def pause():
    pass

def resume():
    pass

def set_time(time):
    global live_time
    live_time = time

def load_rank():
    global rank
    with open('.\\rank.txt', 'r') as f:
        rank = json.load(f)

def save_rank():
    global rank
    with open('.\\rank.txt', 'w') as f:
        json.dump(rank, f)

def load_fonts():
    global font
    if font == None:
        font = load_font('ENCR10B.TTF')