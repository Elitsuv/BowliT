
# Bowl-IT 

A simple python based program that brings back your childhood.

## Documentation
This Python script simulates a simplified version of the popular game, Hand Cricket. In this game, the user and the computer take turns batting and bowling, with each player choosing a number between 1 and 6. If the numbers match, the batsman is out. Otherwise, the batting team scores the runs equal to the number chosen by the batsman.

How to Play

Toss:

The user is asked if they want to toss a coin.
If yes, the user chooses 'Heads' or 'Tails' and a number between 1 and 6.
The computer also chooses a number between 1 and 6.
The sum of both numbers determines the toss result.
The winner of the toss chooses to bat or bowl.
Batting and Bowling:

The batting team plays until three wickets fall.
The batting team's player chooses a number between 1 and 6.
The bowling team's player (computer or user) also chooses a number.
If the numbers match, the batsman is out.
Otherwise, the batting team scores the number of runs chosen by the batsman.
The teams alternate batting and bowling until the game ends.
Winning the Game:

The team with the higher score at the end of the game wins.
Code Structure

The code is primarily divided into the following functions:

toss(): Handles the coin toss and determines the winner.
batting_innings(): Simulates a batting innings, calculating the score and wickets.
bowling_innings(): Simulates a bowling innings, calculating the runs conceded and wickets taken.
play_game(): Orchestrates the entire game, including the toss, batting, and bowling phases.


## Future Implementation

- Multiplayer
- Dark mode toggle
- Cross platform
- Over implementation


## Contributing

Contributions are always welcome!

See `contributing.md` for ways to get started.

Please adhere to this project's `code of conduct`.


## License 
[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)


## Known Bugs
- Various typo error that don't matches with the innigs.
- Minor toss errors.
