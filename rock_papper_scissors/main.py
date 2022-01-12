from math import perm
import random

def play():
    computer = random.choice(['r', 'p', 's'])
    player = input("Choose between 'r, 'p' and 's : \n")

    if player == compile:
        return 'it\'  a tie'
    if is_win(player, computer):
        return 'yay ! you  won'
    return 'you lost'

def is_win(player, computer):
    if (player == 'r' and computer == 's') or ( player == 's' and computer == 'p' ) or (player == 'p' and computer =='r' ):
        return True
 

print(play())