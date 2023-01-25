import os
from random import randint


class TicTacToe:

    def __init__(self):
        self.board = []

    def create_board(self):
        """Create blank board."""
        for num in range(3):
            row = []
            for i in range(3):
                row.append("-")
            self.board.append(row)

    def show_board(self):
        """Print board to screen."""
        for row in self.board:
            for item in row:
                print(item, end=" ")
            print()

    def player_choice(self):
        """Player marker placement."""
        global play_game
        # Check for a winner
        if self.check_win():
            choice = input("Please choose a square.  Example: 0,2\n> ")
            player_x = int(choice[0])
            player_y = int(choice[2])
            # Check that spot is empty
            if self.board[player_x][player_y] == "-":
                self.board[player_x][player_y] = "X"
            else:
                # If spot is claimed, ask for another choice
                print("That spot is claimed, choose again.")
                game.player_choice()
        else:
            play_game = False

    def computer_choice(self):
        """Random computer marker placement."""
        global play_game
        # Check for winner
        if self.check_win():
            computer_x = randint(0, 2)
            computer_y = randint(0, 2)
            # Check that spot is empty
            if self.board[computer_x][computer_y] == "-":
                self.board[computer_x][computer_y] = "O"
                # Check if board is full
                self.board_not_full()
            else:
                # If spot is claimed, choose again
                self.computer_choice()
        else:
            play_game = False

    def check_win(self):
        """Check for a winning condition.  Return True if no winner to continue game."""
        n = len(self.board)
        # Check rows
        for num in range(n):
            if self.board[num][0] != "-":
                if self.board[num][0] == self.board[num][1] and self.board[num][1] == self.board[num][2]:
                    winner = self.board[num][0]
                    print(f"Game over.  {winner} wins the game!")
                    return False
        # Check columns
        row1 = 0
        row2 = 1
        row3 = 2
        for num in range(n):
            if self.board[row1][num] != "-":
                if self.board[row1][num] == self.board[row2][num] and self.board[row2][num] == self.board[row3][num]:
                    winner = self.board[num][num]
                    print(f"Game over.  {winner} wins the game!")
                    return False
        # Check diagonals
        if self.board[0][0] != "-" and self.board[2][2] != "-":
            if self.board[0][0] == self.board[1][1] and self.board[1][1] == self.board[2][2]:
                winner = self.board[0][0]
                print(f"Game over.  {winner} wins the game!")
                return False
            else:
                return True
        elif self.board[0][2] != "-" and self.board[2][0] != "-":
            if self.board[0][2] == self.board[1][1] and self.board[1][1] == self.board[2][0]:
                winner = self.board[0][2]
                print(f"Game over.  {winner} wins the game!")
                return False
            else:
                return True
        else:
            return True

    def board_not_full(self):
        """Check if the board is full.  Return False if board is full."""
        # Counter for empty spaces
        count = 0
        for row in self.board:
            for item in row:
                if item == "-":
                    count += 1
        if count > 0:
            return True
        else:
            print("The board is full.")
            return False

    def play(self):
        """Run the game."""
        os.system("cls")
        print("Play Tic-Tac-Toe!")
        self.show_board()
        self.player_choice()
        os.system("cls")
        self.show_board()
        self.computer_choice()


game = TicTacToe()
game.create_board()

play_game = True
while play_game:
    game.play()
