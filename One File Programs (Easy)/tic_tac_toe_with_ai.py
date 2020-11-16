import random


def display_board(board):
    print('---------')
    print('|', board[0][2], board[1][2], board[2][2], '|')
    print('|', board[0][1], board[1][1], board[2][1], '|')
    print('|', board[0][0], board[1][0], board[2][0], '|')
    print('---------')


class TicTacToe:

    def __init__(self):
        self.cells = [' ' for _ in range(9)]
        self.board = [
            [self.cells[6], self.cells[3], self.cells[0]],
            [self.cells[7], self.cells[4], self.cells[1]],
            [self.cells[8], self.cells[5], self.cells[2]]
        ]
        self.player_symbol = None

    def ai_player_turn(self):
        print('Making move level "easy"')
        while True:
            row = random.randint(0, 2)
            col = random.randint(0, 2)
            if self.board[row - 1][col - 1] != ' ':
                continue
            else:
                self.board[row - 1][col - 1] = 'O'
                display_board(self.board)
                break

    def human_player_turn(self):
        self.player_symbol = 'X'
        self.get_coordinates()
        display_board(self.board)

    def get_coordinates(self):
        while True:
            cds = input('Enter the coordinates: ').split()
            if cds[0].isalpha() or cds[1].isalpha():
                print('You should enter numbers!')
            elif int(cds[0]) < 1 or int(cds[0]) > 3 or int(cds[1]) < 1 or int(cds[1]) > 3:
                print('Coordinates should be from 1 to 3!')
            elif self.board[int(cds[0]) - 1][int(cds[1]) - 1] != ' ':
                print('This cell is occupied! Choose another one!')
            else:
                self.board[int(cds[0]) - 1][int(cds[1]) - 1] = self.player_symbol
                break

    def check_win(self):
        flat_cells = []
        for col in range(2, -1, -1):
            for row in range(3):
                flat_cells.append(self.board[row][col])
        flat_board = ''.join(flat_cells)
        winning_stage = [
            flat_board[:3], flat_board[3:6], flat_board[6:9],
            flat_board[:7:3], flat_board[1:8:3], flat_board[2:9:3],
            flat_board[:9:4], flat_board[2:7:2]
        ]
        if 'XXX' in winning_stage:
            print('X wins')
            return True
        elif 'OOO' in winning_stage:
            print('O wins')
            return True

    def game_play(self):
        display_board(self.board)
        for i in range(9):
            if i % 2 == 0:
                self.human_player_turn()
            else:
                self.ai_player_turn()

            if self.check_win():
                break
        else:
            print('Draw')


tic_tac_toe = TicTacToe()
tic_tac_toe.game_play()
