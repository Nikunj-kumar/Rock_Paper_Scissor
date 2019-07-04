
#Rock, Paper, Scissors
# Rule - Rock blunts scissor, paper cover rock, scissors cut paper


print("Welcome to the game")
print()
print("You are playing Player vs Computer mode")
print()
print("for rock press 'r' ")
print("for paper press 'p' ")
print("for scissors press 's' ")

from random import randint
print()
print()
print("It's your turn")
print()
print()

player = input("Enter your choice 'r', 'p' and 's'")
if player == 'r' or 'p' or 's':
    print("Wait for computer's turn")
    choosen = randint(1,3)
    if choosen == 1:
        print('r')
    elif choosen == 2:
        print('p')
    else:
        print('s')
else:
    print("Choose valid value")
print()
print()
if player == 'r' and choosen == 1:
    print("Both selected the same, Match drawn")
elif player == 'r' and choosen == 2:
    print("Computer won, cause paper covers rock")
elif player == 'r' and choosen == 3:
    print("Player won, cause rock blunts scissors")
elif player == 'p' and choosen == 1:
    print("Player won, cause paper covers rock")
elif player == 'p' and choosen == 2:
    print("Both selected the same, Match drawn")
elif player == 'p' and choosen == 3:
    print("Computer won, scissor cut paper")
elif player == 's' and choosen == 1:
    print("Computer won, cause rock blunts scissors")
elif player == 's' and choosen == 2:
    print("Player won, scissor cut paper")
elif player == 's' and choosen == 3:
    print("Both selected the same, Match drawn")
elif player != 'r' or 'p' or 's':
    print("Player has entered wrong choice")
else:
    ("Error")







    
