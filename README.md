# Number Guessing Game (CLI)

A simple Python command-line game where the user tries to guess a randomly generated number between 1 and 100.

This project demonstrates:
- Loops (`while`)
- Conditional statements (`if/elif/else`)
- The `random` module
- Error handling with `try/except`
- Input validation
- Loop control using `break` and `continue`

---

## How the Game Works

1. The program generates a random number between 1 and 100.
2. The user is prompted to guess the number.
3. After each guess, the program provides feedback:
   - "Too high"
   - "Too low"
   - "Correct!"
4. The game continues until the correct number is guessed.
5. The program displays the total number of attempts used.

---

##  Input Validation

- Prevents crashes if the user enters non-numeric input.
- Restricts guesses to the range 1–100.
- Uses `continue` to restart the loop when input is invalid.

---

##  Concepts Practiced

- Random number generation
- Infinite loops with exit conditions
- Defensive programming
- Tracking state using variables
- Control flow management

---

## ▶️ How to Run

1. Make sure Python 3 is installed.
2. Navigate to the project directory:

## 📁 Project Structure

number_guessing_game/
├── main.py
├── README.md
└── .gitignore


---

## 🚀 Future Improvements

- Add difficulty levels (easy, medium, hard)
- Limit number of attempts
- Add a "Play Again" feature
- Add scoring system