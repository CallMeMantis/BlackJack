
class Is_finished:

    def __init__(self):
        self.a = Game.a

    def condition(self):
        if self.a > 10:
            return False

class Game:

    def __init__(self):
        is_finished = Is_finished().condition()
        self.a = 0
        a = self.a

    def main_game(self):
        while is_finished != False:
            self.a = self.a + 1

Game()