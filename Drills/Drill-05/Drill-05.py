from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

def move_center2right():
    pass
def move_up():
    pass
def move_left():
    pass
def move_down():
    pass
def move_left2center():
    pass

def make_rectangle():
    move_center2right()
    move_up()
    move_left()
    move_down()
    move_left2center()
    
def make_circle():
    pass

while True:
    make_rectangle()
    make_circle()

close_canvas()
