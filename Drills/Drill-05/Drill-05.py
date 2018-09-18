from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

def move_rotation():
    Position=[(203, 535), (132, 243), (535, 470), (477, 203), (715, 136), (316, 225), (510, 92), (692, 518), (682, 336), (712, 349)]
    for num in range(0, 10):
        x,y=Position[num]
        if(num != 10-1):
            x1,y1=Position[num]
            x2,y2=Position[num+1]
        else:
            x1,y1=Position[num]
            x2,y2=Position[0]
        dx,dy=(x2-x1)/5,(y2-y1)/5
        for count in range(0, 5):
            clear_canvas_now()
            grass.draw_now(400, 30)
            character.draw_now(x, y)
            x+=dx
            y+=dy
            delay(0.01)

while True:
    move_rotation()

close_canvas()
