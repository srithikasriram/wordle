from tkinter import *

import keyboard
from gameboard import GameBoard
from keyboard import KeyBoard
from word import Word
import random
import requests
WORDS_URL = "https://darkermango.github.io/5-Letter-words/words.json"

def guess_submitted():
    game_board.create_word()
    user_guess = game_board.create_word()
    color_list = correct_word.check_match(game_board.create_word())
    game_board.change_tile_color(color_list)
    game_board.check_win_loss(color_list, correct_word)
    keyboard.update_keyboard(user_guess.display_word(), color_list)

# Create Gameboard
screen = Tk()
screen.title("Wordle")
screen.config(width=700, height=900)
game_board = GameBoard(guess_submitted)
keyboard = KeyBoard()
screen.bind("<Key>", game_board.key_pressed)

# Correct Word
response = requests.get(url=WORDS_URL)
word_list = response.json()["words"]
correct_word = Word(random.choice(word_list).upper())

screen.mainloop()
