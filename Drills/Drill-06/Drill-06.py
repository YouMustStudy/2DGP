from pico2d import *

KPU_WIDTH, KPU_HEIGHT = 1280, 1024

def GetDxDy(a, b)
    global x,y
    global dx,dy
    global count
    dx,dy=(a-x)/5,(b-y)/5
    count=5

def Move_Character()
    pass

def handle_events():
    global running
    global px,py

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEMOTION:
            px,py=event.x,KPU_HEIGHT-event.y-1
        elif event.type == SDL_MOUSEBUTTONDOWN:
            if event.button == SDL_BUTTON_LEFT:
                GetDxDy(event.x, event.y)

open_canvas(KPU_WIDTH, KPU_HEIGHT)
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')
pointer = load_image('hand_arrow.png')

running = True
px, py = 0, 0
x,y=KPU_WIDTH // 2, KPU_HEIGHT // 2
dx,dy=0, 0
count=5
frame = 0
hide_cursor()

while running:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    character.clip_draw(frame * 100, 100, 100, 100, x, y)
    pointer.draw(px+25,py-25)
    update_canvas()
    frame = (frame + 1) % 8
    Move_Character()
    delay(0.02)
    handle_events()

close_canvas()



