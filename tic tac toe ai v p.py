import random
from typing import List, Tuple, Optional
import os
import time

class TicTacToe:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.scores = {'X': 0, 'O': 0}
        self.current_player = 'X'
        self.ai_mode = False

    def display_board(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print('\n')
        print('  Current Scores:')
        print(f'  X: {self.scores["X"]} | O: {self.scores["O"]}')
        print('\n')
        print('    0   1   2')
        for i, row in enumerate(self.board):
            print(f' {i} {" | ".join(row)}')
            if i < 2:
                print('   -----------')
        print('\n')

    def make_move(self, row: int, col: int) -> bool:
        if self.board[row][col] == ' ':
            self.board[row][col] = self.current_player
            return True
        return False

    def check_winner(self) -> Optional[str]:
        # Check rows, columns and diagonals
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != ' ':
                return self.board[i][0]
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != ' ':
                return self.board[0][i]
        
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            return self.board[0][2]
        
        return None

    def is_board_full(self) -> bool:
        return all(all(cell != ' ' for cell in row) for row in self.board)

    def ai_move(self) -> Tuple[int, int]:
        # Try to win
        move = self.find_winning_move('O')
        if move:
            return move

        # Block player's winning move
        move = self.find_winning_move('X')
        if move:
            return move

        # Take center if available
        if self.board[1][1] == ' ':
            return (1, 1)

        # Take corners
        corners = [(0,0), (0,2), (2,0), (2,2)]
        available_corners = [corner for corner in corners if self.board[corner[0]][corner[1]] == ' ']
        if available_corners:
            return random.choice(available_corners)

        # Take any available edge
        edges = [(0,1), (1,0), (1,2), (2,1)]
        available_edges = [edge for edge in edges if self.board[edge[0]][edge[1]] == ' ']
        if available_edges:
            return random.choice(available_edges)

        return (0, 0)

    def find_winning_move(self, player: str) -> Optional[Tuple[int, int]]:
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == ' ':
                    self.board[i][j] = player
                    if self.check_winner() == player:
                        self.board[i][j] = ' '
                        return (i, j)
                    self.board[i][j] = ' '
        return None

    def play_game(self):
        print("\nWelcome to Tic Tac Toe BKL!")
        self.ai_mode = input("Prdy to lose agnst AI? (y/y): ").lower() == 'y'
        
        while True:
            self.display_board()
            
            if self.current_player == 'O' and self.ai_mode:
                print("Sochne dee...")
                time.sleep(1)
                row, col = self.ai_move()
            else:
                try:
                    print(f"Player {self.current_player}'s turn")
                    row = int(input("Enter row (0-2): "))
                    col = int(input("Enter column (0-2): "))
                    if not (0 <= row <= 2 and 0 <= col <= 2):
                        print("Invalid input! lvde 0 aur 2 ke beech me enter krna.")
                        time.sleep(1)
                        continue
                except ValueError:
                    print("Invalid input! bkl number toh dal.")
                    time.sleep(1)
                    continue

            if not self.make_move(row, col):
                print("andha hai kya udahr pehele se hai!")
                time.sleep(1)
                continue

            winner = self.check_winner()
            if winner:
                self.display_board()
                print(f"\nPlayer {winner} wins!")
                self.scores[winner] += 1
                break
            elif self.is_board_full():
                self.display_board()
                print("\nchiii isse bhi nhi jeet paya!")
                break

            self.current_player = 'O' if self.current_player == 'X' else 'X'

        play_again = input("\nOne more round??? (y/n): ").lower()
        if play_again == 'y':
            self.board = [[' ' for _ in range(3)] for _ in range(3)]
            self.current_player = 'X'
            self.play_game()

if __name__ == "__main__":
    game = TicTacToe()
    game.play_game()