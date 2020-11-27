import sys


board = ['_' for _ in range(9)]
turns = 0
ai, human = 'X', 'O'

def print_board():
    print(board[0], board[1], board[2])
    print(board[3], board[4], board[5])
    print(board[6], board[7], board[8])

def check_win():
    flat_board = ''.join(board)
    winning_stage = [
        flat_board[:3], flat_board[3:6], flat_board[6:9],
        flat_board[6::-3], flat_board[7::-3], flat_board[:1:-3],
        flat_board[:9:4], flat_board[6:1:-2]
    ]
    if 'XXX' in winning_stage:
        return 'X'
    elif 'OOO' in winning_stage:
        return 'O'
    elif turns == 9:
        return 'Draw'

def ai_player():
    best_score = -1000
    best_move = None
    for i in range(len(board)):
        if board[i] == '_':
            board[i] = ai
            score = minimax(board, 0, False)
            board[i] = '_'
            if score > best_score:
                best_score = score
                best_move = i
    board[best_move] = ai

scores = {'X': 1, 'O': -1, 'Draw': 0}
def minimax(board, depth, maximizing_player):
    result = check_win()
    if result:
        return scores[result]

    if maximizing_player:
        best_score = -1000
        for i in range(len(board)):
            if board[i] == '_':
                board[i] = ai
                score = minimax(board, depth + 1, False)
                board[i] = '_'
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = 1000
        for i in range(len(board)):
            if board[i] == '_':
                board[i] = human
                score = minimax(board, depth + 1, True)
                board[i] = '_'
                best_score = min(score, best_score)
        return best_score

print_board()
for i in range(9):
    turns += 1
    if i % 2 == 1:
        cdns = int(input('Enter coordinates: '))
        board[cdns] = human
        print_board()
    else:
        print('\nAI player making turn\n')
        ai_player()
        print_board()

    winner = check_win()
    if winner:
        if winner == 'Draw':
            print('DRAW')
        else:
            print(f'{winner} Wins')
            break