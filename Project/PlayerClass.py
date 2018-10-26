from pico2d import*


class Player:
    def __init__(self, x, y, shape):
        self.index=0 #현 위치
        self.x = x
        self.y = y
        self.money=0 #총자산
        self.cash=0 #현자산
        self.image = None
        if shape == 'p':
            self.image = load_image('.\\character\\pig.png')
        elif shape == 's':
            self.image = load_image('.\\character\\skeleton.png')
        self.status = RunState
        self.frame = 0

    def draw(self):
        self.status.draw(self)

    def update(self):
        self.status.do(self)

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

#state

class IdleState:
    @staticmethod
    def enter(player):
        player.frame = 0
    @staticmethod
    def exit(player):
        pass
    @staticmethod
    def do(player):
        pass
    @staticmethod
    def draw(player):
        player.image.clip_draw(player.frame * 20, 0, 20, 20, player.x, player.y)
class RunState:
    @staticmethod
    def enter(player):
        player.frame = 0
    @staticmethod
    def exit(player):
        pass
    @staticmethod
    def do(player):
        global MAP
        player.frame = (player.frame+1) % 2
        player.x += 1
        player.x = clamp(MAP[player.index].x, player.x, MAP[player.index+1].x)
    @staticmethod
    def draw(player):
        player.shape.clip_draw(player.frame * 20 + 20, 0, 20, 20, player.x, player.y)