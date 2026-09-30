from tkinter import Canvas


class KeyBoard:

    def __init__(self):
        letters = [["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P"],
                   ["A", "S", "D", "F", "G", "H", "J", "K", "L"],
                   ["Z", "X", "C", "V", "B", "N", "M"]]
        self.keyboard_canvas = Canvas(width=300, height=90)
        self.keys = {}
        row_index = 0
        for row in letters:
            col_index = 0
            for col in row:
                x = col_index + (300 / len(row)) / 2
                y = row_index * 30 + 15
                self.keys[col] = self.keyboard_canvas.create_text(x, y, text=col, font=("Times New Roman", 10, "italic"), fill="black", tags=f"key_{col}")
                col_index += (300 / len(row))

            row_index += 1

        self.keyboard_canvas.grid(row=2, column=0)

    def update_keyboard(self, word, color_list):
        for i in range(5):
            color = ""
            if color_list[i] == "green":
                color = "chartreuse3"
            elif color_list[i] == "yellow":
                color = "DarkGoldenrod1"
            else:
                color = "DarkGray"
            self.keyboard_canvas.itemconfig(self.keys[word[i]], fill=color)
