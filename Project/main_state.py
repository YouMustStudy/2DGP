import random
import json
import os

from pico2d import *
import game_framework
import game_world
import PlayerClass
import TileClass


name = "MainState"

MAP = None
PLAYER = None
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 800


def enter():
    global MAP, PLAYER
    MAP = TileClass.init_tile()
    PLAYER = PlayerClass.Player(MAP[0].x, MAP[0].y, 'p')
    game_world.objects.insert(0, MAP)
    game_world.add_object(PLAYER, 0)


def exit():
    game_world.clear()


def pause():
    pass


def resume():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                game_framework.quit()
        else:
            pass
            #boy.handle_event(event)


def update():
    for game_object in game_world.all_objects():
        game_object.update()



def draw():
    clear_canvas()
    #for tiles in MAP:
    #    tiles.draw()

    for game_object in game_world.all_objects():
        game_object.draw()

    update_canvas()







