import random

def roll_dice(dice, is_fixed):
    dice1 = dice[0]
    dice2 = dice[1]
    dice3 = dice[2]
    if len(is_fixed) == 0:
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)
        dice3 = random.randint(1,6)
        return [dice1, dice2, dice3]
    else:
        if 0 not in is_fixed:
            dice1 = random.randint(1,6)
            return [dice1, dice2, dice3]
        elif 1 not in is_fixed:
            dice2 = random.randint(1,6)
            return [dice1, dice2, dice3]
        elif 2 not in is_fixed:
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
        return [0,1]
    elif dice[0] == dice[2]:
        return [0,2]
    elif dice[1] == dice[2]:
        return [1,2]
    else: 
        return []
        

def play_turn(player_name):

    print(f"It is {player_name}'s turn. Their dice will now be rolled.")
    dice = [1, 2, 3]
    dice_rolls = roll_dice(dice, [])
    dice1 = dice_rolls[0]
    dice2 = dice_rolls[1]
    dice3 = dice_rolls[2]
    fixed = get_fixed(dice_rolls)
    print(f"The following values have been rolled: {dice1}, {dice2}, {dice3}\nThis player now has {dice1 + dice2+ dice3} points")
    final_value = dice1 + dice2+ dice3
    if check_tuple_out(dice_rolls):
        final_value = 0
        return final_value
    else:
        while(input("Press ENTER to continue, or anything else to end your turn\n") == ''):
            dice_rolls = roll_dice(dice_rolls, fixed)
            fixed = get_fixed(dice_rolls)
            dice1 = dice_rolls[0]
            dice2 = dice_rolls[1]
            dice3 = dice_rolls[2]
            print(f"The following values have been rolled: {dice1}, {dice2}, {dice3}\nThis player now has {dice1 + dice2+ dice3} points")
            final_value = dice1 + dice2 + dice3
            if check_tuple_out(dice_rolls):
                final_value = 0
                break
        return final_value
            


print("Welcome to the dice game!\nTo start, enter each player's name")
player_1 = input("Player 1 Name: ")
player_2 = input("Player 2 Name: ")
print(f"{player_1} will start. Then {player_2} will go.")
p1_points = 0
p2_points = 0
round_num = 1
while (p1_points < 50 or p2_points < 50):
    print(f"The current point total at round {round_num}:")
    print(f"{player_1}: {p1_points}")
    print(f"{player_2}: {p2_points}")
    print("--------------------------------------------")
    p1_points += play_turn(player_1)
    print(f"\n{player_1}'s turn has concluded. It is now {player_2}'s turn")
    p2_points += play_turn(player_2)
    round_num += 1

if p1_points >= 50 or p2_points >= 50:
    if p1_points < p2_points:
        print(f"{player_1} has won with {p1_points}")
    elif p2_points > p1_points:
        print(f"{player_2} has won with {p1_points}")
    elif p2_points == p2_points:
        print(f"You both tied with {p1_points}!")
else:
    print(f"{player_2} has won with {p2_points}")
