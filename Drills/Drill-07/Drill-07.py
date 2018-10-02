from pico2d import *
import random

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

KPU_WIDTH, KPU_HEIGHT = 1280, 1024


open_canvas(KPU_WIDTH, KPU_HEIGHT)
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')

MAX_VERTEX=10
LINE_VERTEX=20
frame=0
Vertex_Index=0
Line_Index=0

points=MakeRandomPosition(KPU_WIDTH, KPU_HEIGHT, MAX_VERTEX)
while True:
    line=GetLine(points[Vertex_Index], points[(Vertex_Index+1)%MAX_VERTEX], LINE_VERTEX)
    for i in range(LINE_VERTEX-1):
        clear_canvas()
        kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
        character.clip_draw(frame * 100, 100, 100, 100, line[Line_Index][0], line[(Line_Index+1)%LINE_VERTEX][1])
        update_canvas()
        delay(0.02)
        frame = (frame + 1) % 8
        Line_Index = (Line_Index + 1) % LINE_VERTEX
    Line_Index=0
    Vertex_Index = (Vertex_Index + 1) % MAX_VERTEX
