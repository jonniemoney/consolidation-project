import random

print("Welcome to the dice game!\nTo start, enter each player's name")
player_1 = input("Player 1 Name: ")
player_2 = input("Player 2 Name: ")

player_1_input = input(f"{player_1} will go first. Please press enter to roll your dice.")

def roll_dice(dice1, dice2, dice3):
    if dice1 == dice2 or dice2 == dice3 or dice3 == dice1:
        if dice1 == dice2 and dice2 == dice3:
            print("All dice are equal. This player has tupled out")
        else:
            print("two dice are equal")
    else:
        print("No dice are equal. Rolling all dice again")
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)
        dice3 = random.randint(1,6)



dice1 = random.randint(1,6)
dice2 = random.randint(1,6)
dice3 = random.randint(1,6)

dice_rolls = [dice1, dice2, dice3]
player_1_value = 0
while(True):
    dice1 = dice_rolls[0]
    dice2 = dice_rolls[1]
    dice3 = dice_rolls[2]

    print(f"{player_1} rolled {dice1}, {dice2}, {dice3}. This is a total of {dice1 + dice2 + dice3}.")
    if (dice1 == dice2 and dice2 == dice3):
        print("All three dice have rolled the same number. This player has \"Tupled Out\"")
    else:
        player_1_cont = input(f"{player_1} would you like to re-roll?. If you have two dice that are equal, they will not be re-rolled.\nPress ENTER to re-roll or N to stop")
        if player_1_cont == '':
            roll_dice(dice1, dice2, dice3)
        else:
            player_1_value = dice1 + dice2 + dice3
            print(f"{player_1} has elected to stop rolling. His final value is {player_1_value}")


    
player_2_input = input(f"{player_2} will now go. Please press enter to roll your dice.")


