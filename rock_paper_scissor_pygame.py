import random


class game():


    def __init__(self) :
        self.choices = ['paper','rock','scissor']
        self.player_score = 0
        self.computer_score = 0
    def play_game(self):
        print("Welcome to the rock paper scissors")
        while True:
            player_choice = self.get_player()
            computer_choice = random.choice(self.choices)
            print(f'You Choice: {player_choice}')
            print(f'Oponent Choice: {computer_choice}')
            self.get_winner(player_choice, computer_choice)
            print(f'Your score: {self.player_score}')
            print(f'Computer score: {self.computer_score}')
            play_again = input('Do you want to play again? (y/n) ').lower()
            if play_again != 'y':
                print('Thanks for playing :)')
                break

    def get_player(self):
        while True:
            choice = input("Enter a choice ('paper','rock','scissor')")    
            if choice in self.choices:
                return choice
            else:
                print("Invalid entry! Try Again!")



    def get_winner(self,player_choice, computer_choice):
        if player_choice == computer_choice:
            print("Match draw :<")
        elif (player_choice == 'paper' and computer_choice == 'rock') or (player_choice == 'rock' and computer_choice == 'scissor') or (player_choice == 'scissor' and computer_choice == 'paper'):
            print("You win :)")
            self.player_score +=1
        else:
            print('Computer wins :( ')
            self.computer_score +=1

            



my_game = game()

my_game.play_game()

