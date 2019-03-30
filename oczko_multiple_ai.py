import random as rd
import time


def starting_parameters():

    print("------------------------------------ STARTING PARAMETERS")
    word = 'abc'
    print("1) Easy")
    print("2) Medium")
    print("3) Hard")
    difficulty = "abc"
    while difficulty != 1 and difficulty != 2 and difficulty != 3:
        try:
            difficulty = input("Choose difficulty: ")
            difficulty = int(difficulty)
        except Exception:
            print("Error # 2911")
            print("Choose between 1-3")
            difficulty = input("Choose difficulty: ")

    player_money = "abc"
    while type(player_money) == type(word):
        try:                                                                    
            player_money = input("How much money does player have: ")
            player_money = int(player_money)
        except Exception:
            player_money = input("Select you'r player money: ")

    cash_rate = "abc"
    while type(cash_rate) == type(word):
        try:                                                                    
            cash_rate = int(cash_rate)
        except Exception:
            cash_rate = input("Select you cash rate: ")
    print("----------------------------------------- GAME STARTS")
    return player_money, cash_rate, difficulty


class Deck:

    def __init__(self):
        self.cards = [2,3,4,5,6,7,8,9,10,"j","d","k","a"]
        self.cards = self.cards * 4
        self.cards_copy = self.cards.copy()

    def shuffle(self):
        i = 0
        while len(self.cards_copy) != 0:
            a = rd.randint(0, len(self.cards_copy) - 1)
            self.cards[i] = self.cards_copy[a]
            self.cards_copy.pop(a)                                 
            i = i + 1
        return self.cards


class Player:

    def __init__(self, cards, player_points, aces_user, used_cards_player, player_money):
        self.cards = cards
        self.player_points = player_points
        self.aces_user = aces_user
        self.used_cards_player = used_cards_player
        self.player_money = player_money

    def body(self):
        self.id = rd.randint(0, len(self.cards) - 1)
        if self.cards[self.id] == "j":
            self.player_points = self.player_points + 2
        elif self.cards[self.id] == "d":
            self.player_points = self.player_points + 3
        elif self.cards[self.id] == "k":
            self.player_points = self.player_points + 4
        elif self.cards[self.id] == "a":
            self.player_points = self.player_points + 11
            self.aces_user = self.aces_user + 1
        else:
            self.player_points = self.player_points + self.cards[self.id]

        self.used_cards_player.append(self.cards[self.id]) 
        print("----------------------------------------- PLAYER DATA")
        print("you've choosed: ", self.cards[self.id])
        print("your points: ", self.player_points)
        print("used cards by you: ", self.used_cards_player)
        print("player money: ", self.player_money)
        print("----------------------------------------- END OF PLAYER DATA")
        self.cards.pop(self.id) 

    def return_data(self):
        return self.cards, self.player_points, self.aces_user, self.used_cards_player, self.player_money


class Ai:

    def __init__(self, cards, computer_points, used_cards_computer, aces_computer, player_yesno_count):
        self.cards = cards
        self.computer_points = computer_points
        self.used_cards_computer = used_cards_computer
        self.aces_computer = aces_computer
        self.player_yesno_count = player_yesno_count
        # print(self.player_yesno_count)

    def easy(self):
        think = rd.randint(0, 2)
        print("---Start of AI round---")
        time.sleep(0.5)
        print("AI is thinking")
        time.sleep(0.5)
        print(".", sep=' ', end='', flush=True)
        time.sleep(0.2)
        print(".", sep=' ', end='', flush=True)
        time.sleep(0.1)
        print(".", sep=' ', end='', flush=True)
        time.sleep(0.1)
        print()

        does_pick_card = rd.randint(0, 1)
        if does_pick_card == 0 and self.player_yesno_count <= 2:
            self.id = rd.randint(0, len(self.cards))
            if self.cards[self.id] == "j":
                self.computer_points = self.computer_points + 2
            elif self.cards[self.id] == "d":
                self.computer_points = self.computer_points + 3
            elif self.cards[self.id] == "k":
                self.computer_points = self.computer_points + 4
            elif self.cards[self.id] == "a":
                self.computer_points = self.computer_points + 11
                self.aces_computer = self.aces_computer + 1
            else:
                self.computer_points = self.computer_points + self.cards[self.id]

            self.used_cards_computer.append(self.cards[self.id])
            self.cards.pop(self.id)  
        elif does_pick_card == 1 or self.player_yesno_count > 2:
            print("----------------------------------------- AI DECISION")
            print("AI CHOSES NOT TO PICK CARDS")

        print("----------------------------------------- AI DATA")
        print("AI hand: ", self.used_cards_computer)
        print("AI points: ", self.computer_points)
        print("----------------------------------------- END OF AI ROUND")

    def hard(self):
        think = rd.randint(0, 2)
        print("---Start of AI round---")
        time.sleep(0.5)
        print("AI is thinking")
        time.sleep(0.5)
        # print(".", time.sleep(0.5),".",time.sleep(0.5),".")
        print(".", sep=' ', end='', flush=True)
        time.sleep(0.2)
        print(".", sep=' ', end='', flush=True)
        time.sleep(0.1)
        print(".", sep=' ', end='', flush=True)
        time.sleep(0.1)
        print()


        self.id = rd.randint(0, len(self.cards))

        does_pick_card = rd.randint(0, 1)
        if does_pick_card == 0 and self.player_yesno_count <= 2:

            if self.cards[self.id] == "j":
                self.computer_points = self.computer_points + 2
            elif self.cards[self.id] == "d":
                self.computer_points = self.computer_points + 3
            elif self.cards[self.id] == "k":
                self.computer_points = self.computer_points + 4
            elif self.cards[self.id] == "a":
                self.computer_points = self.computer_points + 11
                self.aces_computer = self.aces_computer + 1
            else:
                self.computer_points = self.computer_points + self.cards[self.id]

            self.used_cards_computer.append(self.cards[self.id])
            self.cards.pop(self.id)  # use it as a method
        elif does_pick_card == 1 or self.player_yesno_count > 2:
            print("----------------------------------------- AI DECISION")
            print("AI CHOSES NOT TO PICK CARDS")

        print("----------------------------------------- AI DATA")
        print("AI hand: ", self.used_cards_computer)
        print("AI points: ", self.computer_points)
        print("----------------------------------------- END OF AI ROUND")

    def return_data(self):
        return self.cards, self.computer_points, self.used_cards_computer, self.aces_computer


class Game:

    want_to_play = True

    def __init__(self, player_money, cash_rate, difficulty):
        self.player_yesno_count = 0
        self.aces_user = 0
        self.aces_computer = 0
        self.player_points = 0
        self.cash_rate = cash_rate
        self.player_money = player_money
        self.computer_money = player_money
        self.computer_points = 0
        self.used_cards_player = []
        self.used_cards_computer = []

        self.deck = Deck()
        self.cards = Deck().cards

        self.difficulty = difficulty
        self.ai = Ai(self.cards, self.computer_points, self.used_cards_computer, self.aces_computer, self.player_yesno_count)
        self.player = Player(self.cards, self.player_points, self.aces_user,self.used_cards_player, self.player_money)

    def reset_points(self):
        self.player_points = 0
        self.computer_points = 0
        self.aces_computer = 0
        self.aces_user = 0
        return self.player_points, self.computer_points, self.aces_user, self.aces_computer

    def main_game(self):
        self.deck
        self.deck.shuffle()
        while self.player_money > 0 and self.want_to_play == True:
            game.reset_points()
            while game.is_finished() != False:
                
                player = input("Do you pick your card? yes / no: ")
                
                if (player != "yes") and (player != "no"):
                    print('error #0245 ~ Use answer yes or no')
                if player == "yes":

                    self.player = Player(self.cards, self.player_points, self.aces_user, self.used_cards_player, self.player_money)
                    self.player.body()

                    self.cards = self.player.return_data()[1]
                    self.player_points = self.player.return_data()[2]
                    self.aces_user = self.player.return_data()[3]
                    self.used_cards_player = self.player.return_data()[4]
                    self.player_money = self.player.return_data()[5]

                if player == "no":
                    self.ai = Ai(self.cards, self.computer_points, self.used_cards_computer, self.aces_computer, self.player_yesno_count)

                    self.player_yesno_count += 1
                    print("----------------------------------------- AI ROUND STARTS")
                    print("AI money: ", self.computer_money)
                    if self.difficulty == 1:
                        self.ai.easy()
                    if self.difficulty == 2:
                        self.ai.medium()
                    if self.difficulty == 3:
                        self.ai.hard()

                    self.cards = self.ai.return_data()[0]
                    self.computer_points = self.ai.return_data()[1]
                    self.used_card_computer= self.ai.return_data()[2]
                    self.aces_computer= self.ai.return_data()[3]

            self.want_to_play = input("Do you still want to play? (yes / no): ")
            if self.want_to_play  != "no":
                self.want_to_play = True

        print("End of game")

    def is_finished(self):
        if self.player_points == 21:
            print()
            print('winner is player 1')
            print()
            self.player_money = self.player_money + self.cash_rate
            self.computer_money = self.computer_money - self.cash_rate
            return False

        elif self.computer_points == 21:
            print()
            print('winner is AI ', )
            print()
            self.computer_money = self.computer_money + self.cash_rate
            self.player_money = self.player_money - self.cash_rate
            return False

        elif self.player_points == 22 or self.aces_user == 2:
            print()
            print('YOU WON - two aces')
            print()
            self.player_money = self.player_money + self.cash_rate
            self.computer_money = self.computer_money - self.cash_rate
            return False

        elif  self.computer_points == 22 and self.aces_computer == 2:
            print()
            print("YOU LOST - computer has two aces")
            print()
            self.computer_money = self.computer_money + self.cash_rate
            self.player_money = self.player_money - self.cash_rate
            return False

        elif self.player_points > 22:
            print()
            print("YOU LOST - you've exceeded the limit of points")
            print()
            self.player_money = self.player_money - self.cash_rate
            self.computer_money = self.computer_money + self.cash_rate
            return False

        elif self.computer_points > 22:
            print()
            print("YOU WON - AI exceeded the limit of points")
            print()
            self.player_money = self.player_money + self.cash_rate
            self.computer_money = self.computer_money- self.cash_rate
            return False


starting_parameters = starting_parameters()
player_money = starting_parameters[0]
cash_rate = starting_parameters[1]
difficulty = starting_parameters[2]

game = Game(player_money, cash_rate, difficulty)
game.main_game()








