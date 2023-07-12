class Phrase:
    def __init__(self, phrase):
        self.phrase = phrase.lower()
        self.phrase_list = list(phrase)
        self.puzzle = []
        self.letter_match = False

    def set_puzzle(self):
        for i in range(len(self.phrase_list)):
            if self.phrase_list[i] == " ":
                self.puzzle.append(" ")
            else:
                self.puzzle.append("_")
        return self.puzzle

    def display(self, guesses, ni_count):
        if len(guesses) > 0:
            if ni_count > 0:
                print(f'\nWe have said "Ni!" to you {ni_count} out of 5 times allowed.')
            print(f'    These are the letters you have guessed: {",".join(set(guesses))}\n')
            print("".join(self.puzzle).upper())
        else:
            print("".join(self.puzzle).upper())

    def check_letter(self, guess):
        if guess in self.phrase_list:
            self.letter_match == True
            for i in range(len(self.phrase_list)):
                if guess == self.phrase_list[i]:
                    self.puzzle[i] = guess
            return self.letter_match, self.puzzle
        else:
            self.letter_match = False
            return self.letter_match



    def check_complete(self, ni_count):
        if ni_count == 5:
            complete = True
        elif self.phrase_list == self.puzzle:
            complete = True
        else:
            complete = False
        return complete

