from pico2d import *

open_canvas()
grass = load_image('grass.png')
character = load_image('animation_sheet.png')

x = 0
frame=0
Animation_Height =1
Direction=1
spd = 10
TIMER = 0.01

while(1):
    clear_canvas()
    grass.draw(400,30)
    character.clip_draw(frame * 100, (Animation_Height)*100, 100, 100, x, 90)
    update_canvas()
    frame=(frame+1)%8
    x+=Direction*spd
    if( (x>800) | (x<0)):
        Direction=Direction*(-1)
        Animation_Height=(Animation_Height+1)%2
    delay(TIMER)
    get_events()

close_canvas()
