def display_board():
    print('---------')
    print("|", board[0][2], board[1][2], board[2][2], "|")
    print("|", board[0][1], board[1][1], board[2][1], "|")
    print("|", board[0][0], board[1][0], board[2][0], "|")
    print('---------')


def check_coordinates(symbol):
    while True:
        coords = input('Enter the coordinates:').split()
        if coords[0].isalpha() or coords[1].isalpha():
            print('You should enter numbers!')
        elif int(coords[0]) < 1 or int(coords[0]) > 3 or int(coords[1]) < 1 or int(coords[1]) > 3:
            print('Coordinates should be from 1 to 3!')
        elif board[int(coords[0]) - 1][int(coords[1]) - 1] != ' ':
            print('This cell is occupied! Choose another one!')
        else:
            board[int(coords[0]) - 1][int(coords[1]) - 1] = symbol
            break


def check_win():
    flat_board = []
    for j in range(2, -1, -1):
        for i in range(3):
            flat_board.append(board[i][j])
    flat_board = ''.join(flat_board)
    win_stage = [
        flat_board[:3], flat_board[3:6], flat_board[6:9],
        flat_board[:7:3], flat_board[1:8:3], flat_board[2:9:3],
        flat_board[:9:4], flat_board[2:7:2]
    ]
    if "XXX" in win_stage:
        print("X wins")
        return True
    elif "OOO" in win_stage:
        print("O wins")
        return True


cells = [' ' for _ in range(9)]
board = [
    [cells[6], cells[3], cells[0]],
    [cells[7], cells[4], cells[1]],
    [cells[8], cells[5], cells[2]]
]

display_board()
for i in range(9):
    player = 'X' if i % 2 == 0 else 'O'
    check_coordinates(player)
    display_board()
    if check_win():
        break
else:
    print('Draw')