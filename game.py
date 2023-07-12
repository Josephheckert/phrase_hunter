from phrase import Phrase
import random
import time

class Game:
    def __init__(self):
        self.ni_count = 0
        self.phrases = ['use the force', 'a spoon full of sugar helps the medicine go down', 'oh bother', 'we dont talk about bruno', 'you shall not pass']
        self.active_phrase = None
        self.guesses = []
        self.puzzle = []

    def welcome(self):
        print('==================================\nSUPER AWESOME PHRASE GUESSING GAME\n==================================')
        time.sleep(2)
        print('\nThe object of the game is to guess the hidden phrase.\n')
        time.sleep(2)
        print('Here are the rules:\n')
        time.sleep(2)
        print('    1.) You will be prompted to guess a single letter.\n        You must only guess a letter - no numbers, no punctuation, no special characters.')
        time.sleep(3)
        print('    2.) If you guess one of the letters in the hidden phrase, it will be revealed to you. \n        If you guess a letter that is not in the hidden phrase, we will say "Ni!" to you.')
        time.sleep(3)
        print('    3.) If we say "Ni!" to you 5 times, then you lose.')
        time.sleep(3)
        print('    4.) If you reveal all the letters of the hidden phrase before we say "Ni!" to you 5 times, then you win.')

    def taunt(self):
        print('\nOK, we shall prepare ourselves.')
        time.sleep(2)
        print('\nWe will now select the hidden phrase by undoubtedly dark and nefarious methods. Please wait...')
        time.sleep(3)
        print('The hidden phrase has been chosen. You will never guess it. We are ready to say "Ni!" to you many times.\n\n')
        time.sleep(2)

    def get_random_phrase(self):
        phrase_index = random.randint(1,5) - 1
        active_phrase = self.phrases[phrase_index]
        puzzle = list(active_phrase)
        return active_phrase

    def get_guess(self, guesses):
        guess = input("Please guess a letter:    ")
        while not guess.isalpha() or len(guess) != 1 or guess in guesses:
            if guess in guesses:
                guess = input("What a strange person! You already guessed that letter. Try again! Please guess a letter:    ")
            if not guess.isalpha():
                guess = input("You are a son of a silly person! Your mother was a hamster, and you have to guess a number, not a letter or special symbol. Try again! Please guess a letter:    ")
            if len(guess) != 1:
                guess = input("You are a son of a silly person! Your father smelled of elderberry, and you have to guess one letter, and only one letter. Try again! Please guess a letter:    ")
        guesses.append(guess)
        return guess

    def game_over(self, win):
        if win == True:
            print('GAME OVER! You won!')
            time.sleep(1.5)
            print('Wait, you won?!?')
            time.sleep(1.5)
            print(f'This... This is not possible.')
            time.sleep(1.5)
            print('You must have cheated!')
        else:
            print('GAME OVER! You lost!')

    def play_again(self, win):
        if win == True:
            time.sleep(1.5)
            play = input("Cheater, cheater, pumpkin eater! Let's play again, and this time we will catch you in your cheating ways! Want to play again?  (Y/N)    ").lower()
            while play != "y" and play != "n":
                play = input('You must enter "Y" or "N". Want to play again?  (Y/N)    ')
            return play
        else:
            time.sleep(1.5)
            play = input("You have failed to guess the hidden phrase, but we shall let you try another time. Would you like to lose... erm... play again?  (Y/N)    ").lower()
            while play != "y" and play != "n":
                play = input('You must enter "Y" or "N". Would you like to play again?  (Y/N)    ')
            return play

    def start(self):
        phrase = Phrase(self.get_random_phrase())
        complete = False
        win = False
        ni_count = self.ni_count
        phrase.set_puzzle()
        self.taunt()
        while complete == False:
            phrase.display(guesses, ni_count)
            guess = self.get_guess(guesses)
            letter_match = phrase.check_letter(guess)
            if letter_match == False:
                ni_count += 1
            complete = phrase.check_complete(ni_count)
            if complete == True:
                if phrase.puzzle == phrase.phrase_list:
                    win = True
                else:
                    win = False
                self.game_over(win)
                return win


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


