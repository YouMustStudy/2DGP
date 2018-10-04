from pico2d import *
import random

def GetLine(p1, p2, p3, p4):
    line=[]
    for i in range(0, 100+1, 2):
        t=i/100
        line.append((((-t**3 + 2*t**2 - t)*p1[0] + (3*t**3 - 5*t**2 + 2)*p2[0] + (-3*t**3 + 4*t**2 + t)*p3[0] + (t**3 - t**2)*p4[0])/2, ((-t**3 + 2*t**2 - t)*p1[1] + (3*t**3 - 5*t**2 + 2)*p2[1] + (-3*t**3 + 4*t**2 + t)*p3[1] + (t**3 - t**2)*p4[1])/2))
    return line

def GetAllLine(Vlist, vertex_num):
    AllLine=[]
    for i in range (vertex_num):
        AllLine.append(GetLine(Vlist[(i-1)%vertex_num], Vlist[(i)%vertex_num], Vlist[(i+1)%vertex_num], Vlist[(i+2)%vertex_num]))
    return AllLine

def MakeRandomPosition(width, height, size):
    points=[(random.randint(0, width), random.randint(0, height)) for i in range(size)]
    return points

KPU_WIDTH, KPU_HEIGHT = 1280, 1024

open_canvas(KPU_WIDTH, KPU_HEIGHT)
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')

MAX_VERTEX=10
LINE_VERTEX=50
frame=0
Vertex_Index=0
Line_Index=0
count=0
points=MakeRandomPosition(KPU_WIDTH, KPU_HEIGHT, MAX_VERTEX)
AllLine=GetAllLine(points, MAX_VERTEX)
while True:
    for i in range(LINE_VERTEX):
        if(AllLine[Vertex_Index][Line_Index][0] < AllLine[Vertex_Index][Line_Index+1][0]):
            direction=1
        else:
            direction=0
        clear_canvas()
        kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
        for n in range(count):
            if(points[(n)%MAX_VERTEX][0] < points[(n+1)%MAX_VERTEX][0]):
                stamp_direction=1
            else:
                stamp_direction=0
            character.clip_draw(100, stamp_direction * 100, 100, 100, points[(n+1)%MAX_VERTEX][0], points[(n+1)%MAX_VERTEX][1])

        character.clip_draw(frame * 100, direction*100, 100, 100, AllLine[Vertex_Index][Line_Index][0],AllLine[Vertex_Index][Line_Index][1])
        update_canvas()
        delay(0.02)
        frame = (frame + 1) % 8
        Line_Index = (Line_Index + 1)
    Line_Index=0
    if(count<MAX_VERTEX):
        count=(count+1)
    Vertex_Index = (Vertex_Index + 1) % MAX_VERTEX