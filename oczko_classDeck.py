# import random as rd
# import time
#
#
#
# class Deck:
#
#     def __init__(self):
#         #wpisuj punktacje poszczegolnych kart z klawiatury
#         self.cards = [2,3,4,5,6,7,8,9,10,"j","d","k","a"]
#         self.cards = self.cards * 4
#         self.cards_copy = self.cards.copy()
#
#
#     def shuffle(self):
#         i = 0
#         while len(self.cards_copy) != 0:
#             a = rd.randint(0, len(self.cards_copy) - 1)
#             self.cards[i] = self.cards_copy[a]
#             self.cards_copy.pop(a)   # podobno to zwraca usunięty fragment listy - sprawdź w razie nieznanych problemow
#             i = i + 1
#         return self.cards
#
# class Ai:
#     def __init__(self):
#         print(1)
#
#
# class Game:
#
#
#     def __init__(self, player_money, cash_rate):
#         self.aces_user = 0
#         self.aces_computer = 0
#         self.player_points = 0
#         self.cash_rate = cash_rate
#         self.player_money = player_money
#         self.computer_points = 0
#         self.used_cards_player = []
#         self.used_cards_computer = []
#
#         self.deck = Deck()
#         self.cards = Deck.cards
#
#     def reset_points(self):
#         self.player_points = 0
#         self.computer_points = 0
#         self.aces_computer = 0
#         self.aces_user = 0
#         return self.player_points, self.computer_points, self.aces_user, self.aces_computer
#
#
#     def main_game(self):
#         # Money(self, self.player_money, self.cash_rate)
#         # Game.deck(self)
#         self.deck
#         self.deck.shuffle()
#         while self.player_money > 0:
#             while game.is_finished() != False:
#
#                 print("player money: ", self.player_money)
#
#                 # KTO ZACZYNA
#                 player = input("Do you pick your card? yes / no: ")
#
#                 # JESLI ZACZYNA GRACZ
#                 if (player != "yes") and (player != "no"):
#                     print('error #0245 ~ Use answer yes or no')
#                 if player == "yes":
#                     self.id = rd.randint(0,len(self.cards) - 1)
#                     if self.cards[self.id] == "j":
#                         self.player_points = self.player_points + 2
#                     elif self.cards[self.id] == "d":
#                         self.player_points = self.player_points + 3
#                     elif self.cards[self.id] == "k":
#                         self.player_points = self.player_points + 4
#                     elif self.cards[self.id] == "a":
#                         self.player_points = self.player_points + 11
#                         self.aces_user = self.aces_user + 1
#                     else:
#                         self.player_points = self.player_points + self.cards[self.id]
#
#                     self.used_cards_player.append(self.cards[self.id]) # przydziela do zuzytych kart
#                     print("len(cards): ", len(self.cards))
#                     self.cards.pop(self.id)  # usuwa wylosowana karte
#                     print("-----------------------------------------")
#                     print("TUTAJ TEST: ", self.id, len(self.cards))     # do badania erroru indeksu
#                     print("you've choosed: ", self.cards[self.id])
#                     print("your points: ", self.player_points)
#                     print("used cards by you: ", self.used_cards_player)
#                     print("-----------------------------------------")
#
#                 # JESLI ZACZYNA KOMPUTER
#                 if player == "no":
#                     think = rd.randint(0,2)
#                     print("---Start of AI round---")
#                     time.sleep(0.5)
#                     print("AI is thinking")
#                     time.sleep(0.5)
#                     # print(".", time.sleep(0.5),".",time.sleep(0.5),".")
#                     print(".", sep=' ', end='', flush=True)
#                     time.sleep(0.2)
#                     print(".", sep=' ', end='', flush=True)
#                     time.sleep(0.1)
#                     print(".", sep=' ', end='', flush=True)
#                     time.sleep(0.1)
#                     print()
#
#                     self.id = rd.randint(0,len(self.cards))
#                     print("self id: ", self.id)
#                     if self.cards[self.id] == "j":
#                         self.computer_points = self.computer_points + 2
#                     elif self.cards[self.id] == "d":
#                         self.computer_points = self.computer_points + 3
#                     elif self.cards[self.id] == "k":
#                         self.computer_points = self.computer_points + 4
#                     elif self.cards[self.id] == "a":
#                         self.computer_points = self.computer_points + 11
#                         self.aces_computer = self.aces_computer + 1
#                     else:
#                         self.computer_points = self.computer_points + self.cards[self.id]
#
#                     self.used_cards_computer.append(self.cards[self.id])
#                     self.cards.pop(self.id) # use it as a method
#                     print("-----------------------------------------")
#                     print("AI hand: ", self.used_cards_computer)
#                     print("AI points: ", self.computer_points)
#                     print("End of AI round")
#                     print("-----------------------------------------")
#                     # print("you've choosed: ", self.cards[self.id], "Twoje punkty: ", self.player_points)
#
#     # WARUNKI CZY GRA SKONCZONA
#     def is_finished(self):
#         if self.player_points == 21:
#             print()
#             print('winner is player 1')
#             print()
#             self.player_money = self.player_money + self.cash_rate
#             game.reset_points()
#             return False
#
#         elif self.computer_points == 21:
#             print()
#             print('winner is AI ', )
#             print()
#             self.player_money = self.player_money - self.cash_rate
#             game.reset_points()
#             return False
#
#         elif self.player_points == 22 and self.aces_user == 2:
#             print()
#             print('YOU WON - two aces')
#             print()
#             self.player_money = self.player_money + self.cash_rate
#             game.reset_points()
#             return False
#
#         elif  self.computer_points == 22 and self.aces_computer == 2:
#             print()
#             print("YOU LOST - computer has two aces")
#             print()
#             self.player_money = self.player_money - self.cash_rate
#             game.reset_points()
#             return False
#
#         elif self.player_points > 22:
#             print()
#             print("YOU LOST - you've exceeded the limit of points")
#             print()
#             self.player_money = self.player_money - self.cash_rate
#             game.reset_points()
#             return False
#
#         elif self.computer_points > 22:
#             print()
#             print("YOU WON - AI exceeded the limit of points")
#             print()
#             self.player_money = self.player_money + self.cash_rate
#             game.reset_points()
#             return False
#
#
#
#
# # MAIN
# print("------------------------------------")
# player_money = input("How much money does player have: ")
# player_money = int(player_money)
# cash_rate = "abc"
# word = 'abc'
# while type(cash_rate) == type(word):
#     try:                                        # zapewnia ze wybrana wartosc to liczba
#         cash_rate = int(cash_rate)
#     except Exception:
#         cash_rate = input("Select you cash rate: ")
#
#
# print("------------------------------------")
# iteration = 0
# game = Game(player_money, cash_rate)
#
# game.main_game()
#
#


class A:
    def __init__(self):
        self.a = (1,2,3)

class B: