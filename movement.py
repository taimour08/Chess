import threat


def pawnMovement(board, i, j):

    if i == 6:
        if board[i - 2][j] == ' ':

            if not threat.checkThreat(board, i - 2, j):
                board[i][j] = ' '
                board[i - 2][j] = 'P'

        else:
            if board[i - 1][j] == ' ':

                if not threat.checkThreat(board, i - 1, j):
                    board[i][j] = ' '
                    board[i - 1][j] = 'P'



def rookMovement(board, i, j):

    x = i
    y = j + 1

    moved = False

    # Check if rook can move right
    while y < 8:

        if board[x][y] == ' ':

            if not threat.checkThreat(board, x, y): # If threat at right, keep moving further right and check threat again
                board[i][j] = ' '
                board[x][y] = 'R'
                moved = True
                break
        y += 1

    if not moved:

        x = i
        y = j - 1

        # Check if rook can move left
        while y >= 0:

            if board[x][y] == ' ':

                if not threat.checkThreat(board, x, y):
                    board[i][j] = ' '
                    board[x][y] = 'R'
                    moved = True
                    break
            y -= 1

    if not moved:

        x = i - 1
        y = j

        # Check if rook can move up
        while x >= 0:

            if board[x][y] == ' ':

                if not threat.checkThreat(board, x, y):
                    board[i][j] = ' '
                    board[x][y] = 'R'
                    moved = True
                    break
            x -= 1

    if not moved:

        x = i + 1
        y = j

        # Check if rook can move up
        while x < 8:

            if board[x][y] == ' ':

                if not threat.checkThreat(board, x, y):
                    board[i][j] = ' '
                    board[x][y] = 'R'
                    moved = True
                    break
            x += 1

def bishopMovement(board, i, j):

    x = i + 1
    y = j + 1

    moved = False

    # Move right diagonal down
    while x < 8 and y < 8:

        if board[x][y] == ' ':

            if not threat.checkThreat(board, x, y):
                board[i][j] = ' '
                board[x][y] = 'B'
                moved = True
                break
        x += 1
        y += 1

    # Move left diagonal up
    if not moved:

        x = i - 1
        y = j - 1

        while x >= 0 and y >= 0:

            if board[x][y] == ' ':

                if not threat.checkThreat(board, x, y):
                    board[i][j] = ' '
                    board[x][y] = 'B'
                    moved = True
                    break
            x -= 1
            y -= 1

    # Move right diagonal up
    if not moved:

        x = i - 1
        y = j + 1

        while x >= 0 and y < 8:

            if board[x][y] == ' ':

                if not threat.checkThreat(board, x, y):
                    board[i][j] = ' '
                    board[x][y] = 'B'
                    moved = True
                    break
            x -= 1
            y += 1

        # Move left diagonal down
        if not moved:

            x = i + 1
            y = j - 1

            while x >= 0 and y < 8:

                if board[x][y] == ' ':

                    if not threat.checkThreat(board, x, y):
                        board[i][j] = ' '
                        board[x][y] = 'B'
                        moved = True
                        break
                x += 1
                y -= 1

def movePiece(board, i, j):

    # Kis kis ko threat hai and priority
    if board[i][j] == 'P':  # If pawn
        pawnMovement(board, i, j)

    if board[i][j] == 'R':  # If rook
        rookMovement(board, i, j)

    if board[i][j] == 'B':  # If Bishop
        bishopMovement(board, i, j)
