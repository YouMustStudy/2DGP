from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

x=0
y=90
time=0.005
dx=400
dy=300
theta=0
ramda = 0

while(x<800):
    clear_canvas_now()
    grass.draw_now(400,30)
    character.draw_now(x, y)
    x=x+2
    delay(time)
while(y<600):
    clear_canvas_now()
    grass.draw_now(400,30)
    character.draw_now(x, y)
    y=y+2
    delay(time)
while(x>0):
    clear_canvas_now()
    grass.draw_now(400,30)
    character.draw_now(x, y)
    x=x-2
    delay(time)
while(y>90):
    clear_canvas_now()
    grass.draw_now(400,30)
    character.draw_now(x, y)
    y=y-2
    delay(time)
while(x<400):
    clear_canvas_now()
    grass.draw_now(400,30)
    character.draw_now(x, y)
    x=x+2
    delay(time)

while(theta<360):
    ramda=math.radians(theta)
    clear_canvas_now()
    grass.draw_now(400,30)
    character.draw_now(dx + math.cos(ramda), dy + math.sin(ramda))
    theta=theta+10
    delay(time)
    
close_canvas()
