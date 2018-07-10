import random
import os

computer = ['rock', 'paper', 'scissors']


def get_locations():
    return random.sample(computer, 1)[0]


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def game_loop():
    playing = True
    while playing:
        choice = get_locations()
        my_choice = input('Rock, paper, scissors, pick one! ')
        my_choice = my_choice.lower()
        if my_choice == str(choice):
            input('{} is the same as {}. We will have to play again!   '.format(my_choice, choice))
        elif (my_choice == 'rock' and choice == 'scissors') or (my_choice == 'paper' and choice == 'rock') or \
                (my_choice == 'scissors' and choice == 'paper'):
            input('Congrats you beat the computer! You chose {} and they chose {}!  '.format(my_choice, choice))
        elif (my_choice == 'rock' and choice == 'paper') or (my_choice == 'paper' and choice == 'scissors') or \
                (my_choice == 'scissors' and choice == 'rock'):
            input('Oh no! The computer beat you, better luck next time!  You chose {} and they chose {}!  '.format(my_choice,
                                                                                                              choice))
        else:
            input('That\'s not a valid choice. Try again!   ')
        clear_screen()


input('Lets play rock paper scissors! Press `Enter` to play!')
clear_screen()
game_loop()
