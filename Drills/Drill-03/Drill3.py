from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

x=0
y=90
time=0.01
dx=400
dy=300
theta=0
ramda = 0
r = 210
spd = 5
while(1):
    while(x<800):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x, y)
        x=x+spd
        delay(time)
    while(y<600):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x, y)
        y=y+spd
        delay(time)
    while(x>0):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x, y)
        x=x-spd
        delay(time)
    while(y>90):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x, y)
        y=y-spd
        delay(time)
    while(x<400):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x, y)
        x=x+spd
        delay(time)

    theta = 0
    while(theta<=360):
        ramda=math.radians(theta-90)
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(dx + r*math.cos(ramda), dy + r*math.sin(ramda))
        theta=theta+5
        delay(time)
    
close_canvas()
