import random

class tictactoe:
    """Tic Tac Toe Game Class
    Attributes:
        board (list): The game board represented as a list of strings.
        player_turn (str): The current player's turn ('X' or 'O').
    Methods:
        get_random_first_player(): Randomly selects the first player.
        show(): Displays the current state of the game board.
        swap_turn(): Switches the turn to the other player. 
        is_board_filled(): Checks if the board is completely filled.
        fix_spot(cell, player): Places the player's mark on the specified cell.
        won(player): Checks if the specified player has won the game.
        start(): Starts the game loop.
    """
    def __init__(self,):
        self.board=[' ']*10
        self.player_turn = 'X'

    def get_random_first_player(self):
        return random.choice(['X','O'])

    def show(self):
        print('\n')
        print(self.board[1]+'|'+self.board[2]+'|'+self.board[3])
        print('-----')
        print(self.board[4]+'|'+self.board[5]+'|'+self.board[6])
        print('-----')
        print(self.board[7]+'|'+self.board[8]+'|'+self.board[9])
        print('\n')

    def swap_turn(self):
        self.player_turn = 'X' if self.player_turn == 'O' else 'O'
        return self.player_turn
    
    def is_board_filled(self):
        return ' ' not in self.board[1:]
    
    def fix_spot(self,cell,player):
        self.board[cell] = player
        
    def won(self,player:str):
        win=[
            [1,2,3],[4,5,6],[7,8,9],
            [1,4,7],[2,5,8],[3,6,9],
            [1,5,9],[3,5,7]
        ]
        for condition in win:
            if all(self.board[i]==player for i in condition):
                return True
            
        return False
    
    def start(self):
        """"Starts the Tic Tac Toe game loop.
        The game continues until a player wins or the board is filled (draw).
        Players take turns to input their moves by specifying cell numbers (1-9).
        Validates moves and announces the game result.
    """
        while True:
            self.show()
            print(f"Player {self.player_turn} turn")
            cell = int(input("Enter the cell number (1-9) to fix spot: "))

            if self.board[cell] == ' ' and cell in range(1,10):
                self.fix_spot(cell,self.player_turn)

                if self.won(self.player_turn):
                    self.show()
                    print(f"Player {self.player_turn} won the game!")
                    break
                
                if self.is_board_filled():
                    print("Draw!")
                    break
                self.swap_turn()
            else:
                print("Invalid cell! Try again.")
                
if __name__ == '__main__':
    game = tictactoe()
    game.start()