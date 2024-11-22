import random

def roll_dice():
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    dice3 = random.randint(1,6)

    return [dice1, dice2, dice3]

def check_tuple_out(dice):
    if (dice[0] == dice[1] == dice[2]):
        print("This player has tupled out")
        return True
    else:
        return False

def get_fixed(dice):
    if dice[0] == dice[1]:
        return [0, 1]
    elif dice[0] == dice[2]:
        return [0,2]
    elif dice[1] == dice[2]:
        return [1, 2]
    else: 
        return[]
        

def play_turn(player_name):
    print(f"It is {player_name}'s turn. Their dice will now be rolled.")
    dice_rolls = roll_dice()
    dice1 = dice_rolls[0]
    dice2 = dice_rolls[1]
    dice3 = dice_rolls[2]
    print(f"The following values have been rolled: {dice1}, {dice2}, {dice3}\nThis player now has {dice1 + dice2+ dice3} points")
    final_value = dice1 + dice2+ dice3
    if check_tuple_out(dice_rolls):
        final_value = 0
    while(input("Press ENTER to continue, or anything else to end your turn\n") == ''):
        dice_rolls = roll_dice()
        dice1 = dice_rolls[0]
        dice2 = dice_rolls[1]
        dice3 = dice_rolls[2]
        print(f"The following values have been rolled: {dice1}, {dice2}, {dice3}\nThis player now has {dice1 + dice2+ dice3} points")

print("Welcome to the dice game!\nTo start, enter each player's name")
player_1 = input("Player 1 Name: ")
player_2 = input("Player 2 Name: ")
print(f"{player_1} will start. Then {player_2} will go.")
play_turn(player_1)