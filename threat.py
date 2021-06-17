# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


class Cell:
    def __init__(self, piece, i, j):
        self.piece = piece
        self.i = i
        self.j = j


current = None


# Function will return true if there's a threat on up, down vertical
def checkVertical(board, i, j):  # Check if opponents queen can kill our piece

    threat = False
    x = i + 1
    y = j

    # Check down
    while x < 8:
        print(x, y)
        if board[x][y] != ' ':  # If board isn't empty, check if Q or R then break either ways

            if board[x][y] == 'q' or board[x][y] == 'r':
                threat = True
                print("Threat")



            break

        x += 1

    if not threat:  # If no threat down, only the check up
        x = i - 1
        y = j
        print("\n")

        # Check up
        while x >= 0:
            print(x, y)

            if board[x][y] != ' ':  # If board isn't empty, check if Q or R then break either ways

                if board[x][y] == 'q' or board[x][y] == 'r':
                    threat = True

                break

            x -= 1

    return threat


# Function will return true if there's a threat on up, down horizontal
def checkHorizontal(board, i, j):  # Check if opponents queen can kill our piece

    x = i
    y = j + 1
    threat = False

    # Check right
    while y < 8:
        print(x, y)
        if board[x][y] != ' ':  # If board isn't empty, check if Q or R then break either ways

            if board[x][y] == 'q' or board[x][y] == 'r':
                threat = True


            break
        y += 1

    if not threat:
        x = i
        y = j - 1
        print("\n")

        # Check left
        while y >= 0:
            print(x, y)
            if board[x][y] != ' ':  # If board isn't empty, check if Q or R then break either ways

                if board[x][y] == 'q' or board[x][y] == 'r':
                    threat = True



                break
            y -= 1

    return threat


# Function will return true if there's a threat on right, left diagonal
def checkDiagonal(board, i, j):
    x = i + 1
    y = j + 1
    threat = False

    # Right Diagonal Down
    while x < 8 and y < 8:

        print(x, y)
        if board[x][y] != ' ':

            if board[x][y] == 'q' or board[x][y] == 'b':
                threat = True



            break
        x += 1
        y += 1

    # Right diagonal up
    if not threat:

        x = i - 1
        y = j + 1

        while x >= 0 and y < 8:

            print(x, y)
            if board[x][y] != ' ':

                if board[x][y] == 'q' or board[x][y] == 'b':
                    threat = True


                break
            x -= 1
            y += 1

    # Left diagonal down
    if not threat:

        x = i + 1
        y = j - 1

        while x < 8 and y >= 0:

            print(x, y)
            if board[x][y] != ' ':

                if board[x][y] == 'q' or board[x][y] == 'b':
                    threat = True



                break
            x += 1
            y -= 1

    # Left Diagonal up
    if not threat:

        x = i - 1
        y = j - 1

        while x >= 0 and y >= 0:

            print(x, y)
            if board[x][y] != ' ':

                if board[x][y] == 'q' or board[x][y] == 'b':
                    threat = True
                    print("Threat")

                break
            x -= 1
            y -= 1

    return threat


# def checkKnight(i, j):

# def checkPawnKing(i, j):


def checkThreat(board, i, j):
    # If vert Or horizontal Or L Or pawn or King, return True.
    # print("Check Threat:",
    #     (checkHorizontal(board, i, j) or checkVertical(board, i, j) or checkDiagonal(board, i,
    #                                                                                 j)))  # or checkVertical(i, j))

    return checkHorizontal(board, i, j) or checkVertical(board, i, j) or checkDiagonal(board, i, j)
