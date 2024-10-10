import tkinter as tk  # For creating the graphical user interface
import pandas as pd  # For handling data manipulation and CSV files
import random  # For selecting random words

# Define the background color of the app
BACKGROUND_COLOR = "#B1DDC6"

# Try to load the remaining words, or if the file doesn't exist, load the original French words
try:
    words_df = pd.read_csv("remaining_words.csv")  # Load remaining words
except FileNotFoundError:
    words_df = pd.read_csv("french_words.csv")  # Load full French words list if remaining words file doesn't exist

# Initialize a global variable to store the index of the current word
rand_index = ""

# Function to pick a random word from the dataset and display the French word on the flashcard
def pick_word():
    global rand_index
    # Pick a random index from the DataFrame
    rand_index = random.randint(0, len(words_df.index) - 1)
    
    # Configure the front side of the flashcard (French side)
    canvas.itemconfig(canvas_image, image=card_front)
    canvas.itemconfig(canvas_language, text="French", fill="black")
    canvas.itemconfig(canvas_word, text=words_df.iloc[rand_index]["French"], fill="black")
    
    # After 3 seconds, flip the card to show the English translation
    window.after(3000, change_language, words_df.English[rand_index])
    return rand_index

# Function to handle when the user knows the word (correct guess)
def correct_word():
    global rand_index
    # Reload the remaining words file, or fallback to the full French words list if not found
    try:
        words_df = pd.read_csv("remaining_words.csv")
    except FileNotFoundError:
        words_df = pd.read_csv("french_words.csv")
    
    # Drop the correctly guessed word from the DataFrame
    words_df.drop(axis=0, index=rand_index, inplace=True)
    print(words_df)  # Print the DataFrame for debugging
    
    # Save the updated DataFrame to the remaining words CSV
    words_df.to_csv("remaining_words.csv", index=False)
    
    # Reload the updated DataFrame and pick another word
    words_df = pd.read_csv("remaining_words.csv")
    pick_word()

# Function to flip the card and display the English translation after 3 seconds
def change_language(word):
    # Configure the back side of the flashcard (English side)
    canvas.itemconfig(canvas_image, image=card_back)
    canvas.itemconfig(canvas_language, text="English", fill="white")
    canvas.itemconfig(canvas_word, text=word, fill="white")

# Initialize the main window
window = tk.Tk()
window.title("Flash Card")  # Set the title of the window
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)  # Set padding and background color

# Create a canvas to hold the flashcard images and text
canvas = tk.Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = tk.PhotoImage(file="card_front.png")  # Load the front side of the flashcard image
card_back = tk.PhotoImage(file="card_back.png")  # Load the back side of the flashcard image
canvas_image = canvas.create_image(400, 263, image=card_front)  # Add the front image to the canvas
canvas_language = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))  # Add language text placeholder
canvas_word = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))  # Add word text placeholder
canvas.grid(column=0, row=0, columnspan=2)  # Position the canvas on the grid

# Pick the first random word to display
pick_word()

# Create the "Correct" button (green checkmark), which calls correct_word when clicked
yes_image = tk.PhotoImage(file="right.png")
yes_tick = tk.Button(image=yes_image, highlightthickness=0, command=correct_word)
yes_tick.grid(column=1, row=1)

# Create the "Incorrect" button (red cross), which picks another word when clicked
no_image = tk.PhotoImage(file="wrong.png")
no_tick = tk.Button(image=no_image, highlightthickness=0, command=pick_word)
no_tick.grid(column=0, row=1)

# Start the Tkinter main loop to run the application
window.mainloop()
