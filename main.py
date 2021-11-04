# board
board = [[7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]]

def solve(board):
    print("\n")
    print_board(board)
    find = find_empty(board)
    if not find:
        return True
    else:
        row, col = find

    for num in range(1,10):
        if valid(board,num,(row,col)):
            board[row][col] = num

            if solve(board):
                return True
            board[row][col] = 0
    return False
def valid(board, num, pos):
    # check rows
    for col in range(len(board[0])):
        if board[pos[0]][col] == num and pos[1] != col:
            return False
    # check cols
    for row in range(len(board)):
        if board[row][pos[1]] == num and pos[0] != row:
            return False
    # check squares
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for row in range(box_y*3,box_y*3 + 3):
        for col in range(box_x*3, box_x*3 + 3):
            if board[row][col] == num and (row,col) != pos:
                return False

    return True

def print_board(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - -")
        for j in range(len(board[0])):
            if j % 3== 0 and j != 0:
                print("|",end = "")
            if j == 8:
                print(board[i][j])
            else:
                print(board[i][j], end = " ")
def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i,j) # row, coulmn

    return None

print_board(board)
solve(board)
print("_____________________")
print("\n")
print_board(board)


