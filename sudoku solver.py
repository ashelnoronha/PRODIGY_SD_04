board = []
print("Welcome to the Sudoku Solver!")
print("Enter the Sudoku puzzle row by row and use 0 for empty cells:")
print("Enter the Sudoku board")
for i in range(9):
    while True:
        row = input(f"Row {i+1}: ")
        if len(row) == 9 and row.isdigit():
            board.append([int(num) for num in row])
            break
        else:
            print("Invalid input. Please enter 9 digits with 0 for empty cells.")


def empty_board(board):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("-"*21)
        for j in range(9):
            if j%3 == 0 and j != 0:
                print("| ", end="")
            print(str(board[i][j]) + " ", end="")
        print()

def empty_cell(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i,j)
    return None

def valid(board, row, col, num):
    for j in range(9):
        if board[row][j] == num and j != col:
            return False
    for i in range(9):
        if board[i][col] == num and i != row:
            return False
    start_row, start_col = 3* (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[i + start_row][j + start_col] == num and (i + start_row != row or start_col + j != col):
                return False
    return True 

def solve(board):
    cell = empty_cell(board)
    if not cell:
        return True
    row, col = cell
    for num in range(1,10):
        if valid(board, row, col, num):
            board[row][col] = num
            if solve(board):
                return True
            board[row][col] = 0
    return False


empty_board(board)
if solve(board):
    print("Solved Sudoku board\n")
    empty_board(board)
else:
    print("No solution exists")