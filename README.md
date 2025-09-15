# Guessing-Game
A fun and interactive Command-Line Interface (CLI) number guessing game where the player tries to guess a randomly generated number between 1 and 100. The game features multiple difficulty levels, hint system, score tracking, and timing.

**Project Reference**: This project is part of the [roadmap.sh Number Guessing Game challenge](https://roadmap.sh/projects/number-guessing-game)

## 🎮 How to Play

### Starting the Game
Run the game by executing:

 python number_guessing_game.py


# Game Rules

· The computer generates a random number between 1 and 100
· You have limited attempts based on your chosen difficulty level
· After each guess, you'll get feedback if the number is higher or lower
· Use hints when you're stuck!
· Try to guess the number in the fewest attempts possible

###🎯 Difficulty Levels

1. Easy - 10 chances to guess
2. Medium - 5 chances to guess
3. Hard - 3 chances to guess

### 💡 Hint System

During gameplay, type:

· hint or h - Get a random hint about the number
· Hints include: parity (even/odd), divisibility, or range clues

### ⏰ Features

· Timer: Tracks how long you take to guess the number
· High Score System: Saves your best scores for each difficulty level
· Persistent Data: Scores are saved between game sessions
· Quick Quit: Type quit or q to exit anytime
· Multiple Rounds: Play as many games as you want

### 🏆 Scoring

· Your score is the number of attempts it took to guess correctly
· Lower scores are better!
· High scores are saved separately for each difficulty level
· Beat your own records to see the "New high score" message

### 🎮 Game Commands

### Command Action
hint or h Get a helpful hint
quit or q Exit the game
y or yes Play another round
n or no Quit the game

### 📊 Score File

· Scores are saved in scores.json
· File format: {"Easy": 5, "Medium": 3, "Hard": null}
· null means no score recorded yet for that level

### 🛠️ Technical Requirements

· Python 3.x required
· No external dependencies - uses only built-in modules:
  · random - for number generation
  · time - for timing gameplay
  · json - for score saving/loading

### 🎲 Example Gameplay

```
Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.

🏁The scores are:🏁
Easy : 4
Medium : Not yet  
Hard : Not yet

Please select the difficulty level:
1. Easy (10 chances)
2. Medium (5 chances) 
3. Hard (3 chances)

Enter your choice: 2
Great! You have selected the Medium difficulty level.

Enter your guess: 50
Incorrect! The number is less than 50.
Enter your guess: 25
Incorrect! The number is greater than 25.
Enter your guess: h
The number is between 28 and 48
Enter your guess: 35
Congratulations! You guessed the correct number in 4 attempts in 12.5 seconds.
New high score for Medium
```

### ❓ Troubleshooting

· If scores.json gets corrupted, it will automatically reset
· Make sure you have write permissions in the game directory
· The game handles invalid inputs gracefully

### 🔗 Project Reference

This implementation is based on the Number Guessing Game challenge from roadmap.sh - a great platform for developers to improve their skills through practical projects.

### 🚀 Future Enhancements

Potential features for future versions:

· More hint types
· Custom difficulty settings
· Global leaderboard
· Sound effects
· Graphical interface



Enjoy the game! 🎯
