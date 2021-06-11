"""
Backtracking is an algorithmic-technique for solving problems recursively by trying to build a solution incrementally,
one piece at a time, removing those solutions that fail to satisfy the constraints of the problem at any point of time
(by time, here, is referred to the time elapsed till reaching any level of the search tree).

For example, consider the SudoKo solving Problem, we try filling digits one by one.
Whenever we find that current digit cannot lead to a solution, we remove it (backtrack) and try next digit.
This is better than naive approach (generating all possible combinations of digits and then trying every combination
one by one) as it drops a set of permutations whenever it backtracks.
"""
# utilize backtracking to solve sudoku
# 1. pick empty
# 2. Try all numbers
# 3. Find one that works
# 4. Repeat 1 thru 3
# 5. Backtrack until correct solution is found

board = [
        [7, 8, 0, 4, 0, 0, 1, 2, 0],
        [6, 0, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 1, 0, 7, 8],
        [0, 0, 7, 0, 4, 0, 2, 6, 0],
        [0, 0, 1, 0, 5, 0, 9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 1, 2],
        [1, 2, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 9, 2, 0, 6, 0, 0, 7]
    ]

def solve(b):
    """Recursively call to get a solution"""
    # find empty cells
    find = find_empty(b)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1, 10):
        # if num is valid, add to solution
        if valid(b, i, (row, col)):
            b[row][col] = i

            # check if board is solved, if not continue to recursively try until solved
            if solve(b):
                return True

            # reset the last added element because it's obviously not correct
            b[row][col] = 0

    return False


def valid(b, num, pos):
    """Check validity of the rows/cols/boxes"""
    for i in range(len(b[0])):
        # check for duplicate nums in row
        if b[pos[0]][i] == num and pos[1] != i:
            return False

    for i in range(len(b)):
        # check cols for duplicates
        if b[i][pos[1]] == num and pos[0] != i:
            return False

    # check boxes
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    # check boxes for duplicates
    for i in range(box_y * 3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if b[i][j] == num and (i, j) != pos:
                return False

    return True


def print_board(b):
    for i in range(len(b)):
        # print line after every 3rd row
        if i % 3 == 0 and i != 0:
            print('- - - - - - - - - - - - ')

        for j in range(len(b[0])):
            # print vert line every 3rd column
            if j % 3 == 0 and j != 0:
                print(' | ', end='')

            # if at last pos, go to next line
            if j == 8:
                print(b[i][j])
            else:
                print(str(b[i][j]) + ' ', end='')
                

def find_empty(b):
    """Loop through board and find empty square"""
    for i in range(len(b)):
        for j in range(len(b[0])):
            if b[i][j] == 0:
                return (i, j)  # row, col

    return None



print_board(board)
print('')
solve(board)
print('')
print_board(board)