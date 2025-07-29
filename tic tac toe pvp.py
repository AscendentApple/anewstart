import os
import time
from typing import List, Optional
#fk these modules took most of my time figuring out what i fked up here

class TicTacToe:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.scores = {'Player 1 (X)': 0, 'Player 2 (O)': 0}
        self.current_player = 'X'
        self.current_player_name = 'Player 1 (X)'

        #thihs one was easy classes r tsomething i alr knew about

    def clear_screen(self):
        os.system('cls')
        #ofc we would need to clear the screen

    def display_board(self):
        self.clear_screen()
        print("\n=== TIC TAC TOE ===")
        print("\nCurrent Scores:")

        #isnt this a cool feature!!!

        print(f"Player 1 (X): {self.scores['Player 1 (X)']}")
        print(f"Player 2 (O): {self.scores['Player 2 (O)']}")
        print("\nCurrent Board:")
        print("     0   1   2")
        print("   +---+---+---+")

        # yep i chose - and +

        for i, row in enumerate(self.board):
            print(f" {i} | {' | '.join(row)} |")
            print("   +---+---+---+")
        print(f"\n{self.current_player_name}'s turn")

    def make_move(self, row: int, col: int) -> bool:
        if self.board[row][col] == ' ':
            self.board[row][col] = self.current_player
            return True
        return False

    def check_winner(self) -> Optional[str]:

        # Check rows and columns -_-

        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != ' ':
                return self.current_player
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != ' ':
                return self.current_player

        # Check diagonals-_-

        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            return self.current_player
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            return self.current_player

        return None

    def is_board_full(self) -> bool:
        return all(all(cell != ' ' for cell in row) for row in self.board)

    def switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'
        self.current_player_name = 'Player 2 (O)' if self.current_player == 'O' else 'Player 1 (X)'

    def play_game(self):
        while True:
            self.display_board()
            
            try:
                row = int(input("\nEnter row (0-2): "))
                col = int(input("Enter column (0-2): "))
                
                if not (0 <= row <= 2 and 0 <= col <= 2):
                    print("\nInvalid input! Numbers must be between 0 and 2.")
                    time.sleep(1.5)
                    continue
                    
            except ValueError:
                print("\nInvalid input! Please enter numbers.")
                time.sleep(1.5)
                continue

            if not self.make_move(row, col):
                print("\nThat position is already taken!")
                time.sleep(1.5)
                continue

            winner = self.check_winner()
            if winner:
                self.display_board()
                print(f"\n{self.current_player_name} wins! 🎉")
                self.scores[self.current_player_name] += 1
                break
                
            if self.is_board_full():
                self.display_board()
                print("\nIt's a tie! 🤝")
                break

            self.switch_player()

    def start_game(self):
        print("\nWelcome to Tic Tac Toe!")
        print("Player 1 will be X and Player 2 will be O")
        input("Press Enter to start...")
        
        while True:
            self.play_game()
            play_again = input("\nPlay again? (y/n): ").lower()
            
            if play_again != 'y':
                self.clear_screen()
                print("\nFinal Scores:")
                print(f"Player 1 (X): {self.scores['Player 1 (X)']}")
                print(f"Player 2 (O): {self.scores['Player 2 (O)']}")
                print("\nThanks for playing! 👋")
                break
                
            self.board = [[' ' for _ in range(3)] for _ in range(3)]
            self.current_player = 'X'
            self.current_player_name = 'Player 1 (X)'

if __name__ == "__main__":
    game = TicTacToe()
    game.start_game()
    #bruh this shit ate half of my brain cells