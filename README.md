# Mastermind Game
This is a [Mastermind](https://en.wikipedia.org/wiki/Mastermind_(board_game)) game built in Python using Turtle module.

## Game Mechanics
At the start of the game, a random secret code is generated. The secret code is a set of 4 colors chosen out of 6 colors (For example, ["red", "black", "blue", "yellow"]). Players have up to 10 attempts per round to guess the correct colors and their positions. After each guess, a set of four scoring pegs provides feedback: red pegs indicate correct colors in the wrong positions, while black pegs signify correct colors in the correct positions. The arrangement of these scoring pegs does not correspond to the order of the player's guesses.

On the right side of the game board, a leaderboard showcases the top 10 scores historically achieved. Each new player's name and score are recorded, with scores reflecting the number of attempts taken to correctly guess the code. A player's record is updated only if they achieve a better score than their previous attempts. The game records a score only when a player successfully guesses the secret code. Attempts where the player fails to decipher the code within 10 tries are not recorded.

## Examples
Here are some screenshots of the gameplay:

1. When the user clicks the checkbutton without filling the row:

![image](https://github.com/sssydchen/mastermind/blob/main/Screenshot1.jpg)


2. When the user correctly guessed the secret code, the four scoring pegs on the current row would turn black, and a winner message would display:
   
![image](https://github.com/sssydchen/mastermind/blob/main/Screenshot2.jpg)
