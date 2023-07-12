from game import Game
from phrase import Phrase
import time
import random

if __name__ == "__main__":

    game = Game()
    play = "y"
    win = False
    game.welcome()
    while play == "y":
        phrase = Phrase(game.get_random_phrase())
        guesses = []
        win = game.start()
        play = game.play_again(win)
    print("\nThis was fun. We should do it again sometime!")
