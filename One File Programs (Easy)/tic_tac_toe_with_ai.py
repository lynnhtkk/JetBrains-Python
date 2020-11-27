# Not Finished yet. Hard AI doesn't work as player O

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
        self.turns = 0
        self.opponent = None
        self.player = None

    def ai_player_easy(self):
        print('Making move level "easy"')
        while True:
            row = random.randint(0, 2)
            col = random.randint(0, 2)
            if self.board[row][col] != ' ':
                continue
            else:
                self.board[row][col] = self.player
                break
        display_board(self.board)

    def ai_player_medium(self):
        row, col = None, None
        winning_scenario = self.calculate_winning_scenario(self.board)
        print('Making move level "medium"')
        for i in range(len(winning_scenario)):
            if (winning_scenario[i].count(self.opponent) == 2 or winning_scenario[i].count(self.player) == 2) and \
                    winning_scenario[i].count(' ') == 1:
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
                self.board[row][col] = self.player
                break
        else:
            while True:
                row = random.randint(0, 2)
                col = random.randint(0, 2)
                if self.board[row][col] != ' ':
                    continue
                else:
                    self.board[row][col] = self.player
                    break
        display_board(self.board)

    @staticmethod
    def translate_coordinates(x):
        if x == 0:
            return 0, 2
        elif x == 1:
            return 1, 2
        elif x == 2:
            return 2, 2
        elif x == 3:
            return 0, 1
        elif x == 4:
            return 1, 1
        elif x == 5:
            return 2, 1
        elif x == 6:
            return 0, 0
        elif x == 7:
            return 1, 0
        elif x == 8:
            return 2, 0

    def minimax(self, board, is_maximizing):
        result = self.check_win(board)
        if result:
            if result == self.player:
                return 1
            elif result == self.opponent:
                return -1
            elif result == 'Draw':
                return 0

        if is_maximizing:
            best_score = -1000
            for i in range(len(board)):
                if board[i] == ' ':
                    board[i] = self.player
                    score = self.minimax(board, False)
                    board[i] = ' '
                    best_score = max(score, best_score)
            return best_score
        else:
            best_score = 1000
            for i in range(len(board)):
                if board[i] == ' ':
                    board[i] = self.opponent
                    score = self.minimax(board, True)
                    board[i] = ' '
                    best_score = min(score, best_score)
            return best_score

    def ai_player_hard(self):
        print('Making move level "hard"')
        flat_board = []
        for col in range(2, -1, -1):
            for row in range(3):
                flat_board.append(self.board[row][col])
        best_score = -1000
        best_move = None
        for i in range(len(flat_board)):
            if flat_board[i] == ' ':
                flat_board[i] = self.player
                score = self.minimax(flat_board, False)
                flat_board[i] = ' '
                if score > best_score:
                    best_score = score
                    best_move = i
        row, col = self.translate_coordinates(best_move)
        self.board[row][col] = self.player
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
                self.board[int(cds[0]) - 1][int(cds[1]) - 1] = self.player
                break
        display_board(self.board)

    def reset_board(self):
        self.cells = [' ' for _ in range(9)]
        self.board = [
            [self.cells[6], self.cells[3], self.cells[0]],
            [self.cells[7], self.cells[4], self.cells[1]],
            [self.cells[8], self.cells[5], self.cells[2]]
        ]
        self.turns = 0

    @staticmethod
    def calculate_winning_scenario(board):
        if len(board) == 3:
            flat_cells = []
            for col in range(2, -1, -1):
                for row in range(3):
                    flat_cells.append(board[row][col])
            flat_board = ''.join(flat_cells)
        else:
            flat_board = ''.join(board)
        winning_stage = [
            flat_board[:3], flat_board[3:6], flat_board[6:9],
            flat_board[6::-3], flat_board[7::-3], flat_board[:1:-3],
            flat_board[:9:4], flat_board[6:1:-2]
        ]
        return winning_stage

    def check_win(self, board):
        winning_scenario = self.calculate_winning_scenario(board)
        if 'XXX' in winning_scenario:
            return 'X'
        elif 'OOO' in winning_scenario:
            return 'O'
        elif self.turns == 9 and 'XXX' not in winning_scenario and 'OOO' not in winning_scenario:
            return 'Draw'

    def game_play(self, **kwargs):
        display_board(self.board)
        for i in range(9):
            self.turns += 1
            if i % 2 == 0:
                self.player, self.opponent = 'X', 'O'
                if kwargs['player_x'] == 'easy':
                    self.ai_player_easy()
                elif kwargs['player_x'] == 'medium':
                    self.ai_player_medium()
                elif kwargs['player_x'] == 'hard':
                    self.ai_player_hard()
                else:
                    self.human_player_turn()
            else:
                self.player, self.opponent = 'O', 'X'
                if kwargs['player_o'] == 'easy':
                    self.ai_player_easy()
                elif kwargs['player_o'] == 'medium':
                    self.ai_player_medium()
                elif kwargs['player_o'] == 'hard':
                    self.ai_player_hard()
                else:
                    self.human_player_turn()
            # CHECK WIN STAGE
            winner = self.check_win(self.board)
            if winner:
                if winner != 'Draw':
                    print(f'{winner} wins')
                    break
        else:
            print('Draw')

    def choose_game_mode(self):
        while True:
            self.reset_board()
            mode = input('Input command: ').split()
            if mode[0] == 'exit':
                sys.exit()
            else:
                if mode[0] == 'start':
                    if len(mode) == 3:
                        if (mode[1] == 'easy' or mode[1] == 'user' or mode[1] == 'medium' or mode[1] == 'hard') and (
                                mode[2] == 'easy' or mode[2] == 'user' or mode[2] == 'medium' or mode[2] == 'hard'):
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
