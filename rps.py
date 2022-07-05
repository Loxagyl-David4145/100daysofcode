
import random

def play():
    user = input("'R' for rock, 'P' for paper, 'S' for scissors\n").lower()
    computer = random.choice(['r', 'p', 's'])
    if user == computer:
        return 'It\'s a tie'


    if is_win(user, computer):
        return 'You won!'

    return 'You lost!'

    
def is_win(player, opponent):
        if (player == 'R' and opponent == 'S') or (player == 'S' and opponent == 'P') or (player == 'P' and opponent == 'R'):
            return True

print(play())

def print_hand(hand, name='Guest'):
    # Assign a list of hands to the hands variable
    hands = ['Rock','Paper','Scissors']
    
    # Update using an element of the hands variable
    print(name + ' picked: ' + hands[hand])

print('Starting the Rock Paper Scissors game!')
player_name = input('Please enter your name: ')
# Print 'Pick a hand: (0: Rock, 1: Paper, 2: Scissors)'
print('Pick a hand: (0: Rock, 1: Paper, 2: Scissors')

# Get input, convert it, and assign it to the player_hand variable
player_hand = int(input('Please enter a number(0-2): '))

# Change the first argument to player_hand
print_hand(player_hand, player_name)