
import math
grid = [
    [4, 0, 0, 0, 0, 5, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 9, 8],
    [3, 0, 0, 0, 8, 2, 4, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 8, 0],
    [9, 0, 3, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 3, 0, 6, 7, 0],
    [0, 5, 0, 0, 0, 9, 0, 0, 0],
    [0, 0, 0, 2, 0, 0, 9, 0, 7],
    [6, 4, 0, 3, 0, 0, 0, 0, 0],
]


def find_square(row, column):
    # Finding center of the square
    # of point
    global grid
    centersOfSquare = []
    takeRow = 0
    TakeColumn = 1
    CenterOfSquareILookFor = None
    for rowSquare in range(1, 8, 3):
        for columnSquare in range(1, 8, 3):
            centersOfSquare.append([rowSquare, columnSquare])
    for centers in centersOfSquare:
        a = row - centers[takeRow]
        b = column - centers[TakeColumn]
        # Pytagoras
        distanceFromCenter = math.sqrt(a**2 + b**2)
        if(distanceFromCenter <= math.sqrt(2)):
            CenterOfSquareILookFor = centers
    squareNumbers = []
    for i in range(CenterOfSquareILookFor[takeRow]-1, CenterOfSquareILookFor[takeRow]+2):
        for j in range(CenterOfSquareILookFor[TakeColumn]-1, CenterOfSquareILookFor[TakeColumn]+2):
            squareNumbers.append(grid[i][j])
    return squareNumbers

# checking if number in cell is valid


def possible_input(row, column, choice):
    possible_numbers = list(range(1, 10))
    for numbers in grid[row]:
        if(numbers != 0 and numbers in possible_numbers):
            possible_numbers.remove(numbers)
    for i in range(9):
        number = grid[i][column]
        if(number != 0 and number in possible_numbers):
            possible_numbers.remove(number)
    for numbers in find_square(row, column):
        if(numbers != 0 and numbers in possible_numbers):
            possible_numbers.remove(numbers)
    if(choice in possible_numbers):
        return True
    else:
        return False

# Solving Sudoku


def SolveGrid():
    global grid
    for row in range(9):
        for column in range(9):
            if grid[row][column] == 0:
                for i in range(1, 10):
                    if possible_input(row, column, i):
                        grid[row][column] = i
                        SolveGrid()
                        grid[row][column] = 0
                return
    print_sudoku(grid)

# Printing grid of sudoku


def print_sudoku(board):
    print("-"*37)
    for i, row in enumerate(board):
        print(("|" + " {}   {}   {} |"*3).format(*
                                                 [x if x != 0 else " " for x in row]))
        if i == 8:
            print("-"*37)
        elif i % 3 == 2:
            print("|" + "----"*8 + "---|")
        else:
            print("|" + "    "*8 + "   |")
