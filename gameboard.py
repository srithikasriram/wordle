from tkinter import *
from word import Word

class GameBoard:
    def __init__(self, guess_func):
        label = Label(text="WORDLE", font=("Times New Roman", 24, "bold"))
        label.grid(row=0, column=0)

        self.win_label = Label(text="", font=("Times New Roman", 16, "bold"))
        self.win_label.grid(row=3, column=0, columnspan=6)
        self.guess_submitted = guess_func
        self.canvas = Canvas()
        self.canvas.config(width=300, height=360)
        self.canvas.grid(row=1, column=0, padx=50, pady=50)
        self.current_row_index = 0
        self.current_col_index = 0
        self.canvas_list = []
        self.letters_list = []

        x1 = 5
        x2 = 55
        y1 = 5
        y2 = 55
        font_x = 30
        font_y = 30
        for row in range(6):
            row_of_tiles = []
            row_of_letters = []
            for tile in range(5):
                new_tile = self.canvas.create_rectangle(x1, y1, x2, y2, outline="black", fill="DarkGray")
                new_letter = self.canvas.create_text(font_x,font_y,text="", font=("Times New Roman", 18, "bold"))
                x1 += 60
                x2 += 60
                font_x += 60
                row_of_tiles.append(new_tile)
                row_of_letters.append(new_letter)
            self.canvas_list.append(row_of_tiles)
            self.letters_list.append(row_of_letters)
            x1 = 5
            x2 = 55
            font_x = 30
            y1 += 60
            y2 += 60
            font_y += 60

    def key_pressed(self, event):
        if event.char.isalpha() and self.current_col_index < 5 and self.current_row_index < 6:
            self.canvas.itemconfig(self.letters_list[self.current_row_index][self.current_col_index], text=event.char.upper())
            self.current_col_index += 1
        elif event.keysym == "BackSpace" and self.current_col_index > 0:
            self.canvas.itemconfig(self.letters_list[self.current_row_index][self.current_col_index-1], text="")
            self.current_col_index -= 1
        elif event.keysym == "Return" and self.current_col_index == 5:
            self.guess_submitted()
            self.current_row_index+=1
            self.current_col_index=0


    def create_word(self):
        word = ""
        for letter in range(5):
            word += self.canvas.itemcget(self.letters_list[self.current_row_index][letter], "text")
        return Word(word)

    def change_tile_color(self, cl):
        for tile in range(5):
            if cl[tile] == "green":
                color = "chartreuse3"
            elif cl[tile] == "yellow":
                color = "DarkGoldenrod1"
            else:
                color = "DarkGray"
            self.canvas.itemconfig(self.canvas_list[self.current_row_index][tile], fill=color)


    def check_win_loss(self, cl, correct):
        is_all_green = True
        for color in cl:
            if color != "green":
                is_all_green = False

        if is_all_green:
            self.win_label.config(text="YOU WIN!")

        elif self.current_row_index >= 5:
            self.win_label.config(text=f"YOU LOSE! \n The word was {correct.display_word()}")





