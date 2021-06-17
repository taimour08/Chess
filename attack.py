# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

score = 0


def updateScore(board, i, j):
    global score

    if board[i][j] == 'p':
        score += 1

    if board[i][j] == 'k':
        score += 3

    if board[i][j] == 'b':
        score += 3

    if board[i][j] == 'r':
        score += 5

    if board[i][j] == 'q':
        score += 9



def pawnAttack(board, i, j):
    moved = False

    if 'z' >= board[i - 1][j + 1] >= 'a':  # Check right up
        board[i - 1][j + 1] = 'P'
        board[i][j] = ' '
        updateScore(board, i-1, j+1)
        moved = True

    if not moved:
        if 'z' >= board[i - 1][j - 1] >= 'a':  # Check left up
            board[i - 1][j - 1] = 'P'
            board[i][j] = ' '
            updateScore(board, i - 1, j - 1)
            # moved = True


#ddef queenAttack(board, i, j):

    # In loops Check the diagonals, horizontal, vertical for opponent
    # If opp. present change value of that index to 'Q' update score
