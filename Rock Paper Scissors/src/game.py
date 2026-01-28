"""Author:arefedadshi@gmail.com
Description:This module contains the implementation of a simple Rock-Paper-Scissors game.
"""
import random
from typing import List
class RockPaperScissors:
    """Main in class for Rock Paper Scissors game  """
    def __init__(self,name: str):
        self.choices:List[str] = ['rock', 'paper', 'scissors']
        self.player_name = name

    def get_player_choice(self):
        user_choice:str= input("enter your choice:" )
        if user_choice.lower() in self.choices:
            return user_choice.lower()
        print(f"invalid!select from {self.choices}")
        return self.get_player_choice()  
    
    def get_computer_choice(self):
        """Get computer choice randomly from choices:rock,paper,scissors"""
        return random.choice(self.choices)

    def get_winner(self,user_choice:str,computer_choice:str):
        """Decide the winner between user and computer
        :param user_choice: the choice of user
        :param computer_choice: the choice of computer
        :return:the result of game
        """
        if computer_choice==user_choice:
            return 'it is a tie!'
        win_combinations=[('rock','scissors'),('scissors','paper'),('paper','rock')]
        for win_com in win_combinations:
            if (user_choice,computer_choice) in win_combinations:
                return f'{self.player_name} wins!'
            return 'computer wins!'

    #-quit game or not
    def play(self):
        """play the game
        -Get user choice
        -Get computer choice
        -Decide the winner
        _Print the result
        """
        user_choice=self.get_player_choice()
        computer_choice=self.get_computer_choice()
        print(computer_choice)
        winner_msg=self.get_winner(user_choice,computer_choice)
        print(winner_msg)
    
if __name__ == "__main__":
    game=RockPaperScissors('Ali')

    while True:
        game.play()
        play_again=input("do you want to play again? (y/n): ")
        if play_again.lower() != 'y':
            print("thanks for playing!")
            break