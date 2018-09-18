from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('animation_sheet.png')


def move_rotation():
    move_count=50
    frame=0
    Direction=1
    Position=[(203, 535), (132, 243), (535, 470), (477, 203), (715, 136), (316, 225), (510, 92), (692, 518), (682, 336), (712, 349)]

    for num in range(0, 10):
        x,y=Position[num]
        if(num != 10-1):
            x1,y1=Position[num]
            x2,y2=Position[num+1]
        else:
            x1,y1=Position[num]
            x2,y2=Position[0]
        dx,dy=(x2-x1)/move_count,(y2-y1)/move_count
        if(dx>0) :Direction = 1
        else :Direction = 0
        
        for count in range(0, move_count):
            clear_canvas()
            grass.draw(400, 30)
            character.clip_draw(frame * 100, (Direction)*100, 100, 100, x, y)
            update_canvas()
            frame=(frame+1)%8
            x+=dx
            y+=dy
            delay(0.01)

while True:
    move_rotation()

close_canvas()
