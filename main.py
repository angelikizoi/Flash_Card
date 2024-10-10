import tkinter as tk
import pandas as pd
import random


BACKGROUND_COLOR = "#B1DDC6"
try:
    words_df = pd.read_csv("remaining_words.csv")
except FileNotFoundError:
    words_df = pd.read_csv("french_words.csv")

rand_index = ""


def pick_word():
    global rand_index
    rand_index = random.randint(0, len(words_df.index) - 1)
    canvas.itemconfig(canvas_image, image=card_front)
    canvas.itemconfig(canvas_language, text="French", fill="black")
    canvas.itemconfig(canvas_word, text=words_df.iloc[rand_index]["French"], fill="black")
    window.after(3000, change_language, words_df.English[rand_index])
    return rand_index


def correct_word():
    global rand_index
    try:
        words_df = pd.read_csv("remaining_words.csv")
    except FileNotFoundError:
        words_df = pd.read_csv("french_words.csv")
    words_df.drop(axis=0, index=rand_index, inplace=True)
    print(words_df)
    words_df.to_csv("remaining_words.csv", index=False)
    words_df = pd.read_csv("remaining_words.csv")
    pick_word()


def change_language(word):
    canvas.itemconfig(canvas_image, image=card_back)
    canvas.itemconfig(canvas_language, text="English", fill="white")
    canvas.itemconfig(canvas_word, text=word, fill="white")


window = tk.Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = tk.Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = tk.PhotoImage(file="card_front.png")
card_back = tk.PhotoImage(file="card_back.png")
canvas_image = canvas.create_image(400, 263, image=card_front)
canvas_language = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
canvas_word = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

pick_word()

yes_image = tk.PhotoImage(file="right.png")
yes_tick = tk.Button(image=yes_image, highlightthickness=0, command=correct_word)
yes_tick.grid(column=1, row=1)

no_image = tk.PhotoImage(file="wrong.png")
no_tick = tk.Button(image=no_image, highlightthickness=0, command=pick_word)
no_tick.grid(column=0, row=1)

window.mainloop()
