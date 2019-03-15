
class Ai:

    def __init__(self):

        game = Game()
        self.a = game.a
        self.a = self.a + 1


class Game:

    def __init__(self):
        self.ai = Ai()
        self.a = 0
        self.b = 6

    def lajl(self):
        while self.a < self.b:
            print(self.a)

Game()
