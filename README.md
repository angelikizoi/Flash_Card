# Flashcard Application

This is a simple **Flashcard Application** built using Python's **Tkinter** for the graphical user interface (GUI) and **Pandas** to handle word data stored in CSV files. The application helps users practice French-to-English translations by displaying a French word, allowing the user to guess the meaning, and then showing the English translation.

## Features

- Displays a random French word from a dataset.
- After 3 seconds, the word flips to show the English translation.
- Users can mark whether they recalled the word correctly or not.
- If the user marks the word as correct, it is removed from the word list, ensuring that only unfamiliar words remain for future practice.
- Progress is saved automatically, so users can pick up where they left off.

## How It Works

1. **Word Selection**: The app loads words from a CSV file (`french_words.csv`). If progress has been made, it loads the remaining words from `remaining_words.csv`.
2. **Flashcards**: Each flashcard shows a French word on the front. After 3 seconds, the card flips to show the English translation.
3. **User Interaction**: Users can mark whether they recalled the word correctly using the "Correct" or "Incorrect" buttons. Correct words are removed from the dataset, and progress is saved in `remaining_words.csv`.

## Files

- `french_words.csv`: The initial dataset containing French and English word pairs.
- `remaining_words.csv`: The dataset that updates as users progress, removing known words.
- `card_front.png`: The image for the front of the flashcard.
- `card_back.png`: The image for the back of the flashcard.
- `right.png`: The image for the correct (right) button.
- `wrong.png`: The image for the incorrect (wrong) button.

## Requirements

- Python 3.x
- Pandas
- Tkinter (included with Python)

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/angelikizoi/flashcard-app.git
   cd flashcard-app
   ```

2. **Install required dependencies**:
   If you don't have `pandas` installed, you can install it using pip:
   ```bash
   pip install pandas
   ```

3. **Run the application**:
   ```bash
   python flashcard_app.py
   ```

## How to Use

1. When the application starts, it will randomly select a French word from the dataset and display it on the card.
2. After 3 seconds, the card will flip to show the English translation of the word.
3. If you recalled the word correctly, press the "Correct" button (green checkmark), and the word will be removed from future practice sessions.
4. If you didn't recall the word correctly, press the "Incorrect" button (red cross), and the word will remain in the word list for future practice.

## Application Flow

1. **Pick Word**: A random word is selected using `random.randint()`, and the French word is displayed.
2. **Flip Card**: After 3 seconds, the card flips to show the English translation.
3. **User Feedback**: Depending on user input ("Correct" or "Incorrect"), the word list is updated.

## Code Explanation

- **`pick_word()`**: Selects a random word from the dataset and updates the front of the flashcard.
- **`change_language()`**: Changes the flashcard from French to English after 3 seconds.
- **`correct_word()`**: Removes the correctly recalled word from the dataset and saves the updated word list to `remaining_words.csv`.

## Screenshots

![Flashcard Front](./card_front.png)
*Flashcard displaying a French word*

![Flashcard Back](./card_back.png)
*Flashcard displaying the English translation*
