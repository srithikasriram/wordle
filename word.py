class Word:
    def __init__(self, string):
        self.word = list(string.upper())

    def display_word(self):
        return "".join(self.word)


    def check_match(self, guess):
        color_list = []
        for letter in range(5):
            if self.word[letter].upper() == guess.word[letter].upper():
                color_list.append("green")
            elif guess.word[letter].upper() in self.word:
                color_list.append("yellow")
            else:
                color_list.append("gray")
        return color_list
