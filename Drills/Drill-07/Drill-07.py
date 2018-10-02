from pico2d import *
import random
KPU_WIDTH, KPU_HEIGHT = 1280, 1024

open_canvas(KPU_WIDTH, KPU_HEIGHT)
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')

def GetLine(p1, p2, vertex_num):
    dx = 100//vertex_num
    line=[]
    for i in range(0, 100+1, dx):
        t=i/100
        line.append(((1-t)*p1[0] + t*p2[0], (1-t)*p1[1] + t*p2[1]))
    return line

def MakeRandomPosition(width, height, size):
    points=[(random.randint(0, width), random.randint(0, height)) for i in range(size)]
    return points


points=MakeRandomPosition(KPU_WIDTH, KPU_HEIGHT, 2)
frame=0
line=GetLine(points[0], points[1], 10)
count=0
while True:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    character.clip_draw(frame * 100, 100, 100, 100, line[count][0],line[count][1])
    update_canvas()
    delay(0.01)
    frame = (frame + 1) % 8
    count = (count + 1) % 10
