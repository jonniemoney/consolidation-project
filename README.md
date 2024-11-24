# consolidation-project

How to play the "Tuple Out" Dice Game

## How to Run

When you download the foler, you will notice a file called `dice_game.py` this file is our main python script. In order to run the program simply run `python` or `python3` with the file path to this `dice_game.py`.

Ex: `python3 ./dice_game.py`

To navigate to the proper directory, you might have to change directories. This can be done using the `cd` command. 

Ex: `cd consolidation_project`

## How to Play

When you run the code you will be prompted as such

```
Welcome to the dice game!
To start, enter each player's name
Player 1 Name: 
Player 2 Name: 
```

This game is a two player game, and requires you to enter the names of the two players. It is at this point in the program where you will enter the names of the two players that are playing against each other.

The program will prompt you, saying that player 1 goes first and then player 2 goes second. 

Rounds are played until a player has reached 50 pts. At the start of each round, the current score is updated and displayed to the player. 

```
The current point total at round 1:
player1: 0
player2: 0
--------------------------------------------
It is player1's turn. Their dice will now be rolled.
...
```

At each roll, the players dice are displayed as well as the respective point total generated from those dice. The current player can hit ENTER to continue rolling, or they can enter in any other character, and it will end their turn, adding their total points to their overall points. 


```
It is player1's turn. Their dice will now be rolled.
The following values have been rolled: 6, 2, 3
This player now has 11 points
Press ENTER to continue, or anything else to end your turn
```

If a player has two dice of the same value, they will be fixed and they will not continue to be rolled when a player elects to re-roll. The user is not prompted of their fixed dice, but can see that the fixed dice do not change roll to roll. 

```

The following values have been rolled: 3, 5, 5
This player now has 13 points
Press ENTER to continue, or anything else to end your turn

The following values have been rolled: 6, 5, 5
This player now has 16 points
Press ENTER to continue, or anything else to end your turn

The following values have been rolled: 3, 5, 5
This player now has 13 points
Press ENTER to continue, or anything else to end your turn
```

When a player rolls three dice of the same value, they are prompted that they have tupled out. While the point total is displayed of the three dice, 0 points are added to this players total score.

```
The following values have been rolled: 5, 5, 5
This player now has 15 points
This player has tupled out

player1's turn has concluded. It is now player2's turn
```

Once a player wins, the game will end. No players will be able to continue rolling, and the winning player is displayed.

```
player1 has won with 56
```

## How the code works

The code has a very simple flow. 

To start, the user is prompted to enter their names. After this their point totals are initialized at 0 and a while loop is started. The while loop simply runs so long as no player has 50 pts. 

```
print("Welcome to the dice game!\nTo start, enter each player's name")
player_1 = input("Player 1 Name: ")
player_2 = input("Player 2 Name: ")
print(f"{player_1} will start. Then {player_2} will go.")
p1_points = 0
p2_points = 0
round_num = 1
while (p1_points < 50 or p2_points < 50):
```

At each loop of the while loop, a call is made to my play_turn function as such:
`p1_points += play_turn(player_1)`

This play turn function makes use of several other functions I have defined. These functionsa are: `get_fixed, roll_dice, check_tuple_out`

`get_fixed` works by getting the array locations of the dice that are of equal value. This is used to determine if dice should be fized. If they should be fixed, then the `roll_dice` function will not roll these dice. 

The `roll_dice` function works by using the random python package. It works to generate a random number between 1-6 that can be used as the dice values. We roll 3 different dice values and then assign them to our array of dice values. 

Finally, the `check_tuple_out` function works to check if all dice are equal. If all dice are equal, this means there is a tuple out and we return 0 points as well as end the player's turn.