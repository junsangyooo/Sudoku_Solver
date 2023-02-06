# helper functions to handle main process of finding an answer of given Sudoku

# find index of empty square
def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)
    return None

# Check whether num can be inserted to pos
def valid(board, num, pos):
    # Check row
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[1] != i: return False
    
    # Check col
    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i: return False
    
    # Check box
    box_x, box_y = pos[1] // 3, pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x*3, box_x*3 +3):
            if board[i][j] == num and (i, j) != pos: return False
    
    # Else it is valid
    return True

# Solve Sudoku and return True if possible or return False otherwise
def solve(board):
    find = find_empty(board)
    if not find: return True
    row, col = find

    for i in range(1, 10):
        if valid(board, i, find):
            board[row][col] = i

            if solve(board): return True
            board[row][col] = 0
    return False

# Solve given unsolved Sudoku or raise an exception
def get_board(board):
    if solve(board):
        return board
    else:
        raise ValueError
