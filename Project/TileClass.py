from pico2d import*
import math

WINDOW_WIDTH=800
WINDOW_HEIGHT=800


class Bigtile:
    image = None

    def __init__(self, x, y):
        self.x, self.y = x, y
        self.sx, self.sy = x, y
        self.radian=0
        if Bigtile.image == None:
            Bigtile.image=load_image('Bigtile.png')
            
    def draw(self):
        self.image.rotate_draw(self.radian, self.x, self.y)

    def update(self):
        pass

    def rotate(self, theta):
        global WINDOW_WIDTH, WINDOW_HEIGHT
        theta=math.radians(theta)
        self.radian += theta
        self.x-=WINDOW_WIDTH/2
        self.y-=WINDOW_HEIGHT/2
        tmp_x, tmp_y = self.x, self.y
        self.x=tmp_x*math.cos(theta) - tmp_y*math.sin(theta)
        self.y=tmp_x*math.sin(theta) + tmp_y*math.cos(theta)
        self.x+=WINDOW_WIDTH/2
        self.y+=WINDOW_HEIGHT/2

    def fix_position(self):
        side = self.radian//90
        self.x, self.y = self.sx*math.cos(side * 90) - self.sy*math.sin(side * 90), self.sx*math.sin(side * 90) + self.sy*math.cos(side * 90)


class Smalltile:
    image = None

    def __init__(self, x, y):
        self.x, self.y = x, y
        self.sx, self.sy = x, y
        self.radian=0
        if Smalltile.image == None:
            Smalltile.image=load_image('Tile.png')
            
    def draw(self):
        self.image.rotate_draw(self.radian, self.x, self.y)

    def update(self):
        pass

    def rotate(self, theta):
        global WINDOW_WIDTH, WINDOW_HEIGHT
        theta=math.radians(theta)
        self.radian +=theta
        self.x-=WINDOW_WIDTH/2
        self.y-=WINDOW_HEIGHT/2
        tmp_x, tmp_y = self.x, self.y
        self.x=tmp_x*math.cos(theta) - tmp_y*math.sin(theta)
        self.y=tmp_x*math.sin(theta) + tmp_y*math.cos(theta)
        self.x+=WINDOW_WIDTH/2
        self.y+=WINDOW_HEIGHT/2
        
    def fix_position(self):
        side = self.radian//90
        self.x, self.y = self.sx*math.cos(side * 90) - self.sy*math.sin(side * 90), self.sx*math.sin(side * 90) + self.sy*math.cos(side * 90)


def load_position(x, y):
    pos=[]
    tile=load_image('Tile.png')
    bigtile=load_image('Bigtile.png')
    x-=3*tile.w + bigtile.w/2
    y-=3*tile.w + bigtile.w/2
    pos.append(Bigtile(x, y))
    x+= bigtile.w/2 + tile.w/2
    for i in range(6):
        pos.append(Smalltile(x, y))
        x+=tile.w
    del(tile)
    del(bigtile)
    return pos


def init_tile():
    pos=load_position(WINDOW_WIDTH/2, WINDOW_HEIGHT/2)
    pos+=load_position(WINDOW_WIDTH/2, WINDOW_HEIGHT/2)
    for i in range(7):
        pos[-(i+1)].rotate(90)
    pos+=load_position(WINDOW_WIDTH/2, WINDOW_HEIGHT/2)
    for i in range(7):
        pos[-(i+1)].rotate(180)
    pos+=load_position(WINDOW_WIDTH/2, WINDOW_HEIGHT/2)
    for i in range(7):
        pos[-(i+1)].rotate(270)
    return pos


def rotate_world():
    global pos
    for i in range(9):
        clear_canvas()
        for things in pos:
            things.rotate(-10)
            things.draw()
        update_canvas()
        delay(0.03)
    for things in pos:
        things.fix_position()
