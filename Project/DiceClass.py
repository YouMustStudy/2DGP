from pico2d import*
import random
import main_state
import game_world

class Dice:
    def __init__(self):
        self.image = load_image('.\\icons\\play.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(400, 400, 50, 50)

    def handle_event(self, event):
        if event.x > 400 - 25 and event.x < 400+25 and event.y > 400-25 and event.y < 400+25:
            self.Rolling_Dice()

    def Rolling_Dice(self):
        dice = DiceResult()
        game_world.add_object(dice, 3)

class DiceResult:
    FONT = None
    def __init__(self):
        self.x, self.y = 400, 400
        self.number = random.randint(1, 6)
        self.timer = 1000
        if DiceResult.FONT == None:
            DiceResult.FONT = load_font("C:\\Users\\asaen\\Desktop\\2DGP\\Project\\font\\InterparkGothicBold.ttf", 20)

    def update(self):
        self.timer -= 1
        if self.timer == 0:
            main_state.PLAYER[main_state.PLAYER_TURN].move = self.number
            game_world.remove_object(self)

    def draw(self):
        self.FONT.draw(self.x, self.y, str(self.number))