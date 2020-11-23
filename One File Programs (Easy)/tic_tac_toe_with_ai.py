import random
import sys


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

    def ai_player_easy(self):
        print('Making move level "easy"')
        while True:
            row = random.randint(0, 2)
            col = random.randint(0, 2)
            if self.board[row][col] != ' ':
                continue
            else:
                self.board[row][col] = self.player_symbol
                break
        display_board(self.board)

    def ai_player_medium(self):
        row, col = None, None
        winning_scenario = self.calculate_winning_scenario()
        check_symbol = 'X' if self.player_symbol == 'O' else 'O'
        print('Making move level "medium"')
        for i in range(len(winning_scenario)):
            if (winning_scenario[i].count(check_symbol) == 2 or winning_scenario[i].count(self.player_symbol) == 2) and winning_scenario[i].count(' ') == 1:
                x = i
                y = winning_scenario[i].index(' ')
                if x == 0:
                    row, col = y, 2
                elif x == 1:
                    row, col = y, 1
                elif x == 2:
                    row, col = y, 0
                elif x == 3:
                    row, col = 0, y
                elif x == 4:
                    row, col = 1, y
                elif x == 5:
                    row, col = 2, y
                elif x == 6:
                    row = y
                    if y == 0:
                        col = 2
                    elif y == 1:
                        col = 1
                    elif y == 2:
                        col = 0
                elif x == 7:
                    row, col = y, y
                self.board[row][col] = self.player_symbol
                break
        else:
            while True:
                row = random.randint(0, 2)
                col = random.randint(0, 2)
                if self.board[row][col] != ' ':
                    continue
                else:
                    self.board[row][col] = self.player_symbol
                    break
        display_board(self.board)

    def human_player_turn(self):
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
        display_board(self.board)

    def reset_board(self):
        self.cells = [' ' for _ in range(9)]
        self.board = [
            [self.cells[6], self.cells[3], self.cells[0]],
            [self.cells[7], self.cells[4], self.cells[1]],
            [self.cells[8], self.cells[5], self.cells[2]]
        ]

    def calculate_winning_scenario(self):
        flat_cells = []
        for col in range(2, -1, -1):
            for row in range(3):
                flat_cells.append(self.board[row][col])
        flat_board = ''.join(flat_cells)
        winning_stage = [
            flat_board[:3], flat_board[3:6], flat_board[6:9],
            flat_board[6::-3], flat_board[7::-3], flat_board[:1:-3],
            flat_board[:9:4], flat_board[6:1:-2]
        ]
        return winning_stage

    def check_win(self):
        winning_scenario = self.calculate_winning_scenario()
        if 'XXX' in winning_scenario:
            print('X wins')
            self.reset_board()
            return True
        elif 'OOO' in winning_scenario:
            print('O wins')
            self.reset_board()
            return True

    def game_play(self, **kwargs):
        display_board(self.board)
        for i in range(9):
            if i % 2 == 0:
                self.player_symbol = 'X'
                if kwargs['player_x'] == 'easy':
                    self.ai_player_easy()
                elif kwargs['player_x'] == 'medium':
                    self.ai_player_medium()
                else:
                    self.human_player_turn()
            else:
                self.player_symbol = 'O'
                if kwargs['player_o'] == 'easy':
                    self.ai_player_easy()
                elif kwargs['player_o'] == 'medium':
                    self.ai_player_medium()
                else:
                    self.human_player_turn()
            # CHECK WIN STAGE
            if self.check_win():
                break
        else:
            print('Draw')
            self.reset_board()

    def choose_game_mode(self):
        while True:
            mode = input('Input command: ').split()
            if mode[0] == 'exit':
                sys.exit()
            else:
                if mode[0] == 'start':
                    if len(mode) == 3:
                        if (mode[1] == 'easy' or mode[1] == 'user' or mode[1] == 'medium') and (mode[2] == 'easy' or mode[2] == 'user' or mode[2] == 'medium'):
                            self.game_play(player_x=mode[1], player_o=mode[2])
                        else:
                            print('Bad parameters!')
                            continue
                    else:
                        print('Bad parameters!')
                        continue
                else:
                    print('Bad parameters!')


tic_tac_toe = TicTacToe()
tic_tac_toe.choose_game_mode()