from pico2d import *
import json

import game_framework
import world_build_state

width = height = 0
live_time = 0
rank = None
font = None

def enter():
    global rank, width, height
    width, height = get_canvas_width(), get_canvas_height()
    load_fonts()
    load_rank()
    rank.append(live_time)
    rank.sort()
    del(rank[-1])
    save_rank()

def exit():
    global rank
    rank.clear()

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
    clear_canvas()
    font.draw(width//2, height//2 + 50, 'Total Ranking')
    for i in range(1, 10 + 1):
        font.draw(width//2, height//2-20*i + 50, '#%d. %.2f'%(i, rank[i-1]))
    update_canvas()

def pause():
    pass

def resume():
    pass

def set_time(time):
    global live_time
    live_time = time

def load_rank():
    global rank
    with open('.\\rank.txt', 'rt') as f:
        rank = json.load(f)

def save_rank():
    global rank
    with open('.\\rank.txt', 'wt') as f:
        json.dump(rank, f)

def load_fonts():
    global font
    if font == None:
        font = load_font('ENCR10B.TTF')