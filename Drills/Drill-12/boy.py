from pico2d import *
from ball import Ball

import game_world
import game_framework
import random

# Boy Run Speed
PIXEL_PER_METER = (10.0 / 0.3)
RUN_SPEED_KMPH = 20.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# Boy Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8.0

# Boy Ghost Status
RADIUS_METER = 3.0
RADIUS_PIXEL = RADIUS_METER * PIXEL_PER_METER
ROUND_PER_SEC = 2.0
THETA_PER_SEC = math.radians(ROUND_PER_SEC * 360)

# Boy Event
RIGHT_DOWN, LEFT_DOWN, RIGHT_UP, LEFT_UP, SLEEP_TIMER, SPACE, LSHIFT_DOWN, RSHIFT_DOWN, LSHIFT_UP, RSHIFT_UP, TIRED_TIMER = range(11)

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RIGHT_DOWN,
    (SDL_KEYDOWN, SDLK_LEFT): LEFT_DOWN,
    (SDL_KEYUP, SDLK_RIGHT): RIGHT_UP,
    (SDL_KEYUP, SDLK_LEFT): LEFT_UP,
    (SDL_KEYDOWN, SDLK_SPACE): SPACE,
    (SDL_KEYDOWN, SDLK_LSHIFT): LSHIFT_DOWN,
    (SDL_KEYDOWN, SDLK_RSHIFT) : RSHIFT_DOWN,
    (SDL_KEYUP, SDLK_LSHIFT): LSHIFT_UP,
    (SDL_KEYUP, SDLK_RSHIFT): RSHIFT_UP
}


# Boy States
class IdleState:
    @staticmethod
    def enter(boy, event):
        if event == RIGHT_DOWN:
            boy.velocity += RUN_SPEED_PPS
        elif event == LEFT_DOWN:
            boy.velocity -= RUN_SPEED_PPS
        elif event == RIGHT_UP:
            boy.velocity -= RUN_SPEED_PPS
        elif event == LEFT_UP:
            boy.velocity += RUN_SPEED_PPS
        boy.timer = 10.0

    @staticmethod
    def exit(boy, event):
        if event == SPACE:
            boy.fire_ball()

    @staticmethod
    def do(boy):
        boy.frame = (boy.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8
        boy.timer-=game_framework.frame_time
        if boy.timer <= 0:
            boy.add_event(SLEEP_TIMER)

    @staticmethod
    def draw(boy):
        if boy.dir == 1:
            boy.image.clip_draw(int(boy.frame) * 100, 300, 100, 100, boy.x, boy.y)
        else:
            boy.image.clip_draw(int(boy.frame) * 100, 200, 100, 100, boy.x, boy.y)


class RunState:
    @staticmethod
    def enter(boy, event):
        if event == RIGHT_DOWN:
            boy.velocity += RUN_SPEED_PPS
        elif event == LEFT_DOWN:
            boy.velocity -= RUN_SPEED_PPS
        elif event == RIGHT_UP:
            boy.velocity -= RUN_SPEED_PPS
        elif event == LEFT_UP:
            boy.velocity += RUN_SPEED_PPS
        boy.dir = clamp(-1, boy.velocity, 1)
    @staticmethod
    def exit(boy, event):
        if event == SPACE:
            boy.fire_ball()
    @staticmethod
    def do(boy):
        boy.frame = (boy.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8
        boy.timer -= 1
        boy.x += boy.velocity * game_framework.frame_time
        boy.x = clamp(25, boy.x, 1600 - 25)
    @staticmethod
    def draw(boy):
        if boy.velocity == RUN_SPEED_PPS:
            boy.image.clip_draw(int(boy.frame) * 100, 100, 100, 100, boy.x, boy.y)
        else:
            boy.image.clip_draw(int(boy.frame) * 100, 0, 100, 100, boy.x, boy.y)


class SleepState:
    @staticmethod
    def enter(boy, event):
        ghost = Ghost(boy)
        game_world.add_object(ghost, 1)

    @staticmethod
    def exit(boy, event):
        pass

    @staticmethod
    def do(boy):
        boy.frame=(boy.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8

    def draw(boy):
        if boy.dir == 1:
            boy.image.clip_composite_draw(int(boy.frame) * 100, 300, 100, 100, 3.141592/2, '', boy.x-25, boy.y-25, 100, 100)
            #boy.image.opacify(boy.alpha)
            #boy.image.clip_composite_draw(int(boy.frame) * 100, 300, 100, 100, 3.141592/2 * boy.theta, '', boy.gx-25, boy.gy, 100, 100)
            #boy.image.opacify(1)
        else:
            boy.image.clip_composite_draw(int(boy.frame) * 100, 200, 100, 100, -3.141592/2, '', boy.x+25, boy.y-25, 100, 100)
            #boy.image.opacify(boy.alpha)
            #boy.image.clip_composite_draw(int(boy.frame) * 100, 200, 100, 100, -3.141592/2 * boy.theta, '', boy.gx+25, boy.gy, 100, 100)
            #boy.image.opacify(1)


class DashState:
    @staticmethod
    def enter(boy, event):
        boy.timer = 50
    @staticmethod
    def exit(boy, event):
        if event == SPACE:
            boy.fire_ball()
    @staticmethod
    def do(boy):
        boy.frame = (boy.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8
        boy.timer -= 1
        if boy.timer == 0:
            boy.add_event(TIRED_TIMER)
        boy.x += 3*boy.velocity
        boy.x = clamp(25, boy.x, 1600 - 25)
    @staticmethod
    def draw(boy):
        if boy.velocity == 1:
            boy.image.clip_draw(int(boy.frame) * 100, 100, 100, 100, boy.x, boy.y)
        else:
            boy.image.clip_draw(int(boy.frame) * 100, 0, 100, 100, boy.x, boy.y)


next_state_table = {
    IdleState: {RIGHT_UP: RunState, LEFT_UP: RunState, RIGHT_DOWN: RunState, LEFT_DOWN: RunState, SLEEP_TIMER: SleepState, SPACE: IdleState, LSHIFT_UP: IdleState, RSHIFT_UP: IdleState, LSHIFT_DOWN: IdleState, RSHIFT_DOWN: IdleState},
    RunState: {RIGHT_UP: IdleState, LEFT_UP: IdleState, LEFT_DOWN: IdleState, RIGHT_DOWN: IdleState, SPACE: RunState, LSHIFT_DOWN: DashState, RSHIFT_DOWN: DashState, LSHIFT_UP: RunState, RSHIFT_UP: RunState},
    SleepState: {RIGHT_UP: RunState, LEFT_UP: RunState, RIGHT_DOWN: RunState, LEFT_DOWN: RunState, SPACE: IdleState, LSHIFT_UP: IdleState, RSHIFT_UP: IdleState, LSHIFT_DOWN: IdleState, RSHIFT_DOWN: IdleState},
    DashState:{RIGHT_UP: IdleState, LEFT_UP: IdleState, LEFT_DOWN: IdleState, RIGHT_DOWN: IdleState, SPACE: DashState, LSHIFT_UP: RunState, RSHIFT_UP: RunState, TIRED_TIMER: RunState, LSHIFT_DOWN: DashState, RSHIFT_DOWN: DashState}
}

class Boy:
    def __init__(self):
        self.x, self.y = 1600 // 2, 90
        self.gx, self.gy = self.x, self.y
        self.image = load_image('animation_sheet.png')
        self.font = load_font('ENCR10B.TTF', 16)
        self.dir = 1
        self.velocity = 0
        self.frame = 0
        self.timer = 0
        self.event_que = []
        self.cur_state = IdleState
        self.cur_state.enter(self, None)

    def fire_ball(self):
        ball = Ball(self.x, self.y, self.dir*3)
        game_world.add_object(ball, 1)

    def add_event(self, event):
        self.event_que.insert(0, event)

    def update(self):
        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)

    def draw(self):
        self.cur_state.draw(self)
        self.font.draw(self.x-60, self.y+50, '(time : %3.2f)' % get_time(), (255, 255, 0))


    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)
class Ghost:
    def __init__(self, boy):
        self.boy = boy
        self.image = load_image('animation_sheet.png')
        self.x, self.y = boy.x, boy.y
        self.sx, self.sy = boy.x, boy.y
        self.width, self.height = 0, 0
        self.frame = 0
        self.alpha = 0.5
        self.theta = 1
        self.radian = math.radians(-90)
        self.dir = 1


    def update(self):
        if self.boy.cur_state != SleepState:
            game_world.remove_object(self)

        self.frame=(self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8
        self.alpha = random.randint(1, 6) / 10.0
        self.image.opacify(self.alpha)
        self.x += RUN_SPEED_PPS * game_framework.frame_time * self.dir * 4
        self.x = clamp(self.sx - RUN_SPEED_PPS /4 , self.x, self.sx + RUN_SPEED_PPS /4 )
        if self.x == self.sx-RUN_SPEED_PPS /4  or self.x == self.sx+RUN_SPEED_PPS /4 :
            self.dir *= -1
        self.y += RUN_SPEED_PPS * game_framework.frame_time
        self.y = clamp(self.sy, self.y, self.y + RUN_SPEED_PPS)

        self.width += 200 * game_framework.frame_time
        self.width = clamp(0, self.width, 100)
        self.height += 200 * game_framework.frame_time
        self.height = clamp(0, self.height, 100)

        self.theta -= game_framework.frame_time
        self.theta = clamp(0, self.theta, 1)
        if self.theta == 0:
            self.x = self.sx + RADIUS_PIXEL * math.cos(self.radian)
            self.y = self.sy + RUN_SPEED_PPS + RADIUS_PIXEL + RADIUS_PIXEL * math.sin(self.radian)
            self.radian += THETA_PER_SEC * game_framework.frame_time


    def draw(self):
        self.image.clip_composite_draw(int(self.frame) * 100, 300, 100, 100, 3.141592 / 2 * self.theta, '', self.x - 25, self.y, self.width, self.height)

#Ball Class

class Ball:
    image = None
    def __init__(self, x=800, y=300, velocity =1):
        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')
        self.x, self.y, self.velocity = x, y, velocity

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        self.x += self.velocity
        if self.x <25 or self.x > 1600 - 25:
            game_world.remove_object(self)