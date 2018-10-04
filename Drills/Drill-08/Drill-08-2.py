from pico2d import *
import random

def GetLine(p1, p2):
    line=[]
    if(p1[0] > p2[0]):
        direction = 0
    else:
        direction = 1
    for i in range(0, 100+1, 2):
        t=i/100
        line.append(((1-t)*p1[0] + t*p2[0], (1-t)*p1[1] + t*p2[1], direction))
    return line

def GetAllLine(Vlist, vertex_num):
    AllLine=[]
    for i in range (vertex_num):
        AllLine.append(GetLine(Vlist[i], Vlist[(i+1)%vertex_num]))
    return AllLine

def MakeRandomPosition(width, height, size):
    points=[(random.randint(0, width), random.randint(0, height)) for i in range(size)]
    return points

KPU_WIDTH, KPU_HEIGHT = 1280, 1024

open_canvas(KPU_WIDTH, KPU_HEIGHT)
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')

MAX_VERTEX=20
LINE_VERTEX=50
frame=0
Vertex_Index=0
Line_Index=0

points=MakeRandomPosition(KPU_WIDTH, KPU_HEIGHT, MAX_VERTEX)
AllLine=GetAllLine(points, MAX_VERTEX)
while True:
    for i in range(LINE_VERTEX):
        clear_canvas()
        kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
        character.clip_draw(frame * 100, AllLine[Vertex_Index][Line_Index][2]*100, 100, 100, AllLine[Vertex_Index][Line_Index][0],AllLine[Vertex_Index][Line_Index][1])
        update_canvas()
        delay(0.02)
        frame = (frame + 1) % 8
        Line_Index = (Line_Index + 1) % LINE_VERTEX
    Line_Index=0
    Vertex_Index = (Vertex_Index + 1) % MAX_VERTEX
